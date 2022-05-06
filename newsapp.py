from flask import Flask 
from newsapi impot NewsApiClient


app = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="206c52b0288342de8f6d76f653647450")
    top_headlines = newsapi.get_top_headlines(sources='bbc-news', language='en', country='us')

    articles = top_headlines['articles']

    #add lists to append the data
    desc = []
    news = []
    img = []