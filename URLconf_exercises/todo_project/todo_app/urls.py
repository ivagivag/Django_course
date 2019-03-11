from django.urls import path
from django.urls import re_path


from . import views


urlpatterns = [
	# 127.0.0.1:8000/todoss
	# path('', views.index),

	# http://127.0.0.1:8000/todos/list_1
  re_path(r'^list(_(?P<taskn>\d+)/)?$', views.list_all),

	# http://127.0.0.1:8000/todos/list/2018/02
  # re_path(r'^list/(?P<year>\d+)*/(?P<month>\d+)*/$', views.list_part),
  re_path(r'^list/(?P<year>\d{4})/((?P<month>\d{2})/)?$', views.list_part),
  
  # http://127.0.0.1:8000/todos/table
  # path('table/', views.table),

  # http://127.0.0.1:8000/todos/delete/1
  path('delete/<int:id>', views.delete),
  # re_path('delete/<int:id>', views.delete),
]
# r'^comments/(?:page-(?P<page_number>\d+)/)?$'