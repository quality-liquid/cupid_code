# Standard Library
from math import radians, sin, cos, sqrt, atan2

# Django
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

# Rest Framework
from rest_framework.response import Response
from rest_framework import status

# Miscellaneous Utils
from geopy.geocoders import Nominatim
import geoip2.database
from yelpapi import YelpAPI
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Local
from .models import User, Dater, Cupid
from .serializers import UserSerializer, DaterSerializer, CupidSerializer


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


def user_expand(user, serializer):
    userSerializer = UserSerializer(user)
    return_data = serializer.data
    return_data['user'] = userSerializer.data
    del return_data['user']['password']
    return return_data


def retrieved_response(serializer):
    """
    This method is to make validating information is retrieved correctly and return a 200.
    Returns 400 if it failed.
    """
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def changed_response(serializer):
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
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    # Tokenize input text
    input_ids = tokenizer.encode(message, return_tensors='pt')
    # Generate response
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)
    # Decode and return response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


def update_user_location(user, addr):
    user.location = get_location_string(addr)
    if user.location is not None:
        user.save()


def get_location_string(ip_address):
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
