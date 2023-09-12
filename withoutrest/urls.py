"""
URL configuration for withoutrest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api', views.emp_data_view),
    # path('apijson', views.emp_data_json_view),
    # path('jsonresponseapi', views.emp_data_jsonresponse_view),
    # # path('jsoncbv', views.JsonCBV.as_view()),
    # path('jsoncbv2', views.JsonCBV2.as_view()),

    path('employeejsonview/<int:id>', views.EmployeeDetailsCBV.as_view()),
    path('allemployeejsonview', views.EmployeeListCBV.as_view())


]
