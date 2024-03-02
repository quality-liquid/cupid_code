import base64
from operator import contains
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DaterSerializer, CupidSerializer, ManagerSerializer, MessageSerializer, GigSerializer, \
    DateSerializer, FeedbackSerializer, PaymentCardSerializer, BankAccountSerializer, QuestSerializer
from .models import User, Dater, Cupid, Gig, Quest, Message, Date, Feedback, PaymentCard, BankAccount
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.shortcuts import get_object_or_404
from geopy.geocoders import Nominatim
import geoip2.database
from math import radians, sin, cos, sqrt, atan2
from yelpapi import YelpAPI
import datetime
import speech_recognition
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# 1. write the code for the models
# 2. write doc strings for all the views so we know what they should take in, what they should do, and what they should return
# 3. agree on how the serializers should be used and write the code to use them
# 4. agree on what external APIs we will use
# TODO 5. write the code for the views
# TODO 6. write the tests for the views
# TODO 7. debug

# AI API (pytensor) https://pytensor.readthedocs.io/en/latest/
# Location API (Geolocation) https://pypi.org/project/geolocation-python/
# Speech To Text API (pyttsx3) https://pypi.org/project/pyttsx3/
# Text and Email notifications API (Twilio) https://www.twilio.com/en-us
# Nearby Shops API (yelpapi) https://pypi.org/project/yelpapi/


@api_view(['POST'])
def create_user(request):
    """
    Request the server to create an appropriate dater, cupid, or manager from info given.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
               user_type (str): Dater, Cupid, Manager
               password (str): unhashed password
               confirm_password (str): unhashed password
               username (str)
               email (str)
               first_name (str)
               last_name (str)
               phone_number (str)
               budget (float): the user's default budget
               communication_preference (int): EMAIL = 0, TEXT = 1
               description (str)
               dating_strengths (str)
               dating_weaknesses (str)
               interests (str)
               past (str)
               nerd_type (str)
               relationship_goals (str)
               ai_degree (str)
               cupid_cash_balance (str)
    Returns:
        Response:
            If the user was created successfully, return serialized user and a 200 status code.
            If the user was not created successfully, return an error message and a 400 status code.
    """
    data = request.post
    if data['user_type'] == 'Dater':
        serializer = DaterSerializer(data=data)
    elif data['user_type'] == 'Cupid':
        serializer = CupidSerializer(data=data)
    elif data['user_type'] == 'Manager':
        serializer = ManagerSerializer(data=data)
    else:
        return Response({"error": "invalid user type"}, status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request):
    """
    Get a user's information

    Args (request.post):
        user_id(int): The id of the user
    
    Returns:
        Response:
            Dater, Cupid, or Manager serialized
    """
    data = request.post
    user = get_object_or_404(User, id=data['user_id'])
    if user.role == 'Dater':
        serializer = DaterSerializer(user)
    elif user.role == 'Cupid':
        serializer = CupidSerializer(user)
    elif user.role == 'Manager':
        serializer = ManagerSerializer(user)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def send_chat_message(request):
    """
    For a dater.
    Stores the given message in the database, sends it to the AI, and returns the AI's response.

    Args (request.post):
        user_id(int): The id of the dater
        message(str): The message

    Returns:
        Response:
            message(str): The AI's response
    """
    data = request.post
    user_id = data['user_id']
    message = data['message']
    # save a message to database
    serializer = MessageSerializer(data={'owner': user_id, 'text': message, 'from_ai': False})
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # send a message to AI
    ai_response = __get_ai_response(message)
    # save AI's response to database
    serializer = MessageSerializer(data={'owner': user_id, 'text': ai_response, 'from_ai': True})
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return AI's response
    return Response({'message': ai_response}, status=status.HTTP_200_OK)


def __get_ai_response(message: str):
    """
    Send the message to the AI and return the response.
    https://pytensor.readthedocs.io/en/latest/
    https://huggingface.co/
    """
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    # Tokenize input text
    input_ids = tokenizer.encode(message, return_tensors='pt')
    # Generate response
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)
    # Decode and return response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


@api_view(['GET'])
def get_five_messages(request, pk):
    """
    Returns the five most recent messages between user and AI.

    Args:
        request: information about the request
        pk(int): the user_id as included in the URL
    Returns:
        Response:
            The five messages serialized
    """
    user = get_object_or_404(User, id=pk)
    try:
        messages = Message.objects.filter(owner=user).order_by('-id')[:5]
    except Message.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def calendar(request, pk):
    """
    For a dater.
    Returns the dater's scheduled dates.

    Args (request.post):
        user_id(int): The id of the dater
    Returns:
        Response:
            The planned dates
    """
    if request.method == 'GET':
        dater = get_object_or_404(Dater, id=pk)
        try:
            dates = Date.objects.filter(dater=dater)
        except Date.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = DateSerializer(dates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.post
        serializer = DateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def rate_dater(request):
    """
    For a cupid.
    Saves a rating of a dater to the database.

    Args (request.post):
        user_id(int): The id of the dater
        gig_id(int): The id of the gig
        message(str): Message of feedback
        rating(int): 1-5 stars(hearts)
    Returns:
        Response:
            Saved Feedback serialized
    """
    data = request.post
    cupid = get_object_or_404(Cupid, id=data['user_id'])
    gig = get_object_or_404(Gig, id=data['gig_id'])
    serializer = FeedbackSerializer(
        data={'user': cupid, 'gig': gig, 'message': data['message'], 'star_rating': data['rating']})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_dater_ratings(request, pk):
    """
    For all users.
    Returns the ratings of a specific dater.

    Args:
        request: information about the request
        pk(int): the user_id as included in the URL
    Returns:
        Response:
            Sequence of Feedback objects
    """
    dater = get_object_or_404(Dater, id=pk)
    try:
        ratings = Feedback.objects.filter(user=dater)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = FeedbackSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_avg_rating(request, pk):
    """
    For all users.
    Returns the average rating of a specific user.

    Args:
        request: information about the request
        pk(int): the user_id as included in the URL
    Returns:
        Response:
            rating(int): The dater's rating
    """
    dater = get_object_or_404(Dater, id=pk)
    try:
        ratings = Feedback.objects.filter(user=dater)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    total = 0
    for rating in ratings:
        total += rating.star_rating
    avg = total / len(ratings)
    return Response({'rating': avg}, status=status.HTTP_200_OK)


@api_view(['POST'])
def dater_transfer(request):
    """
    For a dater.
    Charges the dater's card and updates their balance.

    Args (request.post):
        user_id(int): The id of the dater
        card_id(int): The id of the card to charge
        amount(float): The amount to transfer
    Returns:
        Response:
            OK
    """
    data = request.post
    dater = get_object_or_404(Dater, id=data['user_id'])
    card = get_object_or_404(PaymentCard, id=data['card_id'])
    if card.user != dater.user:
        return Response({"error: that card doesnt belong to you"}, status=status.HTTP_400_BAD_REQUEST)
    if card.balance < data['amount']:
        return Response({"error: you dont have that much money"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = PaymentCardSerializer(card)
    if serializer.is_valid():
        serializer.validated_data['balance'] -= data['amount']
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_dater_balance(request, pk):
    """
    For daters.
    Returns the balance of a specific dater.

    Args:
        request: information about the request
        pk(int): the user_id as included in the URL
    Returns:
        Response:
            balance(int): The balance of the dater
    """
    dater = get_object_or_404(Dater, id=pk)
    card = get_object_or_404(PaymentCard, user=dater.user)
    return Response({'balance': card.balance}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_profile(request, pk):
    """
    For daters.
    Returns the profile information of the dater.

    Args:
        request: information about the request
        pk(int): the user_id as included in the URL
    Returns:
        Response:
            The dater serialized
    """

    dater = get_object_or_404(Dater, id=pk)
    serializer = DaterSerializer(dater)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def set_dater_profile(request):
    """
    For a dater.
    Saves the profile data of a dater.

    Args (request.post):
        user_id(int): The id of the dater
        serialized dater
    Returns:
        Response:
            Saved dater serialized
    """
    data = request.post
    dater = get_object_or_404(Dater, id=data['user_id'])
    serializer = DaterSerializer(dater, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def rate_cupid(request):
    """
    For a dater.
    Save a rating of a cupid.

    Args (request.post):
        user_id(int): The id of the cupid
        gig_id(int): The id of the gig
        message(str): Message of feedback
        rating(int): 1-5 stars(hearts)
    Returns:
        Response:
            Saved dater serialized
    """
    data = request.post
    dater = get_object_or_404(Dater, id=data['user_id'])
    gig = get_object_or_404(Gig, id=data['gig_id'])
    serializer = FeedbackSerializer(
        data={'user': dater, 'gig': gig, 'message': data['message'], 'star_rating': data['rating']})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_cupid_ratings(request, pk):
    """
    For all users.
    Returns the ratings of a specific cupid.

    Args:
        request: information about the request
        pk(int): the user_id as included in the URL
    Returns:
        Response:
            Sequence of Feedback objects
    """
    cupid = get_object_or_404(Cupid, id=pk)
    try:
        ratings = Feedback.objects.filter(user=cupid)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = FeedbackSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_avg_rating(request, pk):
    """
    Return the average rating for the requested Cupid.
    
    Args:
        request: Information about the request.
            
        pk (int): ID for the requested user
    Returns:
        Response:
            Average rating from the user's record (int).
            If the account could not be found, return a 400 status code.
    """
    cupid = get_object_or_404(Cupid, id=pk)
    try:
        ratings = Feedback.objects.filter(user=cupid)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    total = 0
    for rating in ratings:
        total += rating.star_rating
    avg = total / len(ratings)
    return Response({'rating': avg}, status=status.HTTP_200_OK)


@api_view(['POST'])
def cupid_transfer(request):
    """
    Performs financial transfer from a Cupid's balance to their bank account.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                cupid_id (int): The id of the Cupid to transfer from.
    Returns:
        Response:
            If the transfer went through successfully, return a 200 status code.
            If the transfer failed, return a corresponding error status code (400 if on our end, 500 if on bank's end)
    """
    data = request.post
    cupid = get_object_or_404(Cupid, id=data['user_id'])
    bank_account = get_object_or_404(BankAccount, user=cupid.user)
    if bank_account.balance < cupid.cupid_cash_balance:
        return Response({"error: you dont have that much money"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = BankAccountSerializer(bank_account)
    if serializer.is_valid():
        serializer.validated_data['balance'] -= cupid.cupid_cash_balance
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_balance(request, pk):
    """
    Returns a number representing the Cupid's balance on their account.

    Args:
        request: Information about the request.
        pk (int): ID for the requested Cupid.
    Returns:
        Response:
            Balance on the Cupid's account (int).
            If the account could not be found, return a 400 status code.
    """
    cupid = get_object_or_404(Cupid, id=pk)
    return Response({'balance': cupid.cupid_cash_balance}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_profile(request, pk):
    """
    Returns all details on a Cupid's profile (details from Cupid record).

    Args: 
        request: Information about the request.
        pk (int): ID for the requested Cupid.
    Returns:
        Response:
            Requested details from Cupid's record (JSON)
    """
    cupid = get_object_or_404(Cupid, id=pk)
    serializer = CupidSerializer(cupid)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def set_cupid_profile(request):
    """
    Creates or changes data in a Cupid's profile.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                cupid_id (int): The id of the Cupid to create or change.
                data (json): The data to create or change in the Cupid's profile.
    Returns:
        Response:
            If the profile was created or changed successfully, return a 200 status code.
            If the profile failed to be created or changed (insufficent permissions, bad data, or error), return a 400 status code.
    """
    data = request.post
    cupid = get_object_or_404(Cupid, id=data['user_id'])
    serializer = CupidSerializer(cupid, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_gig(request):
    """
    Creates a gig.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                dater_id (int): The id of the dater who is requesting the gig.
                quest (json): The quest that the gig is for.
                    quest['budget'] (float): The budget for the gig.
                    quest['items_requested'] (str): The items requested for the gig.
                    quest['pickup_location'] (str): The location to pick up the items for the gig.

    Returns:
        Response:
            If the gig was created correctly, return a 200 status code.
            If the gig was failed to be created, return a 400 status code.
    """
    data = request.post
    dater = get_object_or_404(Dater, id=data['dater_id'])
    serializer = QuestSerializer(data=data['quest'])
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    quest = get_object_or_404(Quest, id=serializer.data['id'])
    serializer = GigSerializer(data={'dater': dater, 'quest': quest})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def accept_gig(request):
    """
    Modifies the gig to show that it has been accepted by a Cupid.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                gig_id (int): The id of the gig to accept.
    Returns:
        Response:
            If the gig was successfully accepted, return a 200 status code.
            If the gig could not be accepted or was already accepted, return a 400 status code.
    """
    data = request.post
    gig = get_object_or_404(Gig, id=data['gig_id'])
    serializer = GigSerializer(gig)
    if serializer.is_valid():
        serializer.validated_data['is_accepted'] = True
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def complete_gig(request):
    """
    Modifies the gig to show that it has been completed.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                gig_id (int): The id of the gig to complete.
    Returns:
        Response:
            If the gig was successfully completed, return a 200 status code.
            If the gig could not be completed or was already completed, return a 400 status code.
    """
    data = request.post
    gig = get_object_or_404(Gig, id=data['gig_id'])
    serializer = GigSerializer(gig)
    if serializer.is_valid():
        serializer.validated_data['is_completed'] = True
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def drop_gig(request):
    """
    Modifies the gig to show that it is no longer claimed by a Cupid. Cupid is no longer in charge of the gig.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                gig_id (int): The id of the gig to drop.
    Returns:
        Response:
            If the gig was successfully dropped, return a 200 status code.
            If the gig could not be dropped, was already dropped, or does not have a Cupid assigned, return a 400 status code.
    """
    data = request.post
    gig = get_object_or_404(Gig, id=data['gig_id'])
    serializer = GigSerializer(gig)
    if serializer.is_valid():
        serializer.validated_data['is_accepted'] = False
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_gigs(request, count):
    """
    Returns a list of gigs, up to the number of `count`.

    Args:
        request: Information about the request.
        count (int): The number of gigs to return and display.
    Returns:
        Response:
            A list of gigs (JSON)
    """
    gigs = Gig.objects.all()
    near_gigs = []
    for gig in gigs:
        cupid = gig.cupid
        quest = gig.quest
        if not gig.is_accepted and __locations_are_near(quest.pickup_location, cupid.location, cupid.gig_range):
            near_gigs.append(gig)
    near_gigs = near_gigs[:count]
    serializer = GigSerializer(near_gigs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def __get_location_string(ip_address):
    latitude, longitude = __get_location_from_ip_address(ip_address)
    return f"{latitude} {longitude}"


def __get_location_from_address(address):
    """
    Returns the location of an address.
    """
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Getting location details
    location = geolocator.geocode(address)

    if location:
        # Extracting latitude and longitude
        latitude = location.latitude
        longitude = location.longitude

        return latitude, longitude
    else:
        return None, None


def __get_location_from_ip_address(ip_address):
    """
    Returns the location of an IP address.
    """
    geoip_database_path = "geodata/GeoLite2-City_20240227/GeoLite2-City.mmdb"
    with geoip2.database.Reader(geoip_database_path) as reader:
        try:
            response = reader.city(ip_address)
            latitude = response.location.latitude
            longitude = response.location.longitude
            return latitude, longitude
        except geoip2.errors.AddressNotFoundError:
            return None, None


def __locations_are_near(location1, location2, max_distance_miles):
    """
    Returns whether two locations are near each other.
    """
    latitude1, longitude1 = location1.split(" ")
    latitude2, longitude2 = location2.split(" ")
    return __within_distance(latitude1, longitude1, latitude2, longitude2, max_distance_miles)


def __haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in miles
    R = 3958.8  # miles

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


def __within_distance(lat1, lon1, lat2, lon2, max_distance_miles):
    distance = __haversine_distance(lat1, lon1, lat2, lon2)
    return distance <= max_distance_miles


@api_view(['GET'])
def get_stores(request, pk):
    """
    Reaches out to an API with an address to get stores near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby stores, including their specific location (JSON)
    """
    response = __call_yelp_api(pk, "stores")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_activities(request, pk):
    """
    Reaches out to an API with an address to get possible activities near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby activities, including their specific location (JSON)
    """
    response = __call_yelp_api(pk, "activities")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_events(request, pk):
    """
    Reaches out to an API with an address to get current entertainment events near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby events, including their specific location (JSON)
    """
    response = __call_yelp_api(pk, "events")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_attractions(request, pk):
    """
    Reaches out to an API with an address to get attractions near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the attractions were retrieved successfully, return a list of nearby attractions, including their specific location amd a 200 status code.
            If the attractions were not retrieved successfully, return an error message and a 400 status code.
    """
    response = __call_yelp_api(pk, "attractions")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_restaurants(request, pk):
    """
    Reaches out to an API with an address to get restaurants near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the restaurants were retrieved successfully, return a list of nearby restaurants, including their specific location and a 200 status code.
            If the restaurants were not retrieved successfully, return an error message and a 400 status code.
    """
    response = __call_yelp_api(pk, "restaurants")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def __call_yelp_api(pk, search):
    dater = get_object_or_404(Dater, id=pk)
    latitude, longitude = dater.location.split(" ")
    api_key = __get_yelp_api_key()
    with YelpAPI(api_key, timeout_s=5.0) as yelp_api:
        try:
            return yelp_api.search_query(term=search, latitude=latitude, longitude=longitude, limit=10)
        except YelpAPI.YelpAPIError as e:
            return None


def __get_yelp_api_key():
    """
    Returns the Yelp API key.
    """
    with open('yelp_api_key.txt', 'r') as file:
        return file.read().split(" ")[-1]


@api_view(['GET'])
def get_user_location(request, pk):
    """
    For gigs, the location of the user is needed to determine the delivery location of the gig.

    Args:
        request: Information about the request.
        pk (int): The id of the user to get the location of.
    Returns:
        Response:
            If the location of the user was retrieved successfully, return the user location and a 200 status code.
            If the location of the user was not retrieved successfully, return an error message and a 400 status code.

    """
    user = get_object_or_404(User, id=pk)
    if user.role == 'Dater':
        user_data = get_object_or_404(Dater, id=pk)
        serializer = DaterSerializer(data=user_data)
    elif user.role == 'Cupid':
        user_data = get_object_or_404(Cupid, id=pk)
        serializer = CupidSerializer(data=user_data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response({'location': serializer.validated_data["location"]}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_cupids(request):
    """
    A manager can get all the cupid profiles.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the cupid profiles were retrieved successfully, return the serialized cupids and a 200 status code.
            If the cupid profiles were not retrieved successfully, return an error message and a 400 status code.
    """
    cupids = Cupid.objects.all()
    serializer = CupidSerializer(data=cupids, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_daters(request):
    """
    A manager can get all the dater profiles.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the dater profiles were retrieved successfully, return the serialized daters and a 200 status code.
            If the dater profiles were not retrieved successfully, return an error message and a 400 status code.
    """
    daters = Dater.objects.all()
    serializer = DaterSerializer(data=daters, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_dater_count(request):
    """
    A manager can get the number of total daters.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of daters that are currently active was retrieved successfully, return the number of daters and a 200 status code.
            If the number of daters that are currently active was not retrieved successfully, return an error message and a 400 status code.
    """
    number_of_daters = Dater.objects.all().count()
    return Response({'count': number_of_daters}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_count(request):
    """
    A manager can get the number of total cupids.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of cupids that are currently active was retrieved successfully, return the cupid count and a 200 status code.
            If the number of cupids that are currently active was not retrieved successfully, return an error message and a 400 status code.
    """
    number_of_cupids = Cupid.objects.all().count()
    return Response({'count': number_of_cupids}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_cupids(request):
    """
    A manager can get the number of active cupids.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of active cupids was retrieved successfully, return the number of active cupids and a 200 status code.
            If the number of active cupids was not retrieved successfully, return an error message and a 400 status code.
    """
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    number_cupid_sessions = 0
    for session in active_sessions:
        session_data = session.get_decoded()
        user_id = session_data.get('_auth_user_id')
        if User.objects.get(id=user_id).role == 'Cupid':
            number_cupid_sessions += 1

    return Response({'active_cupid_sessions': number_cupid_sessions}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_daters(request):
    """
    A manager can get the number of active daters.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of active daters was retrieved successfully, return the number of active daters and a 200 status code.
            If the number of active daters was not retrieved successfully, return an error message and a 400 status code.
    """
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    number_dater_sessions = 0
    for session in active_sessions:
        session_data = session.get_decoded()
        user_id = session_data.get('_auth_user_id')
        if User.objects.get(id=user_id).role == 'Dater':
            number_dater_sessions += 1

    return Response({'active_dater_sessions': number_dater_sessions}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_rate(request):
    """
    A manager can get the rate of gigs per hour.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the rate of gigs per hour was retrieved successfully, return the gig rate and a 200 status code.
            If the rate of gigs per hour was not retrieved successfully, return an error message and a 400 status code.
    """
    try:
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        gigs_from_past_day = Gig.objects.filter(date_time_of_request_range=(yesterday, datetime.datetime.now()))
        gig_rate = gigs_from_past_day.count() / 24
        response = gig_rate.json()
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_gig_count(request):
    """
    A manager can get the number of gigs that are currently active.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of gigs that are currently active was retrieved successfully, return the gig count and a 200 status code.
            If the number of gigs that are currently active was not retrieved successfully, return an error message and a 400 status code.
    """
    number_of_gigs = Gig.objects.all().count()
    return Response({'count': number_of_gigs}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_drop_rate(request):
    """
    A manager can get the rate of gigs that are dropped.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the rate of gigs that are dropped was retrieved successfully, return the gig drop rate and a 200 status code.
            If the rate of gigs that are dropped was not retrieved successfully, return an error message and a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_complete_rate(request):
    """
    A manager can get the rate of gigs that are completed.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the rate of gigs that are completed was retrieved successfully, return the gig complete rate and a 200 status code.
            If the rate of gigs that are completed was not retrieved successfully, return an error message and a 400 status code.
    """
    try:
        number_of_completed_gigs = Gig.objects.filter(status=2).count()
        number_of_gigs = Gig.objects.all().count()

        gig_complete_rate = number_of_completed_gigs / number_of_gigs

        response = gig_complete_rate.json()

        return Response(response, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def suspend(request):
    """
    Manager can suspend a user.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                user_id (int): The id of the user to suspend.
    Returns:
        Response:
            If the user was suspended successfully, return a 200 status code.
            If the user was not suspended successfully, return an error message and a 400 status code.
    """
    user_data = request.post
    if user_data['user_type'] == 'Dater':
        serializer = DaterSerializer(data=user_data)
    elif user_data['user_type'] == 'Cupid':
        serializer = CupidSerializer(data=user_data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.validated_data['is_suspended'] = True
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def unsuspend(request):
    """
    Manager can unsuspend a user.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                user_id (int): The id of the user to unsuspend.
    Returns:
        Response:
            If the user was unsuspended successfully, return a 200 status code.
            If the user was not unsuspended successfully, return an error message and a 400 status code.
    """
    user_data = request.post
    if user_data['user_type'] == 'Dater':
        serializer = DaterSerializer(data=user_data)
    elif user_data['user_type'] == 'Cupid':
        serializer = CupidSerializer(data=user_data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.validated_data['is_suspended'] = False
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def speech_to_text(request):
    """
    For a Dater.
    Convert an audio file to text. When the audio is converted to text, the text is sent to the external AI service.
    The response from the AI service is analyzed and a gig could be created based on the response.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                dater_id (int): The id of the dater who is requesting
                audio (json): The audio to convert to text.
                    audio['type'] (str): The type of audio file.
                    audio['data'] (str): The audio file in base64 format.
    Returns:
        Response:
            If the audio was converted to text successfully and indicate if a gig was created or not, return a 200 status code.
            If the audio was not converted to text successfully or a gig could not be created, return an error message and a 400 status code.
    """
    data = request.data
    dater = get_object_or_404(Dater, id=data['user_id'])
    audio = data['audio']
    audio_type = audio['type']
    audio_data = audio['data']
    recognizer = speech_recognition.Recognizer()
    try:
        # Convert base64 audio data to bytes
        audio_bytes = base64.b64decode(audio_data)
        # Convert bytes to audio file
        with open("audio_file." + audio_type, "wb") as f:
            f.write(audio_bytes)
        # Transcribe audio
        with speech_recognition.AudioFile("audio_file." + audio_type) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_sphinx(audio_data)
        prompt = f"""
                  The following text is transcribed from an audio file. 
                  Analyze the text to determine if a gig should be created. 
                  A gig can be created by saying 'create gig'. 
                  The purpose of a gig is to tell a Cupid what to do to save the date. 
                  If a gig is created, the Cupid will be able to see the gig and accept it. 
                  A gig will need to know what items are requested for the date. 
                  The budget for the gig will be the amount of money the Dater is willing to spend on the date.
                  Budget: {dater.budget}
                  Please give your response in the following form:
                      Create gig: True or False
                      Items requested: Flowers, Chocolate, etc. or NA if no items are requested
                  The text is: 
                  
                  """
        message = prompt + text
        response = __get_ai_response(message)
        if contains("Create gig: True", response):
            requested_items = "NA"
            for line in response.split("\n"):
                if contains("Items requested:", line):
                    requested_items = line.split(":")[1].strip()
            if requested_items == "NA":
                return Response({"error": "gig creation failed. no specified pickup items", "gig_created": False}, status=status.HTTP_200_OK)
            locations = __call_yelp_api(dater.location, requested_items)
            quest_data = {
                "budget": dater.budget,
                "items_requested": requested_items,
                "pickup_location": locations[0]["address"]
            }
            serializer = QuestSerializer(data=quest_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({"error": "gig creation failed. could not serialize quest."}, status=status.HTTP_400_BAD_REQUEST)
            gig_data = {
                "dater": dater,
                "quest": serializer.data
            }
            serializer = GigSerializer(data=gig_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "gig was created", "gig_created": True}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "gig creation failed. could not serialize."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "gig creation not needed", "gig_created": False}, status=status.HTTP_200_OK)
    except speech_recognition.UnknownValueError:
        return Response({"error": "Could not understand the audio."}, status=status.HTTP_400_BAD_REQUEST)
    except speech_recognition.RequestError as e:
        return Response({"error": "Could not request results; {0}".format(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def notify(request):
    """
    Notify a user (any type) of something via a text or email depending on their communication preference.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                user_id (int): The id of the user to notify.
                message (str): The message to send to the user.
    Returns:
        Response:
            If the message was sent successfully, return a 200 status code.
            If the message was not sent successfully, return an error message and a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)
