import datetime
from typing import Dict, Any, Optional, List

from django.utils.timezone import now as tz_now

# Local
from .models import User, Dater, Cupid, Message  # removed Gig, Quest
from . import helpers


def get_server_time() -> Dict[str, Any]:
    """Returns the current server time."""
    return {"server_time": datetime.datetime.now().isoformat() + "Z"}


# Functions to expose our existing server capabilities to AI tools here.

def get_user_summary(user_id: Optional[int] = None) -> Dict[str, Any]:
    """
    Return a minimal summary of the authenticated user.
    """
    if not user_id:
        return {"error": "unauthenticated"}
    user = User.objects.get(id=user_id)
    data: Dict[str, Any] = {
        "id": user.id,
        "role": user.role,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    if hasattr(user, "dater"):
        d = user.dater
        data["dater"] = {
            "balance": d.cupid_cash_balance,
            "budget": d.budget,
        }
    if hasattr(user, "cupid"):
        c = user.cupid
        data["cupid"] = {
            "balance": c.cupid_cash_balance,
            "avg_rating": (c.rating_sum / c.rating_count) if c.rating_count else None,
        }
    return data


def list_nearby_places(category: str, limit: int = 5, user_id: Optional[int] = None) -> Dict[str, Any]:
    """
    List nearby places for the authenticated Dater using Yelp.
    Allowed categories: restaurants, stores, activities, events, attractions
    """
    if not user_id:
        return {"error": "unauthenticated"}
    allowed = {"restaurants", "stores", "activities", "events", "attractions"}
    if category not in allowed:
        return {"error": "invalid_category", "allowed": sorted(list(allowed))}
    # helpers.call_yelp_api expects a dater user_id and a search term
    raw = helpers.call_yelp_api(user_id, category)
    if not raw:
        return {"results": []}

    # yelpapi returns dict with key 'businesses'
    businesses = raw.get("businesses", [])
    items: List[Dict[str, Any]] = []
    for b in businesses[: max(0, int(limit))]:
        location = b.get("location") or {}
        address = " ".join(location.get("display_address", [])) if isinstance(location, dict) else None
        items.append(
            {
                "name": b.get("name"),
                "address": address,
                "rating": b.get("rating"),
                "phone": b.get("display_phone") or b.get("phone"),
                "url": b.get("url"),
            }
        )
    return {"results": items}


def get_recent_messages(count: int = 5, user_id: Optional[int] = None) -> Dict[str, Any]:
    """
    Return the most recent messages for the authenticated user.
    """
    if not user_id:
        return {"error": "unauthenticated"}
    msgs = Message.objects.filter(owner_id=user_id).order_by("-id")[: max(0, int(count))]
    return {
        "messages": [
            {"id": m.id, "from_ai": m.from_ai, "text": m.text}
            for m in reversed(list(msgs))
        ]
    }

# Additional AI tool functions can be added here

AI_FUNCTIONS = {
    "get_server_time": get_server_time,
    "get_user_summary": get_user_summary,
    "list_nearby_places": list_nearby_places,
    "get_recent_messages": get_recent_messages,
}

# OpenAI tool definitions (function schemas)
AI_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_server_time",
            "description": "Get the current server time in ISO 8601 format.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_user_summary",
            "description": "Get a minimal summary of the authenticated user (role, name, balances).",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_nearby_places",
            "description": "List nearby places for the authenticated Dater, using Yelp.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["restaurants", "stores", "activities", "events", "attractions"],
                    },
                    "limit": {"type": "integer", "minimum": 1, "maximum": 10, "default": 5},
                },
                "required": ["category"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_recent_messages",
            "description": "Get the most recent chat messages for the authenticated user.",
            "parameters": {
                "type": "object",
                "properties": {"count": {"type": "integer", "minimum": 1, "maximum": 50, "default": 5}},
                "required": [],
            },
        },
    },
]
