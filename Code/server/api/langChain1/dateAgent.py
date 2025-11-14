import os

from groq import Groq

def date_planner():
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    history = []

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": """You are a romantic date planner. 
                    Start by greeting the user and asking for their ideas for the date 
                    and any information about their partner. Keep this message concise.""",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)
    history.append(chat_completion.choices[0].message)

    user_input = input("User: ")
    history.append({"role": "user", "content": user_input})
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """Suggest exactly 3 (no more or less) date ideas 
                            based on their input and preferences.
                            Number then 1, 2, and 3.
                            Prompt the user to pick one of the ideas by number.""",
            },
            {
                "role": "user",
                "content": user_input,
            },
            {
                "role": "system",
                "content": "chat history: " + str(history),
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    print("Bot:", chat_completion.choices[0].message.content)
    history.append(chat_completion.choices[0].message)

    user_input = input("User: ")
    history.append({"role": "user", "content": user_input})
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """Reply with a summary of the idea they chose in this format:
                    date = {
                      "date_time": "",
                      "description": <insert description>,
                      "location": <insert location>,
                    }""", 
            },
            {
                "role": "user",
                "content": user_input,
            },
            {
                "role": "system",
                "content": "chat history: " + str(history),
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    # open date creation form with the date details
    return(chat_completion.choices[0].message.content)