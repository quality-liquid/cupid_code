import datetime
from typing import Dict, Any


def get_server_time() -> Dict[str, Any]:
    """Returns the current server time."""
    return {"server_time": datetime.datetime.now().isoformat() + "Z"}

# TODO: Add functions to expose our existing server capabilities to AI tools here.

# Additional AI tool functions can be added here

AI_FUNCTIONS = {
    "get_server_time": get_server_time,
    # Add more functions as needed
}

AI_FUNCTION_SCHEMAS = {
    "get_server_time": {
        "description": "Get the current server time in ISO 8601 format.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    # Add more function schemas as needed
}
