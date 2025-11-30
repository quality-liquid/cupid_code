def testMethod(transcript = ''):
    print("This is a test method.")
    print(f"Transcript received: {transcript}")
    # console.log("Test method executed.")
    return f"Test method executed with transcript: {transcript}"

from .mainAgent import create_agent, create_TV_agent

def filterResponse(transcript = ''):
    nerd_agent = create_agent()
    tv_agent = create_TV_agent()


    text = transcript
    nerd_result = nerd_agent.invoke({"input_text": text})
    tv_result = tv_agent.invoke({"input_text": text})
    
    nerd_response = nerd_result.get("result") or ""
    tv_response = tv_result.get("result") or ""
    
    # Combine responses
    responses = []
    if nerd_response and nerd_response != "No relevant tools to call.":
        responses.append(f"🎬 NERD DETECTOR:\n{nerd_response}")
    if tv_response and tv_response != "No relevant tools to call.":
        responses.append(f"📺 TV SHOW DETECTOR:\n{tv_response}")

    final_response = "\n\n".join(responses) if responses else "No relevant information detected."
    return final_response