from django.conf.urls import url
from . import views

app_name = 'theorems'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # subjects
    url(r'^subjects/$', views.subjects, name='subjects'),
    url(r'^subjects/(?P<subject_id>[1-9]*([0-9]+))/theorems/$',views.subject_theorems, name='subject_theorems'),
    url(r'^subjects/(?P<subject_id>[1-9]*([0-9]+))/definitions/$',views.subject_definitions, name='subject_definitions'),
    #theorems
    url(r'^theorems/$', views.theorems, name='theorems'),
    url(r'^theorems/(?P<theorem_id>[1-9]*([0-9]+))/$', views.theorem_proof, name='theorem_proof'),
    #definitions
    url(r'^definitions/$', views.definitions, name='definitions'),
    url(r'^definitions/(?P<definition_id>[1-9]*([0-9]+))/$', views.definition, name='definition'),

    #questions
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^questions/(?P<question_id>[1-9]*([0-9]+))/$', views.question, name='question')
]

