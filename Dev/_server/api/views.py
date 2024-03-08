import base64
from operator import contains
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .serializers import UserSerializer, DaterSerializer, CupidSerializer, ManagerSerializer, MessageSerializer, \
    GigSerializer, \
    DateSerializer, FeedbackSerializer, PaymentCardSerializer, BankAccountSerializer, QuestSerializer
from .models import User, Dater, Cupid, Gig, Quest, Message, Date, Feedback, PaymentCard, BankAccount
from django.contrib.sessions.models import Session
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.utils.timezone import make_aware
from django.shortcuts import get_object_or_404
from geopy.geocoders import Nominatim
import geoip2.database
from math import radians, sin, cos, sqrt, atan2
from yelpapi import YelpAPI
from datetime import datetime
import speech_recognition
from transformers import GPT2Tokenizer, GPT2LMHeadModel


# 3. agree on how the serializers should be used and write the code to use them
# 4. agree on what external APIs we will use
# 5. write the code for the views
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
               role (str): Dater, Cupid, Manager
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
    # Prepare data input
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    data['role'] = data['role'].lower()
    # Create user
    userSerializer = UserSerializer(data=data)
    if userSerializer.is_valid():
        userSerializer.save()
        data['user'] = userSerializer.data['id']
    else:
        return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Create dater or cupid as appropriate
    if data['role'] == User.Role.DATER:
        serializer = DaterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(id=userSerializer.data['id'])
            login(request, user)

            return_data = user_expand(user, serializer)
            return Response(return_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif data['role'] == User.Role.CUPID:
        serializer = CupidSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(id=userSerializer.data['id'])
            login(request, user)

            return_data = user_expand(user, serializer)
            return Response(return_data, status=status.HTTP_201_CREATED)
        User.objects.get(id=data['user']).delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif data['role'] == User.Role.MANAGER:
        return Response(userSerializer.data, status=status.HTTP_201_CREATED)
    else:
        User.objects.get(id=data['user']).delete()
        return Response({"error": "invalid user type"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sign_in(request):
    """
    Log in a user

    Args (request.post):
        email(str): The email of the user 
        password(str): The password of the user

    Returns:
        Response:
            Dater, Cupid, or Manager serialized
    """
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    username = User.objects.get(email=data['email']).username
    user = authenticate(request, username=username, password=data['password'])
    if user is not None:
        login(request, user)
        if user.role == User.Role.DATER:
            dater = Dater.objects.get(user=user)
            serializer = DaterSerializer(dater)
        elif user.role == User.Role.CUPID:
            cupid = Cupid.objects.get(user=user)
            serializer = CupidSerializer(cupid)
        elif user.role == User.Role.MANAGER:
            serializer = ManagerSerializer(user)

        return_data = user_expand(user, serializer)
        return Response(return_data, status=status.HTTP_200_OK)
    else:
        if User.objects.filter(email=data['email']):
            reason = 'Incorrect password'
        else:
            reason = 'User not found'
        return Response({'Reason': reason}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request, pk):
    """
    Get a user's information

    Args (URL query string):
        pk(int): The id of the user
    Returns:
        Response:
            Dater, Cupid, or Manager serialized
    """
    if pk != request.user.id and request.user.is_staff is False:
        return Response(status=status.HTTP_403_FORBIDDEN)

    data = request.data
    user = get_object_or_404(User, id=pk)

    if user.role == User.Role.DATER:
        dater = Dater.objects.get(user=user)
        serializer = DaterSerializer(dater)
    elif user.role == User.Role.CUPID:
        cupid = Cupid.objects.get(user=user)
        serializer = CupidSerializer(cupid)
    elif user.role == User.Role.MANAGER:
        serializer = ManagerSerializer(user)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return_data = user_expand(user, serializer)
    return Response(return_data, status=status.HTTP_200_OK)


def user_expand(user, serializer):
    userSerializer = UserSerializer(user)
    return_data = serializer.data
    return_data['user'] = userSerializer.data
    del return_data['user']['password']
    return return_data


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    """
    For a manager.
    Delete a user

    Args:
        pk(int): The id of the user

    Returns:
        Response:
            OK
    """
    if pk != request.user.id and request.user.is_staff is False:
        return Response(status=status.HTTP_403_FORBIDDEN)
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def send_chat_message(request):
    """
    For a dater.
    Stores the given message in the database, sends it to the AI, and returns the AI's response.

    Args (request.post):
        message(str): The message

    Returns:
        Response:
            message(str): The AI's response
    """
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    user_id = request.user.id
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    user = get_object_or_404(User, id=pk)
    try:
        messages = Message.objects.filter(owner=user).order_by('-id')[:5]
    except Message.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def calendar(request, pk):
    """
    For a dater.
    Returns the dater's scheduled dates.

    GET
    Args:
        pk(int): the user_id as included in the URL
    Returns:
        Response:
            The user's saved dates

    POST
    Args (request.post):
        date_time(str): ISO 8601 timestamp (I fed output back into API, and GPT said that was the date format)
        location(str): Location of date
        description(str): Arbitrary description
        status(str): Date.Status (PLANNED, OCCURING, PAST, or CANCELED)
        budget(decimal): The max budget for the date
    Returns:
        Response:
            The saved date serialized
    """
    if request.method == 'GET':
        if pk != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        dater = get_object_or_404(Dater, user_id=pk)
        try:
            dates = Date.objects.filter(dater=dater)
        except Date.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = DateSerializer(dates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        # TODO: Either us or the frontend needs to determine a planned location, and then we save that, not an ip lookup
        data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
        data['dater'] = request.user.id
        serializer = DateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rate_dater(request):
    """
    For a cupid.
    Saves a rating of a dater to the database.

    Args (request.post):
        dater_id(int): The id of the dater
        gig_id(int): The id of the gig
        message(str): Message of feedback
        rating(int): 1-5 stars(hearts)
    Returns:
        Response:
            Saved Feedback serialized
    """
    data = request.data
    # TODO: This doesn't do much as is, should update user's location instead
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    owner = request.user.id
    target = data['dater_id']
    gig = data['gig_id']
    # TODO: Once dummy feedback has proper targets and owners, test that this portion actually works
    if Gig.objects.get(id=gig).dater.user_id != target:
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = FeedbackSerializer(
        data={'owner': owner, 'target': target, 'gig': gig, 'message': data['message'], 'star_rating': data['rating'], 'date_time': make_aware(datetime.now())})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    dater = get_object_or_404(Dater, user_id=pk)
    try:
        ratings = Feedback.objects.filter(target=dater.user)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = FeedbackSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    dater = get_object_or_404(Dater, user_id=pk)
    try:
        ratings = Feedback.objects.filter(target=dater.user)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # TODO: Database has field to store this instead of recalculating all
    total = 0
    for rating in ratings:
        total += rating.star_rating
    avg = total / len(ratings)
    return Response({'rating': avg}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def dater_transfer(request):
    """
    For a dater.
    Charges the dater's card and updates their balance.

    Args (request.post):
        card_id(int): The id of the card to charge
        amount(float): The amount to transfer
    Returns:
        Response:
            OK
    """
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    dater = get_object_or_404(Dater, user=request.user)
    card = get_object_or_404(PaymentCard, id=data['card_id'])
    if card.user != dater.user:
        return Response({"error: you don't have a card with that id"}, status=status.HTTP_403_FORBIDDEN)
    return Response({f'Card charged {data["amount"]}'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    dater = get_object_or_404(Dater, user_id=pk)
    return Response({'balance': dater.cupid_cash_balance}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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

    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    dater = get_object_or_404(Dater, user_id=pk)
    serializer = DaterSerializer(dater)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def set_dater_profile(request):
    """
    For a dater.
    Saves the profile data of a dater.

    Args (request.post):
        serialized dater
    Returns:
        Response:
            Saved dater serialized
    """
    data = request.data
    data['user'] = request.user.id
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    dater = get_object_or_404(Dater, user_id=request.user.id)
    serializer = DaterSerializer(dater, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rate_cupid(request):
    """
    For a dater.
    Saves a rating of a cupid to the database.

    Args (request.post):
        cupid_id(int): The id of the cupid
        gig_id(int): The id of the gig
        message(str): Message of feedback
        rating(int): 1-5 stars(hearts)
    Returns:
        Response:
            Saved Feedback serialized
    """
    data = request.data
    # TODO: This doesn't do much as is, should update user's location instead
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    owner = request.user.id
    target = data['cupid_id']
    gig = data['gig_id']
    if Gig.objects.get(id=gig).cupid.user_id != target:
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = FeedbackSerializer(
        data={'owner': owner, 'target': target, 'gig': gig, 'message': data['message'], 'star_rating': data['rating'], 'date_time': make_aware(datetime.now())})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    cupid = get_object_or_404(Cupid, user_id=pk)
    try:
        ratings = Feedback.objects.filter(user=cupid)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = FeedbackSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    cupid = get_object_or_404(Cupid, user_id=pk)
    try:
        ratings = Feedback.objects.filter(target=cupid.user)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # TODO: should not have to be calculated from scratch every time
    if len(ratings) == 0:
        return Response({'rating': 0}, status=status.HTTP_200_OK)
    total = 0
    for rating in ratings:
        total += rating.star_rating
    avg = total / len(ratings)
    return Response({'rating': avg}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def cupid_transfer(request):
    """
    Performs financial transfer from a Cupid's balance to their bank account.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
    Returns:
        Response:
            If the transfer went through successfully, return a 200 status code.
            If the transfer failed, return a corresponding error status code (400 if on our end, 500 if on bank's end)
    """
    data = request.data
    # TODO: This doesn't do much as is, should update the cupid's location instead.
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    cupid = get_object_or_404(Cupid, user_id=request.user.id)
    bank_account = get_object_or_404(BankAccount, user=cupid.user)
    return Response({f"Transfering {cupid.cupid_cash_balance} to {bank_account.routing_number}"},status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    cupid = get_object_or_404(Cupid, user_id=pk)
    return Response({'balance': cupid.cupid_cash_balance}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    cupid = get_object_or_404(Cupid, user_id=pk)
    serializer = CupidSerializer(cupid)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def set_cupid_profile(request):
    """
    Creates or changes data in a Cupid's profile.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                data (json): The data to create or change in the Cupid's profile.
    Returns:
        Response:
            If the profile was created or changed successfully, return a 200 status code.
            If the profile failed to be created or changed (insufficent permissions, bad data, or error), return a 400 status code.
    """
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    data['user'] = request.user.id
    cupid = get_object_or_404(Cupid, user_id=request.user.id)
    serializer = CupidSerializer(cupid, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_gig(request):
    """
    Creates a gig.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                quest (json): The quest that the gig is for.
                    quest['budget'] (float): The budget for the gig.
                    quest['items_requested'] (str): The items requested for the gig.
                    quest['pickup_location'] (str): The location to pick up the items for the gig.

    Returns:
        Response:
            If the gig was created correctly, return a 200 status code.
            If the gig was failed to be created, return a 400 status code.
    """
    data = request.data
    # TODO: This doesn't do much, should update the dater's location instead
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    dater = get_object_or_404(Dater, user_id=request.user.id)
    serializer = QuestSerializer(data=data['quest'])
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    quest = get_object_or_404(Quest, id=serializer.data['id'])
    serializer = GigSerializer(data={'dater': dater, 'quest': quest.id, 'status': Gig.Status.UNCLAIMED, 'dropped_count': 0, 'accepted_count': 0})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    gig = get_object_or_404(Gig, id=data['gig_id'])
    serializer = GigSerializer(gig, data={'is_accepted': True, 'cupid': request.user.id, 'accepted_count': gig.accepted_count + 1, 'date_time_of_claim': make_aware(datetime.now())}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    gig = get_object_or_404(Gig, id=data['gig_id'])
    serializer = GigSerializer(gig, data={'status': Gig.Status.COMPLETE, 'date_time_of_completion': make_aware(datetime.now())}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    data = request.data
    # This doesn't do much, should update the cupid's location instead
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    gig = get_object_or_404(Gig, id=data['gig_id'])
    if gig.cupid != request.user.cupid:
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = GigSerializer(gig, data={'is_accepted': False, 'status': Gig.Status.UNCLAIMED, 'cupid': None, 'dropped_count': gig.dropped_count + 1}, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    geoip_database_path = "api/geodata/GeoLite2-City_20240227/GeoLite2-City.mmdb"
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_stores(request, pk):
    """
    Reaches out to an API with an address to get stores near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby stores, including their specific location (JSON)
    """
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    response = __call_yelp_api(pk, "stores")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_activities(request, pk):
    """
    Reaches out to an API with an address to get possible activities near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby activities, including their specific location (JSON)
    """
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    response = __call_yelp_api(pk, "activities")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_events(request, pk):
    """
    Reaches out to an API with an address to get current entertainment events near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby events, including their specific location (JSON)
    """
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    response = __call_yelp_api(pk, "events")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    response = __call_yelp_api(pk, "attractions")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    response = __call_yelp_api(pk, "restaurants")
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def __call_yelp_api(pk, search):
    dater = get_object_or_404(Dater, user_id=pk)
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    user = get_object_or_404(User, id=pk)
    if user.role == User.Role.DATER:
        user_data = get_object_or_404(Dater, user_id=pk)
        serializer = DaterSerializer(data=user_data)
    elif user.role == User.Role.CUPID:
        user_data = get_object_or_404(Cupid, user_id=pk)
        serializer = CupidSerializer(data=user_data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response({'location': serializer.validated_data["location"]}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
        if User.objects.get(id=user_id).role == User.Role.CUPID:
            number_cupid_sessions += 1
    return Response({'active_cupid_sessions': number_cupid_sessions}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
        if User.objects.get(id=user_id).role == User.Role.DATER:
            number_dater_sessions += 1

    return Response({'active_dater_sessions': number_dater_sessions}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
        yesterday = datetime.now() - datetime.timedelta(days=1)
        gigs_from_past_day = Gig.objects.filter(date_time_of_request_range=(yesterday, datetime.now()))
        gig_rate = gigs_from_past_day.count() / 24
        response = gig_rate.json()
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
    try:
        number_of_drops = 0
        yesterday = datetime.now() - datetime.timedelta(days=1)
        gigs_from_past_day = Gig.objects.filter(date_time_of_request_range=(yesterday, datetime.now()))
        for gig in gigs_from_past_day:
            number_of_drops += gig.dropped_count

        drop_rate = number_of_drops / 24
        response = drop_rate.json()
        return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
    user_data = request.data
    if user_data['role'] == 'Dater':
        serializer = DaterSerializer(data=user_data)
    elif user_data['role'] == 'Cupid':
        serializer = CupidSerializer(data=user_data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.validated_data['is_suspended'] = True
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
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
    user_data = request.data
    if user_data['role'] == 'Dater':
        serializer = DaterSerializer(data=user_data)
    elif user_data['role'] == 'Cupid':
        serializer = CupidSerializer(data=user_data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.validated_data['is_suspended'] = False
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def speech_to_text(request):
    """
    For a Dater.
    Convert an audio file to text. When the audio is converted to text, the text is sent to the external AI service.
    The response from the AI service is analyzed and a gig could be created based on the response.

    Args:
        request: Information about the request.
            request.post: The json data sent to the server.
                audio (json): The audio to convert to text.
                    audio['type'] (str): The type of audio file.
                    audio['data'] (str): The audio file in base64 format.
    Returns:
        Response:
            If the audio was converted to text successfully and indicate if a gig was created or not, return a 200 status code.
            If the audio was not converted to text successfully or a gig could not be created, return an error message and a 400 status code.
    """
    data = request.data
    data['location'] = __get_location_string(request.META['REMOTE_ADDR'])
    dater = get_object_or_404(Dater, user_id=request.user.id)
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
                return Response({"error": "gig creation failed. no specified pickup items", "gig_created": False},
                                status=status.HTTP_200_OK)
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
                return Response({"error": "gig creation failed. could not serialize quest."},
                                status=status.HTTP_400_BAD_REQUEST)
            gig_data = {
                "dater": dater,
                "quest": serializer.data
            }
            serializer = GigSerializer(data=gig_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "gig was created", "gig_created": True}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "gig creation failed. could not serialize."},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "gig creation not needed", "gig_created": False}, status=status.HTTP_200_OK)
    except speech_recognition.UnknownValueError:
        return Response({"error": "Could not understand the audio."}, status=status.HTTP_400_BAD_REQUEST)
    except speech_recognition.RequestError as e:
        return Response({"error": "Could not request results; {0}".format(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
    data = request.data
    dater = get_object_or_404(Dater, user_id=data['user_id'])
    account_sid = 'AC9b5808bbd03ee994e26fc36e9a59aeef'
    auth_token = '584fb19de19ec92bacf218df367efb4c'
    message = data['message']
    if dater.communication_preference == 0:
        dater_email = dater.email
        mail = Mail(
            from_email='throhawy@gmail.com',
            to_emails=dater_email,
            subject='Notification from Cupid Code',
            html_content=message
        )
        try:
            sg = SendGridAPIClient('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')
            response = sg.send(mail)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_200_OK)
    elif dater.communication_preference == 1:
        # We are hard-coding the number since only verified numbers can be used
        dater_phone_number = '+18017083373'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+18446234068',
            body=message,
            to=dater_phone_number
        )
        return Response(message.sid, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
