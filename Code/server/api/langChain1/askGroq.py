"""
Simple Groq chat interface for getting conversational responses.
"""

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage


def ask_groq(user_message: str, system_prompt: str = None, model: str = "llama-3.3-70b-versatile") -> str:
    """
    Send a message to Groq and get a simple chat response.
    
    Args:
        user_message: The user's message/question
        system_prompt: Optional system prompt to set context (default: friendly assistant)
        model: Groq model to use (default: llama-3.3-70b-versatile)
        
    Returns:
        String response from the LLM
    """
    llm = ChatGroq(model=model)
    
    messages = []
    
    # Add system message if provided
    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))
    else:
        messages.append(SystemMessage(content="""
            You are a helpful assistant with the main role to give some context 
            about a specific TV SHOW. You will give no more than three sentences 
            about the tv show in question.""")
        )
    
    # Add user message
    messages.append(HumanMessage(content=user_message))
    
    # Get response
    response = llm.invoke(messages)
    
    return response.content

