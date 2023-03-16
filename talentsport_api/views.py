import re
from django.http import HttpResponse, JsonResponse
from talentsport_app.models import *
from talentsport_api.serializers import *

def Overview(request):
    return JsonResponse(
        {
            'Liste des joueurs':'api/players'
        }
    )

