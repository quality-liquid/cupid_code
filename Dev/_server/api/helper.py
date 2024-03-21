from math import radians, sin, cos, sqrt, atan2

from geopy.geocoders import Nominatim
import geoip2.database
from yelpapi import YelpAPI
from transformers import GPT2Tokenizer, GPT2LMHeadModel

from .models import User, Dater
from django.contrib.auth import login


def save_profile(data, request, user_serializer, serializer):
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(id=user_serializer.data['id'])
        login(request, user)

        return_data = user_expand(user, serializer)
        return Response(return_data, status=status.HTTP_201_CREATED)
    User.objects.get(id=data['user']).delete()
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


def get_location_string(ip_address):
    latitude, longitude = get_location_from_ip_address(ip_address)
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
        return file.read().split(" ")[-1]


def update_user_location(user, addr):
    user.location = get_location_string(addr)
    user.save()
