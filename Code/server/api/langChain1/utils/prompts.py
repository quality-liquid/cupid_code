# LangChain v1 moved ChatPromptTemplate to langchain_core.prompts
try:
  from langchain_core.prompts import ChatPromptTemplate
except ImportError:  # fallback for older/langchain 0.x layouts
  from langchain.prompts import ChatPromptTemplate

# Return one of: star_wars | hobbit | star_trek | lotr | none
NERD_FILTERING_PROMPT = ChatPromptTemplate.from_template(
	"""
Classify the following text into exactly one category:
- star_wars (any Star Wars references)
- hobbit (any The Hobbit references)
- star_trek (any Star Trek references)
- lotr (any The Lord of the Rings references)
- none (none of the above)

Return ONLY one of these tokens: star_wars | hobbit | star_trek | lotr | none.

Text: {input_text}
"""
)


ALL_TV_SHOWS_PROMPT = ChatPromptTemplate.from_template(
    """
    If the input text mentions any TV show, return only the name of the tv show
    If no TV shows are mentioned, return none.
    Text: {input_text}
"""
)

EMAIL_PROMPT = ChatPromptTemplate.from_template(
    """
You are an email address extractor.
    
Given a person's name or description, return ONLY their email address.
If you cannot determine an email address, respond with 'none'.

Examples:
    If the input asks to send an email to Shelby, respond with the following format: Shelby@willjensen.com
    If the input asks for Brad or Bradford, respond with: epicbw77@gmail.com
    If the input asks for Garrett or Mr. Woodhouse, respond with: gwoodyduke@gmail.com
    If the prompt asks for Luke, respond with: lukestockett33@gmail.com
    If the input does not ask to send an email to any of these people, respond with: none

Return ONLY the email address, nothing else.

Text: {input_text}
"""
)

# For one-shot email instructions: multi-recipient + mode extraction
# Returns JSON: {"emails": ["...", "..."], "topic": "...", "mode": "combined"|"separate"}
ONE_SHOT_EMAIL_PROMPT = ChatPromptTemplate.from_template(
    """
You extract structured information from a natural language email instruction.

Known name to email mappings (ONLY these are valid):
  Shelby -> Shelby@willjensen.com
  Brad or Bradford -> epicbw77@gmail.com
  Garrett or Mr. Woodhouse -> gwoodyduke@gmail.com
  Luke -> lukestockett33@gmail.com
  Mom or Andrea -> andreamwoodhouse@gmail.com
  Dad or Scott -> swoodhouse1@gmail.com
  Rebecca or Becca -> becwoodhouse@gmail.com
  Mitch or Mitchell -> mitchwoodhouse15@gmail.com
  The family -> The emails for Scott, Andrea, Brad, Garrett, Becca, and Mitch

  
Parse the instruction and return a JSON object with these exact keys:
- "emails": array of zero or more mapped email addresses (use the mapping above; do not invent)
- "topic": short phrase describing what the email should be about (extract from the instruction)
- "mode": "combined" if the instruction implies a single group email (e.g., "together", "group", "same email"),
           or "separate" if it implies individual emails (e.g., "separate", "individually", "each", "one by one").
           If multiple names are present and wording is ambiguous, default to "combined".

Compatibility: If the instruction clearly targets only one person, still return an array with that single email.

Examples:
  Input: "Send an email to Brad and tell him a funny joke"
  Output: {{"emails": ["epicbw77@gmail.com"], "topic": "funny joke", "mode": "combined"}}

  Input: "Email Garrett about the meeting agenda"
  Output: {{"emails": ["gwoodyduke@gmail.com"], "topic": "meeting agenda", "mode": "combined"}}

  Input: "Send Luke and Shelby an update about our Q4 plans"
  Output: {{"emails": ["lukestockett33@gmail.com", "Shelby@willjensen.com"], "topic": "Q4 plans", "mode": "combined"}}

  Input: "Send separate emails to Brad and Garrett about interviews"
  Output: {{"emails": ["epicbw77@gmail.com", "gwoodyduke@gmail.com"], "topic": "interviews", "mode": "separate"}}

  Input: "Email Taylor about the budget"
  Output: {{"emails": [], "topic": "budget", "mode": "combined"}}

Return ONLY valid JSON. No markdown, no commentary.

Text: {input_text}
"""
)