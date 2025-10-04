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
| /api/user/sign_in | POST | sign_in | Signs the user in and returns their daa
| /api/user/<int:id> | GET | get_user | Gets the user's data based on their id number |
| /api/chat/ | POST | send_chat_message | Sends the chat message and returns the AI's response |
| /api/chat/<int:id>/ GET | get_five_messages | Returns the user's five most recent chat messages
| /api/dater/calendar/<int:id>/ | GET, POST | calondar | GET gathers the dater's calendar data, POST creates a new event/date |
| /api/dater/rate/ | POST | rate_dater | ??? |
|api/dater/ratings/<int:id>/ | GET | get_dater_ratings | Gets a list of the dater's ratings |
| /api/dater/ratings/<int:id>/ | GET | get_dater_avg_rating | Gets a dater's average rating | 
| /api/dater/transfer/ | POST | dater_transfer | ??? |
| /api/dater/balance/<int:id>/ | GET | get_dater_balance | Get's the dater's cupid cash balance
| /api/dater/profile/<int:id>/ | GET | get_dater_profile | Get dater's profile
| /api/dater/profile/ | POST | set_dater_profile | Saves/updates the dater's profile |
| /api/dater/save_card | POST | save_card | what the hell is a card ??? |
| /api/dater/get_cards/<int:id>/ | GET | get_cards | ??? |
| /api/dater/gigs/<int:id> | GET | get_dater_gigs | Gets all the gigs that the user has requested |
| /api/cupid/rate/ | POST | rate_cupid | ??? |
|api/cupid/ratings/<int:id>/ | GET | get_cupid_ratings | Gets a list of the cupid's ratings |
| /api/cupid/ratings/<int:id>/ | GET | get_cupid_avg_rating | Gets a cupid's average rating | 
| /api/cupid/transfer/ | POST | cupid_transfer | ??? |
| /api/cupid/balance/<int:id>/ | GET | get_cupid_balance | Get's the cupids's income balance
| /api/cupid/profile/<int:id>/ | GET | get_cupid_profile | Get cupid's profile
| /api/cupid/profile/ | POST | set_cupid_profile | Saves/updates the cupid's profile |
| /api/cupid/save_bank_account/ | POST | save_bank_account | aren't we using paypal ??? |
| /api/cupid/accepting/ | POST | cupid_accepting | Updates whether the cupid is accepting |
| /api/gig/create/ | POST | create_gig | Creates a gig |
| /api/gig/accept/ | POST | accept_gig | How is this different that cupid_accepting idk ??? |
| /api/gig/complete/ | POST | complete_gig | Sets the gig as completed |
| /api/gig/drop/ | POST | Sets the gig as dropped by the cupid |
| /api/gig/delete/ | POST | delete_gig | Gig is deleted by the dater |
| /api/gig/<int:dist> | GET | get_gigs | Returns a list of gigs within the cupid's preferred distance |
| /api/geo/stores/<int:id>/ | GET | get_stores | Gets a list of nearby stores ??? what is id for |
| /api/geo/activities/<int:id>/ | Get | get_activities | Gets a list of nearby activities |
| ??? | How are events | activities | and attractions different |
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
| /api/manager/delete_user/<int:id> | POST | delete_user | Deletes the user whose id number is used |
| /api/stt/ | POST | speech_to_text | Takes in audio and returns the words as text |
| /api/notify/ | POST | notify | Send a notification |

??? TODO:
- check all questionable items
- check HLD/req for any other required urls

### Django Settings

The file `server/settings.py` will apply settings to the Django project. These adjustments will be made in order to comply with this program:

* `DEBUG` will be set to `False` for the version that is deployed.
* `ALLOWED_HOSTS` will be set to the project's domain name.
* django.contrib.admin will be added to `INSTALLED_APPS` in order to access Django admin.
* Any APIs used will be added to `INSTALLED_APPS`.
* `MIDDLEWARE` will also include the asset middleware. ???
* `STATIC_URL` will be set to the asset url ???
* `TEMPLATES` will be adjusted to include `home.html`
* `SECURE_SSL_REDIRECT` will be set to `True`
* `SESSION_COOKIE_SECURE` will be set to `True`

### Backend Pseudocode

**cupid_code/urls.py**
``` python
path("", include("api.urls")),
path("api/", include("api.urls")),
path("admin/", admin.site.urls),
```

**api/urls.py**

**api/serializers.py**
``` python

from rest_framework import serializers # ???

```

**api/views.py**

**server/settings.py**

``` python

DEBUG = False #for production

ALLOWED_HOSTS = [
    'cupid-code.com', 
    #to be substituted with the actual domain
]

INSTALLED_APPS = [
  ...
  'django.contrib.admin',
  'rest_framework',
  'api',
  ...
]

MIDDLEWARE = [
    'asset', #???
]

TEMPLATES = [
    {
      ...
        'DIRS': ['home.html'],
      ...
        },
    },
]

STATIC_URL = 'static/' # ???

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True