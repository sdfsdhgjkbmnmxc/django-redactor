from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^do-photos-upload/$', views.upload_photos, name="upload_photos"),
    url(r'^do-photos-recent/$', views.recent_photos, name="recent_photos")
)
