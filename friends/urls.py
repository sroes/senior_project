from django.urls import path, re_path


from .views import (
	friends, 
	profile_view, 
	send_friend_request, 
	cancel_friend_request,
	accept_friend_request,
	delete_friend_request
	)

urlpatterns = [
    path('', friends, name='friends'),
    path(r'^(?P<slug>[\w-]+)/$', profile_view),
    path(r'^friend-request/send/(?P<id>[\w-]+)/$', send_friend_request),
    path(r'^friend-request/cancel/(?P<id>[\w-]+)/$', cancel_friend_request),
    path(r'^friend-request/accept/(?P<id>[\w-]+)/$', accept_friend_request),
    path(r'^friend-request/delete/(?P<id>[\w-]+)/$', delete_friend_request),
]
