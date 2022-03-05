from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    answer = '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Django Hello,World Website</title>
        </head>
        <style>
            body {
                font-family: Arial;
            }
            h1 {
                color: red;
                font-weight: lighter;
            }

        </style>
        <body>
            <h1> Hello, World </h1>
        </body>
    </html>
    
    '''
    return HttpResponse(answer)