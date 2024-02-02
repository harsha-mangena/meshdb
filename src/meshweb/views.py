from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import loader


# Home view
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def index(request):
    template = loader.get_template("meshweb/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
