from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
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
    subject_name = get_object_or_404(Subject, id=subject_id).subject_name
    theorem_list = list(Theorem.objects.filter( subject_id__exact=subject_id))
    theorem_list.sort(key=lambda x:x.theorem_name)
    context = {
                  'subject_name': subject_name,
                  'theorems':theorem_list
              }
    return render(request,'theorems/subject_theorems.html',context)

def subject_definitions(request, subject_id):
    subject_name = get_object_or_404(Subject, id=subject_id).subject_name
    definition_list = list(Definition.objects.filter(subject_id__exact=subject_id))
    definition_list.sort(key=lambda x: x.definition_name)
    context = {
                  'subject_name': subject_name,
                  'definitions': definition_list
              }
    return render(request,'theorems/subject_definitions.html',context)

def theorems(request):
    theorem_list = Theorem.objects.order_by(Lower('theorem_name').asc())
    context = {
                  'theorems':theorem_list
              }
    return render(request,'theorems/theorems.html',context)

def theorem_proof(request,theorem_id,proof_num):
    rpp = 1
    theorem = get_object_or_404(Theorem,id=theorem_id)
    proof_list = theorem.theorem_proof_set.order_by('id')
    paginator = Paginator(proof_list, rpp ,orphans=0 ,allow_empty_first_page=True)
    page = proof_num
    try:    
        proofs = paginator.page(page)
    except PageNotAnInteger:
        return redirect('theorem:theorem_proof',theorem_id=theorem_id,proof_num=1,permanent=True) # redirect to first page
    except EmptyPage:
        return redirect('theorem:theorem_proof',theorem_id=theorem_id,proof_num=paginator.num_pages,permanent=True) # show last page
    context = {
                  'theorem_id': theorem.id,
                  'theorem_name': theorem.theorem_name,
                  'theorem_statement': theorem.theorem_statement.theorem_statement,
                  'proofs':proofs
              }
    return render(request,'theorems/theorem_proof.html',context)

def definitions(request):
    definition_list = Definition.objects.order_by(Lower('definition_name').asc())
    context = {
                  'definitions':definition_list
              }
    return render(request,'theorems/definitions.html',context)

def questions(request,page_num):
    rpp = 3
    question_list = Question.objects.order_by('id')
    paginator = Paginator(question_list, rpp ,orphans=0 ,allow_empty_first_page=True)
    page = page_num
    try:    
        quests = paginator.page(page)
    except PageNotAnInteger:
        return redirect('theorem:questions',page_num=1,permanent=True) # redirect to first page
    except EmptyPage:
        return redirect('theorem:questions',page_num=paginator.num_pages,permanent=True) # show last page
    context = {
                  'questions':quests
              }
    return render(request,'theorems/questions.html',context)
