import json

from django.http import HttpResponse, JsonResponse

from user.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the user app index.")


def register_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # #user = User.objects.create(user_name=data.get("user_name"), password=data.get("password"),
            #                            first_name=data.get("first_name"), last_name=data.get("last_name"),
            #                            email=data.get("email"))
            user = User(user_name=data.get("user_name"), password=data.get("password"),
                        first_name=data.get("first_name"), last_name=data.get("last_name"),
                        email=data.get("email"))
            print(user)
            user.save()
            return JsonResponse({"message": f"user {user.user_name} added successfully"})
        except Exception:
            return JsonResponse({"message": f"username {user.user_name} already exists"})

    return JsonResponse({"message": "method not allowed"})


def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            user = User.objects.filter(user_name=data.get("user_name"), password=data.get("password"))
            print(user)
            # if user is None:
            #     return JsonResponse({"message": "incorrect username/password"})
            return JsonResponse({"message": f"login is successful {user.first().user_name}"})
        except Exception as err:
            print(err)
            return JsonResponse({"message": "incorrect username/password"})
    return JsonResponse({"message": "method not allowed"})
