from rest_framework import serializers
from .models import Dater, Cupid, User, Message, Gig, Quest, Date, Feedback, PaymentCard, BankAccount


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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CupidSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        return data

    def create(self, validated_data):
        cupid = Cupid(**validated_data)
        cupid.is_suspended = False
        cupid.save()
        return cupid


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = '__all__'


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
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
