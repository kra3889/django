#app level
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.success),

]
