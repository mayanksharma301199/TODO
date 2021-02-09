from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name = 'Home'),
    path('NewTask/<str:UrlValue>', views.NewTask, name = 'NewTask')
    # path('StatusChange/<int:id>', views.StatusChange, name = 'StatusChange'),
    # path('TaskEdit/<int:id>/<str:ChangedContent>', views.TaskEdit, name = 'TaskEdit'),
    # path('TaskDelete/<int:id>', views.TaskDelete, name = 'TaskDelete')

]