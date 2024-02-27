from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DaterSerializer, CupidSerializer, MessageSerializer, GigSerializer, DateSerializer, FeedbackSerializer, PaymentCardSerializer, BankAccountSerializer
from .models import User, Dater, Cupid, Gig
from django.contrib.sessions.models import Session
from django.utils import timezone

# 1. write the code for the models
# 2. write doc strings for all the views so we know what they should take in, what they should do, and what they should return
# 3. agree on how the serializers should be used and write the code to use them
# 4. agree on what external APIs we will use
# TODO 5. write the code for the views
# TODO 6. write the tests for the views
# TODO 7. debug

# AI API (Microsoft Copilot) (openai) https://platform.openai.com/docs/quickstart?context=python
# Location API (Geolocation) https://pypi.org/project/geolocation-python/
# Speech To Text API (pyttsx3) https://pypi.org/project/pyttsx3/
# Text and Email notifications API (Twilio) https://www.twilio.com/en-us
# Nearby Shops API (yelpapi) https://pypi.org/project/yelpapi/

# Nate S start

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
    user_data = request.post
    if user_data['user_type'] == 'Dater':
        serializer = DaterSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif user_data['user_type'] == 'Cupid':
        serializer = CupidSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)

# Nate S end

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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


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
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_stores(request):
    """
    Reaches out to an API with an address to get stores near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby stores, including their specific location (JSON)
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_activities(request):
    """
    Reaches out to an API with an address to get possible activities near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby activities, including their specific location (JSON)
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_events(request):
    """
    Reaches out to an API with an address to get current entertainment events near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            A list of nearby events, including their specific location (JSON)
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_attractions(request):
    """
    Reaches out to an API with an address to get attractions near that address location.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the attractions were retrieved successfully, return a list of nearby attractions, including their specific location amd a 200 status code.
            If the attractions were not retrieved successfully, return an error message and a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)

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
    user = User.objects.get(id=pk)
    if user.role == 'Dater':
        user_data = Dater.objects.get(id=pk)
        serializer = DaterSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'location': serializer.validated_data["location"]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif user.role == 'Cupid':
        user_data = Cupid.objects.get(id=pk)
        serializer = CupidSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'location': serializer.validated_data["location"]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

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

    return Response({'cupids': cupids}, status=status.HTTP_200_OK)
    


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

    return Response({'daters': daters}, status=status.HTTP_200_OK)


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
    daters = Dater.objects.all()

    return Response({'count': len(daters)}, status=status.HTTP_200_OK)


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
    cupids = Cupid.objects.all()

    return Response({'count': len(cupids)}, status=status.HTTP_200_OK)


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
    
    return Response(status=status.HTTP_200_OK)


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
    gigs = Gig.objects.all()

    return Response({'count': len(gigs)}, status=status.HTTP_200_OK)



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
    return Response(status=status.HTTP_200_OK)


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
        if serializer.is_valid():
            serializer.validated_data['is_suspended'] = True
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif user_data['user_type'] == 'Cupid':
        serializer = CupidSerializer(data=user_data)
        if serializer.is_valid():
            serializer.validated_data['is_suspended'] = True
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
        if serializer.is_valid():
            serializer.validated_data['is_suspended'] = False
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif user_data['user_type'] == 'Cupid':
        serializer = CupidSerializer(data=user_data)
        if serializer.is_valid():
            serializer.validated_data['is_suspended'] = False
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
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
    return Response(status=status.HTTP_200_OK)


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
