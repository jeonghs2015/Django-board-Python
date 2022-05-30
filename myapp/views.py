from http.client import HTTPResponse
from django.http import HttpResponse
import random

from django.shortcuts import render
from numpy import require

# Create your views here.
nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body' : 'Routing is ...'},
    {'id':2, 'title':'view', 'body' : 'View is ...'},
    {'id':3, 'title':'model', 'body' : 'Model is ...'},
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]} </a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}<br>
        <ul>
            <li><a href="/create/">Create</a></li>
        </ul>
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

    
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id" : nextId, "title" : title, "body" : body}

