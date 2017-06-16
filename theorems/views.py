from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.db.models.functions import Lower
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from random import randint
from .models import Question
from .models import Subject
from .models import Theorem
from .models import Theorem_Statement
from .models import Theorem_Proof
from .models import Definition
from .models import Proof_Definition_Link
from .models import Keyword
from .models import Theorem_Keyword_Link
# Create your views here.

def index(request):
    questions_list = Question.objects.all().order_by('id')
    row = randint(0,len(questions_list)-1)
    question = questions_list[row]
    context = {
               'question':question,
               'question_num': row + 1
              }
    return render(request,'theorems/index.html',context)

def subjects(request):
    subjects_list = Subject.objects.order_by(Lower('subject_name').asc())
    if request.GET and 'id' in request.GET:
        subject_id = request.GET['id']   # don't need to check if subject_id == '' or none because I'm using get_object_or_404 
        specific_subject = get_object_or_404(subjects_list,id=subject_id)
        try:
            specific_subject_index = list(subjects_list).index(specific_subject) + 1
        except ValueError:
            specific_subject_index = None
    else:
        specific_subject = None
        specific_subject_index = None
    context = {
                  'specific_subject_index': specific_subject_index,
                  'specific_subject': specific_subject,
                  'subjects':subjects_list
              }
    return render(request,'theorems/subjects.html',context)
        

def subject_theorems(request, subject_id):
    rpp = 10  #rpp = results per page
    theorem_list = list(Theorem.objects.filter( subject_id__exact=subject_id))
    theorem_list.sort(key=lambda x:x.theorem_name)
    paginator = Paginator(theorem_list, rpp ,orphans=4 ,allow_empty_first_page=True)
    page = request.GET.get('page')
    try:    
        thrms = paginator.page(page)
    except PageNotAnInteger:
        thrms = paginator.page(1) #show first page
    except EmptyPage:
        thrms = paginator.page(paginator.num_pages) #show last page
    context = {
                  'subject_name': get_object_or_404(Subject, id=subject_id).subject_name,
                  'theorems':thrms
              }
    return render(request,'theorems/subject_theorems.html',context)

def subject_definitions(request, subject_id):
    rpp = 10  #rpp = results per page
    definition_list = list(Definition.objects.filter(subject_id__exact=subject_id))
    definition_list.sort(key=lambda x: x.definition_name)    
    paginator = Paginator(definition_list, rpp ,orphans=4 ,allow_empty_first_page=True)
    page = request.GET.get('page')
    try:    
        defs = paginator.page(page)
    except PageNotAnInteger:
        defs = paginator.page(1) #show first page
    except EmptyPage:
        defs = paginator.page(paginator.num_pages) #show last page
    context = {
                  'subject_name': get_object_or_404(Subject, id=subject_id).subject_name,
                  'definitions': defs
              }
    return render(request,'theorems/subject_definitions.html',context)

def theorems(request):
    rpp = 10  #rpp = results per page
    theorem_list = Theorem.objects.order_by(Lower('theorem_name').asc())
    paginator = Paginator(theorem_list, rpp ,orphans=4 ,allow_empty_first_page=True)
    page = request.GET.get('page')
    try:    
        thrms = paginator.page(page)
    except PageNotAnInteger:
        thrms = paginator.page(1) #show first page
    except EmptyPage:
        thrms = paginator.page(paginator.num_pages) #show last page
    context = {
                  'theorems':thrms
              }
    return render(request,'theorems/theorems.html',context)

def theorem_proof(request,theorem_id):
    rpp = 1  #rpp = results per page
    proof_list = Theorem_Proof.objects.filter(theorem_id__exact=theorem_id).order_by('id')
    theorem = Theorem.objects.get(id=theorem_id)
    paginator = Paginator(proof_list, rpp ,orphans=0 ,allow_empty_first_page=True)
    page = request.GET.get('page')
    try:    
        proofs = paginator.page(page)
    except PageNotAnInteger:
        proofs = paginator.page(1) #show first page
    except EmptyPage:
        proofs = paginator.page(paginator.num_pages) #show last page
    context = {
                  'theorem_name': theorem.theorem_name,
                  'theorem_statement': theorem.theorem_statement.theorem_statement,
                  'proofs':proofs
              }
    return render(request,'theorems/theorem_proof.html',context)

def definitions(request):
    rpp = 10  #rpp = results per page
    definition_list = Definition.objects.order_by(Lower('definition_name').asc())
    paginator = Paginator(definition_list, rpp ,orphans=4 ,allow_empty_first_page=True)
    page = request.GET.get('page')
    try:    
        defs= paginator.page(page)
    except PageNotAnInteger:
        defs = paginator.page(1) #show first page
    except EmptyPage:
        defs = paginator.page(paginator.num_pages) #show last page
    context = {
                  'definitions':defs
              }
    return render(request,'theorems/definitions.html',context)

def definition(request,definition_id):
    return HttpResponse("""You're looking at definition %s""" % definition_id)

def questions(request):
    return HttpResponse("""You're looking at all the questions on page %s""" % 1)

def question(request, question_id):
    return HttpResponse("""You're looking at question %s""" % question_id)
