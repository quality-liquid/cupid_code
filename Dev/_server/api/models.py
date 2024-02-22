from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        DATER = 'Dater'
        CUPID = 'Cupid'
        MANAGER = 'Manager'

    role = models.CharField(choices=Role.choices, max_length=7)

class Dater(models.Model):
    class Communication(models.IntegerChoices):
        EMAIL = 0
        TEXT = 1

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.role = User.Role.DATER
        self.user.save()

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    communication_preference = models.IntegerField(choices = Communication.choices)
    description = models.TextField()
    dating_strengths = models.TextField()
    dating_weaknesses = models.TextField()
    interests = models.TextField()
    past = models.TextField()
    nerd_type = models.TextField()
    relationship_goals = models.TextField()
    ai_degree = models.TextField()
    cupid_cash_balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField()
    average_rating = models.DecimalField(max_digits=10, decimal_places=2)
    suspended = models.BooleanField()
    #TODO: ImageField cannot be used without Pillow. We will have to add that to poetry before
    # implementing profile_picture.
    #profile_picture = models.ImageField()



class Cupid(models.Model):
    class Status(models.IntegerChoices):
        OFFLINE = 0
        GIGGING = 1
        AVAILABLE = 2

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    accepting_gigs = models.BooleanField()
    gigs_completed = models.IntegerField()
    gigs_failed = models.IntegerField()
    status = models.IntegerField(choices=Status.choices)
    cupid_cash_balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField()
    average_rating = models.DecimalField(max_digits=10, decimal_places=2)
    
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    from_ai = models.BooleanField()

class Quest(models.Model):
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    items_requested = models.TextField()
    pickup_location = models.TextField()

class Gig(models.Model):
    class Status(models.IntegerChoices):
        UNCLAIMED = 0
        CLAIMED = 1
        COMPLETE = 2
        DROPPED = 3

    dater = models.ForeignKey(Dater, on_delete=models.CASCADE)
    cupid = models.ForeignKey(Cupid, on_delete=models.CASCADE, null=True)
    quest = models.OneToOneField('Quest', on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices)
    date_time_of_request = models.DateTimeField()
    date_time_of_claim = models.DateTimeField(null=True)
    date_time_of_completion = models.DateTimeField(null=True)

class Date(models.Model):
    class Status(models.TextChoices):
        PLANNED = 'planned'
        OCCURING = 'occuring'
        PAST = 'past'
        CANCELED = 'canceled'

    dater = models.ForeignKey(Dater, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.TextField()
    description = models.TextField()
    status = models.TextField(choices = Status.choices)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    message = models.TextField()
    star_rating = models.IntegerField()
    date_time = models.DateTimeField()
    
class PaymentCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.TextField()
    cvv = models.TextField()
    expiration = models.TextField()

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routing_number = models.TextField()
    account_number = models.TextField()

