from rest_framework import serializers
from .models import Dater, Cupid, Message, Gig, Date, Feedback, PaymentCard, BankAccount


class DaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dater
        fields = '__all__'

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            return serializers.ValidationError('Password and password confirmation do not match')
        return data

    def create(self, validated_data):
        dater = Dater(**validated_data)
        dater.is_suspended = False
        dater.save()
        return dater


class CupidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupid
        fields = '__all__'

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            return serializers.ValidationError('Password and password confirmation do not match')
        return data

    def create(self, validated_data):
        cupid = Cupid(**validated_data)
        cupid.is_suspended = False
        cupid.save()
        return cupid


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
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
        fields = ['card_number']


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['account_number']
