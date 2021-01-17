from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    # url(r'^$', views.welcome, name = 'welcome'),
    url(r'^$', views.index, name = 'index'),
    url(r'^new/upload$',views.uploadproject,name = 'upload'),
    url(r'^new/profile$', views.addprofile, name='edit'),
    url(r'^myprofile$',views.userprofile,name ='myprofile'),
    url(r'^oneproject/(\d+)$', views.one_project, name='oneproject'),
    url(r'^search/$', views.search_project, name='search'),
    url(r'^comment/(\d+)/$', views.add_comment, name='comment'),
    url(r'^view_comment/(\d+)/$', views.comment, name='view'),
    url(r'^api/profile/$', views.ProfileList.as_view(), name='profile'),
    url(r'^api/project/$', views.ProjectList.as_view(), name='project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)