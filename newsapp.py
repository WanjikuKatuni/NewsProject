from flask import Flask, render_template
from newsapi import NewsApiClient



app = Flask(__name__)

@app.route('/') #create url path/method
def index():
    

    newsapi = NewsApiClient(api_key="206c52b0288342de8f6d76f653647450")
    #to get latest news from many articles
    top_headlines = newsapi.get_top_headlines(sources='bbc-news, abc-news, cnn, nfl-news', language='en')

    articles = top_headlines['articles']

    #add lists to append the data
    description = []
    #news = []
    img = []
    datepublished = []
    #bywho = []


    for i in range(len(articles)):
        newsarticles = articles[i]

        #fetching information
        #news.append(newsarticles['title']) #fetch title
        datepublished.append(newsarticles['publishedAt']) #fetch date published
        description.append(newsarticles['description']) # fetch description
        img.append(newsarticles['urlToImage']) #fetchimages
        #bywho.append(newsarticles['author']) #fetch author details
    
    #send data to indexhtml

    newslist = zip(datepublished, description, img)

    return render_template('index.html', context=newslist)



#bbc news
@app.route('/bbc.html') #create url path/method
def bbc():
    

    newsapi = NewsApiClient(api_key="206c52b0288342de8f6d76f653647450")
    #to get latest news from many articles
    top_headlines = newsapi.get_top_headlines(sources='bbc-news', language='en')

    articles = top_headlines['articles']

    #add lists to append the data
    description = []
    #news = []
    img = []
    datepublished = []
    #bywho = []


    for i in range(len(articles)):
        newsarticles = articles[i]

        #fetching information
        #news.append(newsarticles['title']) #fetch title
        datepublished.append(newsarticles['publishedAt']) #fetch date published
        description.append(newsarticles['description']) # fetch description
        img.append(newsarticles['urlToImage']) #fetchimages
        #bywho.append(newsarticles['author']) #fetch author details
    
    #send data to indexhtml

    newslist = zip(datepublished, description, img)

    return render_template('bbc.html', context=newslist)


@app.route('/abc.html') #create url path/method
def abc():
    

    newsapi = NewsApiClient(api_key="206c52b0288342de8f6d76f653647450")
    #to get latest news from many articles
    top_headlines = newsapi.get_top_headlines(sources='abc-news', language='en')

    articles = top_headlines['articles']

    #add lists to append the data
    description = []
    #news = []
    img = []
    datepublished = []
    #bywho = []


    for i in range(len(articles)):
        newsarticles = articles[i]

        #fetching information
        #news.append(newsarticles['title']) #fetch title
        datepublished.append(newsarticles['publishedAt']) #fetch date published
        description.append(newsarticles['description']) # fetch description
        img.append(newsarticles['urlToImage']) #fetchimages
        #bywho.append(newsarticles['author']) #fetch author details
    
    #send data to indexhtml

    newslist = zip(datepublished, description, img)

    return render_template('abc.html', context=newslist)




#NFL

@app.route('/nfl.html') #create url path/method
def nfl():
    

    newsapi = NewsApiClient(api_key="206c52b0288342de8f6d76f653647450")
    #to get latest news from many articles
    top_headlines = newsapi.get_top_headlines(sources='nfl-news', language='en')

    articles = top_headlines['articles']

    #add lists to append the data
    description = []
    #news = []
    img = []
    datepublished = []
    #bywho = []


    for i in range(len(articles)):
        newsarticles = articles[i]

        #fetching information
        #news.append(newsarticles['title']) #fetch title
        datepublished.append(newsarticles['publishedAt']) #fetch date published
        description.append(newsarticles['description']) # fetch description
        img.append(newsarticles['urlToImage']) #fetchimages
        #bywho.append(newsarticles['author']) #fetch author details
    
    #send data to indexhtml

    newslist = zip(datepublished, description, img)

    return render_template('nfl.html', context=newslist)



#cnn

@app.route('/cnn.html') #create url path/method
def cnn():
    

    newsapi = NewsApiClient(api_key="206c52b0288342de8f6d76f653647450")
    #to get latest news from many articles
    top_headlines = newsapi.get_top_headlines(sources='cnn', language='en')

    articles = top_headlines['articles']

    #add lists to append the data
    description = []
    #news = []
    img = []
    datepublished = []
    #bywho = []


    for i in range(len(articles)):
        newsarticles = articles[i]

        #fetching information
        #news.append(newsarticles['title']) #fetch title
        datepublished.append(newsarticles['publishedAt']) #fetch date published
        description.append(newsarticles['description']) # fetch description
        img.append(newsarticles['urlToImage']) #fetchimages
        #bywho.append(newsarticles['author']) #fetch author details
    
    #send data to indexhtml

    newslist = zip(datepublished, description, img)

    return render_template('cnn.html', context=newslist)



#home

@app.route('/home.html') #create url path/method
def home():
    

    newsapi = NewsApiClient(api_key="206c52b0288342de8f6d76f653647450")
    #to get latest news from many articles
    top_headlines = newsapi.get_top_headlines(sources='cnn, bbc-news, abc-news, nfl-news', language='en')

    articles = top_headlines['articles']

    #add lists to append the data
    description = []
    #news = []
    img = []
    datepublished = []
    #bywho = []


    for i in range(len(articles)):
        newsarticles = articles[i]

        #fetching information
        #news.append(newsarticles['title']) #fetch title
        datepublished.append(newsarticles['publishedAt']) #fetch date published
        description.append(newsarticles['description']) # fetch description
        img.append(newsarticles['urlToImage']) #fetchimages
        #bywho.append(newsarticles['author']) #fetch author details
    
    #send data to indexhtml

    newslist = zip(datepublished, description, img)

    return render_template('home.html', context=newslist)

# run application in debug stage

if __name__ == "__main__":
        app.run(debug = True)