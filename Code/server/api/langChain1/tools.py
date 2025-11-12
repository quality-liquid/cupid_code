try:
    from .askGroq import ask_groq
except ImportError:
    from askGroq import ask_groq

def you_are_a_nerd(tool_input=None):
    """Tool callable used by the agent.

    The agent will pass a single positional argument (the tool input string),
    so accept an optional parameter and return a string result.
    """
    # Return a message; avoid printing to prevent duplicate lines when called multiple times
    return "You are a nerd! "

def changeTheTopicAboutHer(tool_input=None):
    return "Let's change the topic to something more interesting! Ask her about her favorite book."

def talkingAboutStarWars(tool_input=None):
    return "Ah, Star Wars! A classic saga of good versus evil in a galaxy far, far away."

def talkingAboutTheHobbit(tool_input=None):
    return "The Hobbit is a fantastic adventure story by J.R.R. Tolkien, following Bilbo Baggins on his journey."

def talkingAboutStarTrek(tool_input=None):
    return "Star Trek explores the adventures of the starship Enterprise and its crew as they explore new worlds."

def talkingAboutLordOfTheRings(tool_input=None):   
    return "The Lord of the Rings is an epic fantasy trilogy by J.R.R. Tolkien, centered around the quest to destroy the One Ring."

def talkingAboutThisTVShow(tool_input=None, show_name="Unknown Show"):
    showInformation = ""
    if show_name == "none":
        return "No TV show mentioned."
    else:
        showInformation = ask_groq(f"Tell me about {show_name}")
    return f"I see you are talking about {show_name}! This show is about {showInformation}. \n\n Does she like this show too? Ask her."