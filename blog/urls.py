from django.urls import path
from .import views
urlpatterns = [
    path('blogs',views.blog_list,name='blog_list'),
    path('blog/<slug:slug>/',views.blog_detail,name='blog_detail'),
    path('create/',views.create_blog,name='create_blog'),
    path('edit/<slug:slug>/',views.edit_blog,name='edit_blog'),
    path('del/<slug:slug>/',views.del_blog,name='del_blog'),
    path('profile/',views.page_profile,name='page_profile'),

]
