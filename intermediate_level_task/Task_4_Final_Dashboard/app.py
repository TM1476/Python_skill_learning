from flask import Flask, render_template, request
from textblob import TextBlob
from google import genai
from googlesearch import search

app = Flask(__name__, template_folder='.')

GEMINI_API_KEY = "AIzaSyAgSySyvQF_Demn6nI2v0G5iqCOkZu_N8I"
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('sentiment_text', '')
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 2)
    
    if polarity > 0: result, color = "Positive", "success"
    elif polarity < 0: result, color = "Negative", "danger"
    else: result, color = "Neutral", "secondary"
    
    return render_template('dashboard.html', sentiment_res=result, pol=polarity, original_text=text, color=color)

@app.route('/search', methods=['POST'])
def ai_search():
    query = request.form.get('search_query', '')
    print(f"Searching for: {query}")
    
    context = ""
    try:
        for res in search(query, num_results=3):
            context += f"Source: {res}\n"
    except:
        context = "No live web data found."

    try:
        prompt = f"Using these sources, answer the query: {query}\n\nSources:\n{context}"
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        answer = response.text
    except Exception as e:
        answer = f"Error: {e}"

    return render_template('dashboard.html', search_answer=answer, user_query=query)

if __name__ == '__main__':
    app.run(debug=True)
