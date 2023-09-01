from django.urls import path,re_path
from cloneApp import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    re_path(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    re_path(r'post/(?P<pk>\d+)/edit/$',views.UpdatePostView.as_view(),name='post_edit'),
    re_path(r'post/(?P<pk>\d+)/remove/$',views.postDeleteView.as_view(),name='post_remove'),
    path('drafts',views.draftListView.as_view(),name='post_draft_list'),
    re_path(r'post/(?P<pk>\d+)/comment/$',views.add_comments_to_post,name='add_comments_to_post'),
    re_path(r'comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    re_path(r'comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    re_path(r'post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
    
]