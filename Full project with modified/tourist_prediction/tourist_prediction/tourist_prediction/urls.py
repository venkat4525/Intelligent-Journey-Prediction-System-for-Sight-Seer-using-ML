"""tourist_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from admins import views as admins_views
from customer import views as customer_views
from tourist_prediction import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',customer_views.loginform, name='loginform'),
    url(r'^registerform$',customer_views.registerform, name='registerform'),
    url(r'^mydetails',customer_views.mydetails, name='mydetails'),
    url(r'^viewtou',customer_views.viewtou, name='viewtou'),
    url(r'^search_touristplace',customer_views.search_touristplace, name='search_touristplace'),
    url(r'^feedback',customer_views.feedback, name='feedback'),
    url(r'^quiz',customer_views.quiz, name='quiz'),
    url(r'^view_prediction/(?P<pk>\d+)/$', customer_views.view_prediction, name="view_prediction"),
    url(r'^bking/(?P<pp>\d+)/$', customer_views.bking, name="bking"),
    url(r'^graph/(?P<grpchart_type>\w+)$',customer_views.graph,name="graph"),

    url('admin_loginpage/$', admins_views.admin_loginpage, name='admin_loginpage'),
    url('view_user_details/$', admins_views.view_user_details, name='view_user_details'),
    url('upload_tourist/$', admins_views.upload_tourist, name='upload_tourist'),
    url('view_feedback/$', admins_views.view_feedback, name='view_feedback'),
    url('cusbooking/$', admins_views.cusbooking, name='cusbooking'),
    url('view_tourist/$', admins_views.view_tourist, name='view_tourist'),
    url(r'^tourist/(?P<chart_type>\w+)$',admins_views.tourist,name="tourist"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
