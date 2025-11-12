# Prefer relative import within the package; fall back to local when run as a script
try:
    from .agents import create_agent, create_TV_agent  # type: ignore
except Exception:
    from agents import create_agent, create_TV_agent  # type: ignore


def main():
    # Create both agents once
    print("Initializing agents...")
    nerd_agent = create_agent()
    tv_agent = create_TV_agent()
    print("Both agents ready!\n")

    text = input("Enter your message: ")
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
    print("\n" + final_response)
if __name__ == "__main__":
    main()