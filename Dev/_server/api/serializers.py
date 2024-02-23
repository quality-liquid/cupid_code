from rest_framework import serializers
from .models import Dater, Cupid, Message, Quest, Gig, Date, Feedback, PaymentCard, BankAccount


# TODO make better serializers
class DaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dater
        fields = '__all__'


class CupidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupid
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = '__all__'


class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = '__all__'


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class PaymentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCard
        fields = '__all__'


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
