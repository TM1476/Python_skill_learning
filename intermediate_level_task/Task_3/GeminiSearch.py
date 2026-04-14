from google import genai
from googlesearch import search

client = genai.Client(api_key="AIzaSyAgSySyvQF_Demn6nI2v0G5iqCOkZu_N8I")
MODEL_ID = "gemini-2.0-flash" 

def get_web_context(query):
    print(f"Searching the web for: {query}...")
    context = ""
    try:
        for result in search(query, num_results=3):
            context += f"Source URL: {result}\n"
    except Exception as e:
        print(f"Search error: {e}")
    return context

def ask_gemini(query):
    web_data = get_web_context(query)

    prompt = (
        f"You are a QSkill Research Assistant. Answer the user's question based on "
        f"these web sources.\n\nQuestion: {query}\n\nSources:\n{web_data}"
    )

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text

def main():
    print("=== QSkill AI Search Assistant (Gemini 2.0) ===")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nWhat do you want to search for? ")
        if user_input.lower() == 'exit':
            break
        if not user_input.strip():
            continue
            
        try:
            answer = ask_gemini(user_input)
            print("\n--- AI Answer ---")
            print(answer)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
