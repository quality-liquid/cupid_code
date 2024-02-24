from rest_framework import serializers
from .models import Dater, Cupid, Message, Quest, Gig, Date, Feedback, PaymentCard, BankAccount


# TODO make better serializers
class DaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dater
        fields = ['budget', 'average_rating', 'is_suspended']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Password and password confirmation do not match')
        return data

    def create(self, validated_data):
        dater = Dater(**validated_data)
        dater.is_suspended = False
        dater.save()
        return dater


class CupidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupid
        fields = ['']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['']


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['']


class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = ['']


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['']


class PaymentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCard
        fields = ['']


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['']
