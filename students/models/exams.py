# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
    '''Exam Model'''

    class Meta(object):
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Предмет"
    )

    date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Дата и время"
    )


    exams_group = models.ForeignKey('Group',
                                      verbose_name="Группа",
                                      blank=False,
                                      null=True,
                                      on_delete=models.SET_NULL
                                      )

    teacher = models.ForeignKey('Teacher',
        verbose_name="Преподаватель",
        blank=False,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name="Дополнительные заметки")





    def __str__(self):
        if self.teacher:
            return "%s (%s %s)" % (self.title, self.teacher.first_name, self.teacher.last_name)
        else:
            return "%s" % (self.title,)
