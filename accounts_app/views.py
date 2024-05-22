from django.shortcuts import render,HttpResponse



# def userlist (request):
#     return render(request, "accounts_app/userlist.html", context={"userlist": users})


# def profile(request, username):
#     for user in users:
#         if user['username'] == username:
#             return render(request, "accounts_app/profile.html", context={'user': user})       


def info(requset):
    return render(requset, "accounts_app/info.html",)
