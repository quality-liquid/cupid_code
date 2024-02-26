from rest_framework import serializers
from .models import Dater, Cupid, Message, Gig, Date, Feedback, PaymentCard, BankAccount


class DaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dater
        fields = ['budget', 'average_rating', 'is_suspended']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            return serializers.ValidationError('Password and password confirmation do not match')
        return data

    def create(self, validated_data):
        dater = Dater(**validated_data)
        dater.is_suspended = False
        dater.save()
        return dater

    def update(self, instance, validated_data):
        instance.budget = validated_data.get('budget', instance.budget)
        instance.average_rating = validated_data.get('average_rating', instance.average_rating)
        instance.is_suspended = validated_data.get('is_suspended', instance.is_suspended)
        instance.save()
        return instance


class CupidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupid
        fields = ['status', 'average_rating', 'cupids_cash_balance']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            return serializers.ValidationError('Password and password confirmation do not match')
        return data

    def create(self, validated_data):
        cupid = Cupid(**validated_data)
        cupid.is_suspended = False
        cupid.save()
        return cupid

    def update(self, instance, validated_data):
        instance.accepting_gigs = validated_data.get('accepting_gigs', instance.accepting_gigs)
        instance.gigs_completed = validated_data.get('gigs_completed', instance.gigs_completed)
        instance.gigs_failed = validated_data.get('gigs_failed', instance.gigs_failed)
        instance.status = validated_data.get('status', instance.status)
        instance.average_rating = validated_data.get('average_rating', instance.average_rating)
        instance.is_suspended = validated_data.get('is_suspended', instance.is_suspended)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance


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
