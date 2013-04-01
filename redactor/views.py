import json

from django.http import HttpResponse
from django.views.decorators.http import require_POST

from models import File


@require_POST
def upload_photos(request):
    images = [{
        "filelink": File.objects.create(upload=f, is_image=True).upload.url,
    } for f in request.FILES.getlist("file")]
    return HttpResponse(json.dumps(images), mimetype="application/json")


def recent_photos(request):
    images = [{
        "thumb": obj.upload.url,
        "image": obj.upload.url,
    } for obj in File.objects.filter(is_image=True).order_by("-date_created")[:20]]
    return HttpResponse(json.dumps(images), mimetype="application/json")
