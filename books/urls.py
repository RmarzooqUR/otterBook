from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.APISpec.as_view(), name='api_spec'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('upvote/<int:pk>/', views.UpvoteView.as_view(), name='upvote'),
    path('comment/<int:pk>/', views.CommentView.as_view(), name='comment'),
]
