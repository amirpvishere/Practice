from django.shortcuts import render, HttpResponse

# users = ["amir", 'fati', 'pedram', 'arash', 'reza', 'mahan']
# blocked_users = ['reza', 'mahan']


def profile(request, username):
    return render(request, "accounts_app/profile.html",)
    # if username in users:
    #     if username in blocked_users:
    #         return HttpResponse(f'<h1>{username.capitalize()} is blocked.</h1>')
    #     else:
    #         return HttpResponse(f"<h1>This is {username.capitalize()}'s Page</h1>")
    # else:
    #     return HttpResponse("<h1>This Page is Not Found</h1>")


def info(requset):
    return HttpResponse("<h1>This is info page</h1>")
