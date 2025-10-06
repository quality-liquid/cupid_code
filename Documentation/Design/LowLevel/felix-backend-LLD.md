## Backend Design

### URL Mapping

#### Static endpoints

The static endpoints do not require user data.

| URL      | Method    | View Function | Notes                                                                                          |
|----------|-----------|---------------|------------------------------------------------------------------------------------------------|
| / | GET | home | The home page |
| /login/ | GET, POST | login | The login page, post the form |
| /signup/ | GET, POST | signup | The signup page, post the form |
| /app/ | GET | NA | This can only be called after a user is authenticated. The Vue Router will take over from here.
| /get_*/ | GET | get_* | This will get icon images for the front end

More pages will be covered by the [Vue Router] (#vue-router)

#### Dynamic Endpoints

The dynamic endpoints neet user data. Authenication will be required to access all of these endpoints.

| URL      | Method    | View Function | Notes                                                                                          |
|----------|-----------|---------------|------------------------------------------------------------------------------------------------|
| /api/user/create | POST | create_user | Creates a user and makes them a cupid or dater as necessary |
| /api/user/<int:id> | GET | get_user | Gets the user's data based on their id number |
| /api/chat/ | POST | send_chat_message | Sends the chat message and returns the AI's response |
| /api/chat/<int:id>/ GET | get_five_messages | Returns the user's five most recent chat messages
| /api/dater/calendar/<int:id>/ | GET, POST | calendar | GET gathers the dater's calendar data, POST creates a new event/date |
| /api/dater/rate/ | POST | rate_dater | Dater rating cupids |
|api/dater/ratings/<int:id>/ | GET | get_dater_ratings | Gets a list of the dater's ratings |
| /api/dater/ratings/<int:id>/ | GET | get_dater_avg_rating | Gets a dater's average rating | 
| /api/dater/money_transfer/ | POST | dater_transfer | Dater can tranfer their money in exchange for cupid cash via an api |
| /api/dater/balance/<int:id>/ | GET | get_dater_balance | Gets the dater's cupid cash balance
| /api/dater/profile/<int:id>/ | GET | get_dater_profile | Get dater's profile
| /api/dater/profile/ | POST | set_dater_profile | Saves/updates the dater's profile |
| /api/dater/gigs/<int:id> | GET | get_dater_gigs | Gets all the gigs that the user has requested |
| /api/cupid/rate/ | POST | rate_cupid | Cupid rating daters |
|api/cupid/ratings/<int:id>/ | GET | get_cupid_ratings | Gets a list of the cupid's ratings |
| /api/cupid/ratings/<int:id>/ | GET | get_cupid_avg_rating | Gets a cupid's average rating | 
| /api/cupid/money_transfer/ | POST | cupid_transfer | Cupids can transfer their earnings out of the app via an api |
| /api/cupid/balance/<int:id>/ | GET | get_cupid_balance | Gets the cupids's income balance
| /api/cupid/profile/<int:id>/ | GET | get_cupid_profile | Get cupid's profile
| /api/cupid/profile/ | POST | set_cupid_profile | Saves/updates the cupid's profile |
| /api/cupid/accepting/ | POST | cupid_accepting | Updates whether the cupid is currently accepting gigs |
| /api/gig/create/ | POST | create_gig | Creates a gig |
| /api/gig/accept/ | POST | accept_gig | Sets the gig as accepted |
| /api/gig/complete/ | POST | complete_gig | Sets the gig as completed |
| /api/gig/drop/ | POST | drop_gig | Sets the gig as dropped by the cupid |
| /api/gig/delete/ | POST | delete_gig | Gig is deleted by the dater |
| /api/gig/<int:dist> | GET | get_gigs | Returns a list of gigs within the cupid's preferred distance |
| /api/geo/stores/<int:id>/ | GET | get_stores | Gets a list of nearby stores |
| /api/geo/activities/<int:id>/ | Get | get_activities | Gets a list of nearby activities |
| /api/geo/events/<int:id>/ | Get | get_events | Gets a list of nearby events |
| /api/geo/attractions/<int:id>/ | Get | get_attractions | Gets a list of nearby attractions |
| /api/geo/user/<int:id>/ | GET | get_user_location | Get the user's current location |
| /api/manager/daters/ | GET | get_daters | Gets a list of daters |
| /api/manager/cupids/ | GET | get_cupids | Gets a list of cupids |
| /api/manager/dater_count/ | GET | get_dater_count | Gets a total count of dater accounts |
| /api/manager/cupid_count/ | GET | get_cupid_count | Gets a total count of cupid accounts |
| /api/manager/active_daters/ | GET | get_active_daters | Gets a count of daters currently using the app |
| /api/manager/active_cupids/ | GET | get_active_cupids | Gets a count of cupids currently using the app |
| /api/manager/gig_rate | GET | get_gig_rate | Returns the number of gigs created per day |
| /api/manager/gig_count | GET | get_gig_count | Returns the number of gigs currently active |
| /api/manager/gig_drop_rate | GET | get_gig_drop_rate | Returns the number of gigs dropped per day |
| /api/manager/gig_complete_rate | GET | get_gig_complete_rate | Returns the number of gigs completed per day |
| /api/manager/suspend/ | POST | suspend | Sets user as suspended |
| /api/manager/unsuspend | POST | unsuspend | sets user as unsuspended |
| /api/manager/delete_user/<string:usertype>/<int:id> | POST | delete_user | Deletes the user whose id number is used |
| /api/stt/ | POST | speech_to_text | Takes in audio and returns the words as text |
| /api/notify/ | POST | notify | Send a notification |

??? TODO:
- check HLD/req for any other required urls
- add to urls.py & views.py

### Django Settings

The file `server/settings.py` will apply settings to the Django project. All of the current settings will be kept the same with the note that:

* `DEBUG` will be set to `False` for the version that is deployed.

### Backend Pseudocode

**cupid_code/urls.py**
``` python
path("", include("api.urls")),
path("api/", include("api.urls")),
path("admin/", admin.site.urls),
```

**api/urls.py**

``` python

from django.url import path
from . import views

urlpatterns = [
  path = ("/" , views.home, name="home"),
  path = ("/login/", views.login, name="login"),
  path = ("/signup/", views.signup, name="signup"),
  path = ("/app/", views.app, name="app"),
  path = ("/api/user/create", views.create_user, name="create_user"),
  path = ("/api/user/<int:id>", views.get_user, name="get_user"),
  path = ("/api/chat/", views.send_chat_message, name="send_chat_message"),
  path = ("/api/chat/<int:id>/", views.get_five_messages, name="get_five_messages"),
  path = ("/api/dater/calendar/<int:id>/", views.calendar, name="calendar"),
  path = ("/api/dater/rate/", views.rate_dater, name="rate_dater"),
  path = ("|api/dater/ratings/<int:id>/", views.get_dater_ratings, name="get_dater_ratings"),
  path = ("/api/dater/ratings/<int:id>/", views.get_dater_avg_rating, name="get_dater_avg_rating"),
  path = ("/api/dater/money_transfer/", views.dater_transfer, name="dater_transfer")
  path = ("/api/dater/balance/<int:id>/" views.get_dater_balance, name="get_dater_balance"),
  path = ("/api/dater/profile/<int:id>/", views.get_dater_profile, name="get_dater_profile"),
  path = ("/api/dater/profile/", views.set_dater_profile, name="set_dater_profile"),
  path = ("/api/dater/gigs/<int:id>", views.get_dater_gigs, name="get_dater_gigs"),
  path = ("/api/cupid/rate/", views.rate_cupid, name="rate_cupid"),
  path = ("api/cupid/ratings/<int:id>/", views.get_cupid_ratings, name="get_cupid_ratings"),
  path = ("/api/cupid/ratings/<int:id>/", views.get_cupid_avg_rating, name="get_cupid_avg_rating"),
  path = ("/api/cupid/money_transfer/", views.cupid_transfer, name="cupid_transfer"),
  path = ("/api/cupid/balance/<int:id>/", views.get_cupid_balance, name="get_cupid_balance"),
  path = ("/api/cupid/profile/<int:id>/", get_cupid_profile, name="get_cupid_profile"),
  path = ("/api/cupid/profile/", views.set_cupid_profile, name="set_cupid_profile"),
  path = ("/api/cupid/accepting/", views.cupid_accepting, name="cupid_accepting"),
  path = ("/api/gig/create/", views.create_gig, name="create_gig"),
  path = ("/api/gig/accept/", views.accept_gig, name="accept_gig"),
  path = ("/api/gig/complete/", views.complete_gig, name="complete_gig"),
  path = ("/api/gig/drop/", views.drop_gig, name="drop_gig"),
  path = ("/api/gig/delete/", views.delete_gig, name="delete_gig"),
  path = ("/api/gig/<int:dist>", views.get_gigs, name="get_gigs"),
  path = ("/api/geo/stores/<int:id>/", views.get_stores, name="get_stores"),
  path = ("/api/geo/activities/<int:id>/", views.get_activities, name="get_activities"),
  path = ("/api/geo/events/<int:id>/", views.get_events, name="get_events"),
  path = ("/api/geo/attractions/<int:id>/", views.get_attractions, name="get_attractions"),
  path = ("/api/geo/user/<int:id>/", views.get_user_location, name="get_user_location"),
  path = ("/api/manager/daters/", views.get_daters, name="get_daters"),
  path = ("/api/manager/cupids/", views.get_cupids, name="get_cupids"),
  path = ("/api/manager/dater_count/", views.get_dater_count, name="get_dater_count"),
  path = ("/api/manager/cupid_count/", views.get_cupid_count, name="get_cupid_count"),
  path = ("/api/manager/active_daters/", views.get_active_daters, name="get_active_daters"),
  path = ("/api/manager/active_cupids/", views.get_active_cupids, name="get_active_cupids"),
  path = ("/api/manager/gig_rate", views.get_gig_rate, name="get_gig_rate"),
  path = ("/api/manager/gig_count", views.get_gig_count, name="get_gig_count"),
  path = ("/api/manager/gig_drop_rate", views.get_gig_drop_rate, name="get_gig_drop_rate"),
  path = ("/api/manager/gig_complete_rate", views.get_gig_complete_rate, name="gig_complete_rate"),
  path = ("/api/manager/suspend/", views.suspend, name="suspend"),
  path = ("/api/manager/unsuspend", views.unsuspend, name="unsuspend"),
  path = ("/api/manager/delete_user/<string:usertype>/<int:id>", views.delete_user, name="delete_user"),
  path = ("/api/stt/", views.speech_to_text, name="speech_to_text"),
  path = ("/api/notify/", views.notify, name="notify"),
]

```

**api/views.py**
``` python

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dater, Cupid, Message, Manager, Gig, Quest, Date, Feedback, PaymentCard, BankAccount
from .serializers import DaterSerializer, CupidSerializer, MessageSerializer, ManagerSerializer, GigSerializer, QuestSerializer, DateSerializer, FeedbackSerializer, PaymentCardSerializer, BankAccountSerializer

def home(request):
    return render(request, "home.html")
    
def signup(request):
    if request.method == "POST":
        validate the form
        return redirect("/login/")
    else:
        return render(request, "signup.html")
        
def login(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/app/")
        else:
            return render(request, "login.html", {"message": "Incorrect Password"})
    else:
        return render(request, "login.html")

def create_user(request):
  for each profile data for user:
    create a variable = request.{specific data}

  dater = Dater(
    model_column = request.POST[matching variable]
  )

  dater.save()
  
  return redirect("/app/")


def get_user(request, id):
  user = {flag that identifies who the user is (Dater/Cupid/Manager)}.objects.get(id=id)

  response = user.json()

  return response

def send_chat_message(request):
  forward_message = request.{name of message in body}
  save forward_message to DB as Message

  response = {method call to send to external AI chat API}
  save response to DB as Message

  return response.json()

def get_five_messages(request, id):
  dater = Dater.objects.get(id=id)

  list_of_messages = Message.objects.filter(owner=id)

  ordered_most_recent_messages = reorder list_of_messages from newest to oldest

  list_of_messages = first five of ordered_most_recent_messages

  response = list_of_messages.json()

  return response

def calendar(request, id):
    if request.method == "POST":
        dater = Dater.objects.get(id=id)
        date = Date(
            dater = dater,
            date_time = request.date_time,
            location = request.location,
            description = request.description,
            status = request.status,
            budget = request.budget,
        )
        date.save()
        return JsonResponse({'message': 'Date has been created'})
    else:
        dater = Dater.objects.get(id=id)
        calendar = Date.objects.filter(dater=id)
        response = calendar.json()
        return response

def rate_dater(request):
  dater_id = request.dater_id
  dater = Dater.get(id=dater_id)
  rating = request.POST["rating"]

  feedback = Feedback(
    user = rating.user,
    intervention_request = rating.intervention_request, 
    message = rating.message,
    star_rating = request.star_rating,
    datetime = rating.datetime, 
  )

  feedback.save()

  new_rating = avg_rating(rating, dater_id)
  dater.avg_rating = new_rating

  dater.save()

  return JsonResponse({'message': 'Rating has been submitted'})

def get_dater_ratings(request, id):
  dater = Dater.objects.get(id=id)

  ratings = Feedback.objects.get(user=id)
  
  response = ratings.json()

  return response

def get_dater_avg_rating(request, id):
  dater = Dater.objects.get(id=id)

  avg_rating = dater.avg_rating

  response = avg_rating.json()

  return response

def dater_transfer(request):
  dater_id = request.user_id
  money_api = request.api_info

  transfer_amount = request.transfer_amount
  
  result = way to transfer money from api(money_api, transfer_amount)

  dater.balance = dater.balance + result

  send result to money_api

  dater.save()

  return JsonResponse({'message': 'Payment successful'})

def get_dater_balance(request, id):
  dater = Dater.objects.get(id=id)

  response = dater.balance.json()

  return response

def get_dater_profile(request, id):
  dater = Dater.objects.get(id=id)

  response = dater.json()

  return response

def set_dater_profile(request):
  dater_id = request.user

  dater = Dater.objects.get(dater_id)

  for each dater profile property sent in request:
    dater.property = profile property sent    

  dater.save()

  return JsonResponse({'message': 'Profile saved'})

def get_dater_gigs(request, id):
  dater = Dater.objects.get(id=id)

  gigs = Gig.objects.get(user=id)

  response = gigs.json()

def rate_cupid(request):
  cupid_id = request.cupid_id
  cupid = Cupid.get(id=cupid_id)
  rating = request.POST["rating"]

  feedback = Feedback(
    user = rating.user,
    intervention_request = rating.intervention_request, 
    message = rating.message,
    star_rating = request.star_rating,
    datetime = rating.datetime, 
  )

  feedback.save()

  new_rating = avg_rating(rating, cupid_id)
  cupid.avg_rating = new_rating

  cupid.save()

  return JsonResponse({'message': 'Rating has been submitted'}) 
  
def get_cupid_ratings(request, id):
  cupid = Cupid.objects.get(id=id)

  ratings = Feedback.objects.get(user=id)
  
  response = ratings.json()

  return response

def get_cupid_avg_rating(request, id):
  cupid = Cupid.objects.get(id=id)

  avg_rating = cupid.avg_rating

  response = avg_rating.json()

  return response

def cupid_transfer(request):
  cupid_id = request.cupid_id
  money_api = request.api_info

  transfer_amount = request.transfer_amount
  
  send transfer_amount to money_api
  
  cupid.balance = dater.balance - transfer_amount

  cupid.save()

  return JsonResponse({'message': 'Deposit successful'})

def get_cupid_balance(request, id):
  cupid = Cupid.objects.get(id=id)

  response = cupid.balance.json()

  return response

def get_cupid_profile(request, id):
  cupid = Cupid.objects.get(id=id)

  response = cupid.json()

  return response

def set_cupid_profile(request):
  cupid_id = request.user

  cupid = Cupid.objects.get(cupid_id)

  for each cupid profile property sent in request:
    cupid.property = profile property sent    

  cupid.save()

  return JsonResponse({'message': 'Profile saved'})

def cupid_accepting(request):
    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address  

    cupid.accepting = True
    cupid.save()

    return JsonResponse({'message': 'Cupid is now active'})

def create_gig(request):
    
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    quest = request.quest
    
    gig = Gig(
        dater = dater,
        cupid = None,
        quest = quest,
        status = 0,
        date_time_of_request = request.date_time_of_request,
        date_time_of_claim = None,
        date_time_of_completion = None,
    )
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been created'})
  
def accept_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address

    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    
    gig.cupid = cupid
    gig.status = 1
    gig.date_time_of_claim = request.date_time_of_claim
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been accepted'})
    
def complete_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address
    
    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    
    gig.status = 2
    gig.date_time_of_completion = request.date_time_of_completion
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been completed'})
    
def drop_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address
    
    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    
    gig.status = 1
    gig.date_time_of_claim = None
    gig.cupid = None
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been dropped'})

def delete_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address
    
    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    
    gig.delete()
    
    return JsonResponse({'message': 'Gig has been deleted'})
    
def get_gigs(request, count):
    gigs = Gig.objects.all()[:count]
    
    response = gigs.json()
    
    return response
    
def get_stores(request):
    
    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    stores = method call to get stores
    
    response = stores.json()
    
    return response
    
def get_activities(request):
    
    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address

    activities = method call to get activities
    
    response = activities.json()
    
    return response
    
def get_events(request):
    
    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    events = method call to get events
    
    response = events.json()
    
    return response
    
def get_attractions(request):

    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    attractions = method call to get attractions
    
    response = attractions.json()
    
    return response
    
def get_user_location(request, id):
    user = User.objects.get(id=id)
    
    location = user.location
    
    response = location.json()
    
    return response
    
def get_cupids(request):
    cupids = Cupid.objects.all()
    
    response = cupids.json()
    
    return response
    
def get_daters(request):
    daters = Dater.objects.all()
    
    response = daters.json()
    
    return response
    
def get_dater_count(request):
    dater_count = Dater.objects.count()
    
    response = dater_count.json()
    
    return response
    
def get_cupid_count(request):
    cupid_count = Cupid.objects.count()
    
    response = cupid_count.json()
    
    return response
    
def get_active_cupids(request):
    active_cupids = Cupid.objects.filter(status=2)
    
    response = active_cupids.json()
    
    return response
    
def get_active_daters(request):
    active_daters = Dater.objects.filter(status=2)
    
    response = active_daters.json()
    
    return response
    
def get_gig_rate(request):
    dates = Gig.objects.filter(status=1).count()
    gig_rate = Gig.objects.filter(status=1).count()
    
    rate = gig_rate / dates
    
    response = rate.json()
    
    return response

def get_gig_count(request):
    gig_count = Gig.objects.count()
    
    response = gig_count.json()
    
    return response
    
def get_gig_drop_rate(request):
    dates = Gig.objects.filter(status=3).count()
    gig_drop_rate = Gig.objects.filter(status=3).count()
    
    rate = gig_drop_rate / dates
    
    response = rate.json()
    
    return response
    
def get_gig_complete_rate(request):
    dates = Gig.objects.filter(status=2).count()
    gig_complete_rate = Gig.objects.filter(status=2).count()
    
    rate = gig_complete_rate / dates
    
    response = rate.json()
    
    return response
    
def suspend(request):
    user_id = request.user_id
    user = User.get(id=user_id)
    user.suspended = True
    
def unsuspend(request):
    user_id = request.user_id
    user = User.get(id=user_id)
    user.suspended = False

def delete_user(request, usertype, id):
  if usertype == "dater":
    user = Dater.objects.get(id=id)
  else if usertype == "cupid":
    user = Cupid.objects.get(id=id)
  else:
    return JsonResponse({'message': 'Invalid usertype'})
  
  user.delete()
  return JsonResponse({'message': 'The {usertype} has been deleted'})
    
def speech_to_text(request):

    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    file = request.file
    text = api call to convert speech to text
    
    message = Message(
        owner = dater,
        text = text,
        from_ai = False,
    )
    
    ai_response = api call to convert text to speech
    ai_message = Message(
        owner = dater,
        text = ai_response,
        from_ai = True,
    )
    
    message.save()
    ai_message.save()
    
    return ai_message.json()
    
def notify(request):
    user_id = request.user_id
    user = User.get(id=user_id)
    message = request.message
    
        message = Message(
        owner = user,
        text = message,
        from_ai = True,
    )
    
    communication_preference = user.communication_preference
    
    if communication_preference == 1:
        send message to user's phone
    elif communication_preference == 2:
        send message to user's email
    elif communication_preference == 3:
        send message to user's phone and email
        
    message.save()
    
    return message.json()

```

**server/settings.py**

``` python
DEBUG = False #for production
```