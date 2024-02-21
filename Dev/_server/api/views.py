from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def create_user(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def send_chat_message(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_five_messages(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def calendar(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def rate_dater(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_ratings(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_avg_rating(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def dater_transfer(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_balance(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_profile(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def set_dater_profile(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def rate_cupid(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_ratings(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_avg_rating(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def cupid_transfer(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_balance(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_profile(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def set_cupid_profile(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def create_gig(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def accept_gig(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def complete_gig(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def drop_gig(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gigs(request, count):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_stores(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_activities(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_events(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_attractions(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_location(request, pk):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupids(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_daters(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_count(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_count(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_cupids(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_daters(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_rate(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_count(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_drop_rate(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_complete_rate(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def suspend(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def unsuspend(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def speech_to_text(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def notify(request):
    return Response(status=status.HTTP_200_OK)
