import json

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from user.models import UserAuth


def index(request):
    return HttpResponse("Hello, world. You're at the user app index.")


def user_register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:

            user = UserAuth.objects.create_user(username=data.get("username"), password=data.get("password"),
                                                first_name=data.get("first_name"), last_name=data.get("last_name"),
                                                email=data.get("email"), address=data.get("address"),
                                                phone_number=data.get("phone_number"))
            # user = User(user_name=data.get("user_name"), password=data.get("password"),
            #             first_name=data.get("first_name"), last_name=data.get("last_name"),
            #             email=data.get("email")
            # user.save()
            return JsonResponse({"message": f"user {user.username} added successfully"})
        except Exception as err:
            print(err)
            return JsonResponse({"message": f"username {data.get('username')} already exists"}, status=400)

    return JsonResponse({"message": "method not allowed"})


def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = authenticate(username=data.get("username"), password=data.get("password"))
            if user is not None:
                # A backend authenticated the credentials
                return JsonResponse({"message": f"login is successful {user.username}"})
            else:
                # No backend authenticated the credentials
                return JsonResponse({"message": "incorrect username/password"})
        except Exception as err:
            return JsonResponse({"message": str(err)})
    return JsonResponse({"message": "method not allowed"})
