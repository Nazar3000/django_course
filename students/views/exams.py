# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..models import Exam
from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger


# Views for Exams

def exams_list(request):
    exams = Exam.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'date', 'student_group', 'teacher'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    # set nomber on page

    number_on_page = request.GET.get('number_on_page')
    if number_on_page < 1:
        number_on_page = 1

    loading_step = 1

    # paginate students
    paginator = Pagination(exams, number_on_page, loading_step)
    # paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exams = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g 9999), deliver last page of resoult
        exams = paginator.page(paginator.num_pages)

    return render(request,'students/exams.html',
                  {'exams':exams})


# def exams_add(request):
#     return HttpResponse('<h1>s Add Form</h1>')
#
# def groups_edit(request, gid):
#     return HttpResponse('<h1>Edit Groups %s</h1>' %gid)
#
# def groups_delete(request, gid):
#     return HttpResponse('<h1> Delete Group %s</h1>' %gid)