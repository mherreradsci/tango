from django.shortcuts import render



def index(request):
    # Construct a dictionary to pass to the template engine as
    # its context. Note the key boldmessage matches to
    # {{ aboldmessage }} in the template!
    context_dict = {"aboldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, "rango/index.html", context=context_dict)


def about(request):
    context_dict = {"username": "mherrera"}
    return render(request, "rango/about.html", context_dict)
