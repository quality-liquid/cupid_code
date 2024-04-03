# Standard Library
from math import radians, sin, cos, sqrt, atan2
import base64

# Django
from django.contrib.auth import login
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, get_list_or_404

# Rest Framework
from rest_framework.response import Response
from rest_framework import status

# Miscellaneous Utils
from geopy.geocoders import Nominatim
import geoip2.database
from yelpapi import YelpAPI
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from operator import contains
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
import speech_recognition

# Local
from .models import User, Dater, Cupid, Date
from .serializers import UserSerializer, DaterSerializer, CupidSerializer, QuestSerializer, GigSerializer, \
    DateSerializer


def initialize_serializer(user):
    if user.role == User.Role.DATER:
        dater = Dater.objects.get(user=user)
        return DaterSerializer(dater)
    elif user.role == User.Role.CUPID:
        cupid = Cupid.objects.get(user=user)
        return CupidSerializer(cupid)


def authenticated_dater(pk, user):
    if pk != user.id:
        raise PermissionDenied()
    return get_object_or_404(Dater, user_id=pk)


def authenticated_cupid(pk, user):
    if pk != user.id:
        raise PermissionDenied()
    return get_object_or_404(Cupid, user_id=pk)


def save_profile(request, user, serializer):
    if serializer.is_valid():
        serializer.save()
        login(request, user)

        return_data = user_expand(user, serializer)
        return Response(return_data, status=status.HTTP_201_CREATED)
    user.delete()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_expand(user, other_serializer):
    try:
        return_data = other_serializer.data
        if user.role == User.Role.MANAGER:
            return_data['user'] = other_serializer.data
        else:
            user_serializer = UserSerializer(user)
            return_data['user'] = user_serializer.data
        del return_data['user']['password']
        return return_data
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def retrieved_response(serializer):
    """
    This method is to make validating information is retrieved correctly and return a 200.
    Returns 400 if it failed.
    """
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def save_serializer(serializer):
    """
    This method is to make validating information is changed and saved correctly, and it returns a 201.
    Returns 400 if it failed.
    """
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_ai_response(message: str):
    """
    Send the message to the AI and return the response.
    https://pytensor.readthedocs.io/en/latest/
    https://huggingface.co/
    """
    try:
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("gpt2")
        # Tokenize input text
        input_ids = tokenizer.encode(message, return_tensors='pt')
        # Generate response
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)
        # Decode and return response
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response
    except Exception as e:
        return str(e)


def save_calendar(request):
    try:
        data = request.data
        # TODO: Either us or the frontend needs to determine a planned location, then save the geo coords
        data['location'] = get_location_string(request.META['REMOTE_ADDR'])
        data['dater'] = request.user.id
        serializer = DateSerializer(data=data)
        return save_serializer(serializer)
    except Dater.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def get_calendar(pk, request):
    try:
        dater = authenticated_dater(pk, request.user)
        dates = get_list_or_404(Date, dater=dater)
        serializer = DateSerializer(dates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Dater.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def update_user_location(user, addr):
    user.location = get_location_string(addr)
    if user.location is not None:
        user.save()


def get_location_string(ip_address):
    if ip_address is None:
        return None
    if ip_address == "127.0.0.1" or ip_address == "localhost":
        return "430909.36611535 4621007.2874155"
    latitude, longitude = get_location_from_ip_address(ip_address)
    if latitude is None or longitude is None:
        return None
    return f"{latitude} {longitude}"


def get_location_from_address(address):
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


def get_location_from_ip_address(ip_address):
    """
    Returns the location of an IP address.
    """
    if ip_address is None:
        return None
    if ip_address == "127.0.0.1" or ip_address == "localhost":
        return "430909.36611535 4621007.2874155"
    geoip_database_path = "api/geodata/GeoLite2-City_20240227/GeoLite2-City.mmdb"
    with geoip2.database.Reader(geoip_database_path) as reader:
        try:
            response = reader.city(ip_address)
            latitude = response.location.latitude
            longitude = response.location.longitude
            return latitude, longitude
        except geoip2.errors.AddressNotFoundError:
            return None, None


def locations_are_near(location1, location2, max_distance_miles):
    """
    Returns whether two locations are near each other.
    """
    latitude1, longitude1 = location1.split(" ")
    latitude1 = latitude1.strip(',')
    latitude2, longitude2 = location2.split(" ")
    latitude2 = latitude2.strip(',')
    # TODO: Expand quest or give frontend an api for getting quests.
    return within_distance(
        float(latitude1), float(longitude1), float(latitude2), float(longitude2), float(max_distance_miles)
    )


def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in miles
    r = 3958.8  # miles

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = r * c

    return distance


def within_distance(lat1, lon1, lat2, lon2, max_distance_miles):
    distance = haversine_distance(lat1, lon1, lat2, lon2)
    return distance <= max_distance_miles


def call_yelp_api(pk, search):
    dater = get_object_or_404(Dater, user_id=pk)
    latitude, longitude = dater.location.split(" ")
    api_key = get_yelp_api_key()
    with YelpAPI(api_key, timeout_s=5.0) as yelp_api:
        try:
            return yelp_api.search_query(term=search, latitude=latitude, longitude=longitude, limit=10)
        except YelpAPI.YelpAPIError as e:
            return None


def get_yelp_api_key():
    """
    Returns the Yelp API key.
    """
    with open('yelp_api_key.txt', 'r') as file:
        lines = file.readlines()
        return lines[0].split(" ")[2].strip()


def get_twilio_account_sid():
    """
    Returns the Twilio account SID.
    """
    with open('yelp_api_key.txt', 'r') as file:
        lines = file.readlines()
        return lines[1].split(" ")[2].strip()


def get_twilio_auth_token():
    """
    Returns the Twilio authentication token.
    """
    with open('yelp_api_key.txt', 'r') as file:
        lines = file.readlines()
        return lines[1].split(" ")[4].strip()


def get_twilio_authenticated_sender_email():
    """
    Returns the Twilio authenticated sender email.
    """
    with open('yelp_api_key.txt', 'r') as file:
        lines = file.readlines()
        return lines[5].split(" ")[1].strip()


def get_grid_api_key():
    """
    Returns the Grid API key.
    """
    with open('yelp_api_key.txt', 'r') as file:
        lines = file.readlines()
        return lines[2].split(" ")[2].strip()


def get_twilio_authenticated_reserve_phone_number():
    """
    Returns the Twilio authenticated reserve phone number.
    """
    with open('yelp_api_key.txt', 'r') as file:
        lines = file.readlines()
        return lines[4].split(" ")[1].strip()


def get_twilio_authenticated_sender_phone_number():
    """
    Returns the Twilio authenticated sender phone number.
    """
    with open('yelp_api_key.txt', 'r') as file:
        lines = file.readlines()
        return lines[5].split(" ")[1].strip()


def process_ai_response(dater, response):
    if contains('Create gig: True', response):
        return create_new_gig(dater, response)
    else:
        return Response(
            {'message': 'gig creation not needed', 'gig_created': False},
            status=status.HTTP_200_OK,
        )


def create_new_gig(dater, response):
    requested_items = 'NA'
    for line in response.split('\n'):
        if contains('Items requested:', line):
            requested_items = line.split(':')[1].strip()
    if requested_items == 'NA':
        return Response(
            {
                'error': 'gig creation failed. no specified pickup items',
                'gig_created': False,
            },
            status=status.HTTP_200_OK,
        )
    locations = call_yelp_api(dater.location, requested_items)
    quest_data = {
        'budget': dater.budget,
        'items_requested': requested_items,
        'pickup_location': locations[0]['address'],
    }
    serializer = QuestSerializer(data=quest_data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(
            {'error': 'gig creation failed. could not serialize quest.'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    gig_data = {'dater': dater, 'quest': serializer.data}
    serializer = GigSerializer(data=gig_data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'gig was created', 'gig_created': True},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {'error': 'gig creation failed. could not serialize.'},
            status=status.HTTP_400_BAD_REQUEST,
        )


def send_text(account_sid, auth_token, message):
    # We are hard-coding the number since only verified numbers can be used
    to_phone_number = get_twilio_authenticated_reserve_phone_number()
    from_phone_number = get_twilio_authenticated_sender_phone_number()
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_phone_number,
        body=message,
        to=to_phone_number
    )
    return Response(message.sid, status=status.HTTP_200_OK)


def send_email(dater, message):
    dater_email = dater.email
    from_email = get_twilio_authenticated_sender_email()
    mail = Mail(
        from_email=from_email,
        to_emails=dater_email,
        subject='Notification from Cupid Code',
        html_content=message,
    )
    try:
        grid_api_key = get_grid_api_key()
        sg = SendGridAPIClient(grid_api_key)
        response = sg.send(mail)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
    return Response(response, status=status.HTTP_200_OK)


def get_response_from_audio(audio_data, audio_type, dater):
    recognizer = speech_recognition.Recognizer()
    # Convert base64 audio data to bytes
    audio_bytes = base64.b64decode(audio_data)
    # Convert bytes to audio file
    with open('audio_file.' + audio_type, 'wb') as f:
        f.write(audio_bytes)
    # Transcribe audio
    with speech_recognition.AudioFile('audio_file.' + audio_type) as source:
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
    response = get_ai_response(message)
    return response


def get_response_from_yelp_api(pk, request, search):
    if pk != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    response = call_yelp_api(pk, search)
    if response:
        return Response(response, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def get_sessions(role):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    if active_sessions is None:
        return Response({'error': 'No active sessions'}, status=status.HTTP_400_BAD_REQUEST)
    number_dater_sessions = 0
    for session in active_sessions:
        session_data = session.get_decoded()
        user_id = session_data.get('_auth_user_id')
        if User.objects.get(id=user_id).role == role:
            number_dater_sessions += 1
    return Response({'active_sessions': number_dater_sessions}, status=status.HTTP_200_OK)
