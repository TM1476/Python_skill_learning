from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        blob = TextBlob(rawtext)
      
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        if polarity > 0:
            result = "Positive"
            color = "success"
        elif polarity < 0:
            result = "Negative"
            color = "danger"
        else:
            result = "Neutral"
            color = "secondary"
            
        return render_template('index.html', 
                               result=result, 
                               polarity=round(polarity, 2), 
                               subjectivity=round(subjectivity, 2), 
                               rawtext=rawtext,
                               color=color)

if __name__ == '__main__':
    app.run(debug=True)
