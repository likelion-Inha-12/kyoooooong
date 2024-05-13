from django.shortcuts import render

from django.http import HttpResponse, response


def health(request):
    return HttpResponse(status = 200, content = "seminar server ok!")

def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return response(response, status=status)
