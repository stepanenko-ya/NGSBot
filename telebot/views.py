from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from .models import Message, Admins, Activities, ClientAdmin
import random


def main_page(request):

    # Generate a personal ID for a User
    user_id = random.randrange(10000, 99999)

    return render(request, "telebot/main_page.html", locals())


def ajax_send_message(request):

    bot_token = settings.BOT_TOKEN
    message_text = request.GET.get("message_text")
    user_id = request.GET.get("user_id")

    enable_client = ClientAdmin.objects.filter(clientId=user_id).first()
    if enable_client:

        chat = enable_client.adminId
        url = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + chat + "&text=" + message_text
        requests.get(url)

    else:
        status_admin = Activities.objects.get(status="Активен")

        admin = Admins.objects.filter(activity=status_admin).order_by('?').first()
        if admin:
            chat = admin.number_admin
            url = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + chat + "&text=" + message_text
            requests.get(url)

            ClientAdmin.objects.create(clientId=user_id, adminId=chat)

            unable = Activities.objects.get(status="Неактивен")
            admin.activity = unable
            admin.save()

    return JsonResponse({})


def update_ajax(request):

    bot_token = settings.BOT_TOKEN
    user_id = request.GET.get("user_id")
    response_msg = {"message": ""}
    response = requests.get("https://api.telegram.org/bot" + bot_token + "/getUpdates")
    result = json.loads(response.content.decode('utf-8'))

    id_from_message = result["result"][-1]["message"]["from"]["id"]

    if not Admins.objects.filter(number_admin=id_from_message).exists():
        Admins.objects.create(number_admin=id_from_message)


    id_message = result["result"][-1]["message"]['message_id']
    if not Message.objects.filter(id_message=id_message).exists():

        admin_id = result["result"][-1]["message"]['from']["id"]
        current_admin = Admins.objects.filter(number_admin=admin_id).first()
        if ClientAdmin.objects.filter(clientId=user_id, adminId=current_admin.number_admin).first():

            Message.objects.create(id_message=id_message)
            message_admin = result["result"][-1]["message"]['text']

            if message_admin != "/end":
                response_msg = {"message": message_admin}
            else:
                # Closing the current chat and changing the status for
                # the administrator
                ClientAdmin.objects.get(adminId=current_admin.number_admin).delete()
                status_active = Activities.objects.get(status="Активен")
                current_admin.activity = status_active
                current_admin.save()

    return JsonResponse(response_msg)



