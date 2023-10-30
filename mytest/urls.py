from django.urls import path, re_path
from .views import test_view, open_folder

from django.http import HttpResponse


# #direct, simple way
def test_home(request):
    return HttpResponse('Hello my test Word!')

urlpatterns = [
    path('', test_home, name='test_home'),
    path('test/', test_view, name='test'),
    re_path(r'^open_folder/(?P<folder_path>.+)/$', open_folder, name='open_folder'),
]
