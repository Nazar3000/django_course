# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views.generic.edit import FormView
import logging
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from abc import abstractmethod, ABCMeta
from django.utils.translation import ugettext as _







class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super().__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Отправить'))


# Поля самой формы
    from_email = forms.EmailField(
    label=u"Ваш Емейл Адрес")

    subject = forms.CharField(
        label=u"Оглавдение письма",
        max_length=128)

    message = forms.CharField(
        label=u"Текст сообщения",
        max_length=2560,
        widget=forms.Textarea)


class PremissionRequiredClass(FormView):
    __metaclass__ = ABCMeta

    # @abstractmethod
    @method_decorator(permission_required('auth.add_user'))
    def dispatch(self, *args, **kwargs):
        return super(PremissionRequiredClass, self).dispatch(*args, **kwargs)


class ContactView(PremissionRequiredClass):
    template_name = 'contact_admin/form.html'
    form_class = ContactForm
    # success_url = '/email-sent/'

    # @method_decorator(permission_required('auth.add_user'))
    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']

        send_mail(subject, message, from_email, [ADMIN_EMAIL])

        return super().form_valid(form)


    def get_success_url(self):
        return '%s?status_message=%s' % (reverse('home'), _("Email sent successfully"))



# Ограничение прав для пользователей
# @permission_required('auth.add_user')
# def contact_admin(request):
#     # check if form was posted
#     if request.method =='POST':
#        # create a form instance and populate it with data from the request:
#
#         form = ContactForm(request.POST)
#         # check whether user data is valid:
#
#         if form.is_valid():
#             # send email
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             from_email = form.cleaned_data['from_email']
#             try:
#                 send_mail(subject, message, from_email, [ADMIN_EMAIL])
#             except Exception:
#                 message = u'Во время отправки письма возникла ошибка. Попробуйте позже sand_email: subject:%s, message:%s, from_email:%s, ADMIN_EMAIL:%s '% (subject, message, from_email, ADMIN_EMAIL)
#                 logger = logging.getLogger(__name__)
#                 logger.exception(message)
#             else:
#                 message = u'Сообщение отправлено'
#             # redirect to same contact page with success message
#             return HttpResponseRedirect(
#             u'%s?status_message=%s' % (reverse('contact_admin'), message))
#
#             # if there was not POST render blank from
#     else:
#         form = ContactForm()
#     return render(request, 'contact_admin/form.html', {'form': form})