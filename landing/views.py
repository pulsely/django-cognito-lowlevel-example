from django.shortcuts import render
from cognitolowlevel.handlers.backend import CognitoAuthenticator

# Create your views here.
def landing_index(request):

    return render( request, "landing/index.html", {
        'authentication_url' : CognitoAuthenticator().authentication_url
    })