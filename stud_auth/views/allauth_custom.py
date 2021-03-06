from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Fieldset, Button
from allauth.account.forms import LoginForm as LoginFormAllauth
from allauth.account.forms import UserForm as UserFormAllauth
from allauth.account.forms import SignupForm as SignupFormAllauth
from allauth.account.forms import ResetPasswordForm as ResetPasswordFormAllauth
from allauth.account.forms import ChangePasswordForm as ChangePasswordFormAllauth
from allauth.account.views import LoginView as LoginViewAllauth
from allauth.account.views import SignupView as SignupViewAllauth
from allauth.account.views import PasswordResetView as PasswordResetViewAllauth
from allauth.account.views import PasswordChangeView as PasswordChangeViewAllauth


from django.utils.translation import ugettext as _
from django.urls import reverse_lazy



class LoginFormCrispy(LoginFormAllauth):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super().__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('login')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-2'
        self.helper.layout = Layout(Fieldset(
            _('Login'),
            'login',

            'password',
            HTML('<a href="{% url "pass_reset_allauth" %}">Reset Password</a>'),
        ))

        # form buttons
        self.helper.add_input(Submit('send_button', _('Login')))
        # self.helper.add_input(Submit('cancel_button', u'Отмена'))



class LoginFormView(LoginViewAllauth):
    template_name = 'crispy_registration.html'
    form_class = LoginFormCrispy


class SignupFormCrispy(SignupFormAllauth):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super().__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('login')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-2'
        # self.helper.layout = Layout(Fieldset(
        #     _('Login'),
        #     'username',
        #     'password'
        # ))

        # form buttons
        self.helper.add_input(Submit('send_button', _('Login')))
        # self.helper.add_input(Submit('cancel_button', u'Отмена'))

class SignupView(SignupViewAllauth):
    template_name = 'crispy_registration.html'
    form_class = SignupFormCrispy
    # success_url = reverse_lazy('home')
    # redirect_field_name = 'home'

class PasswordResetForm(ResetPasswordFormAllauth):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super().__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('login')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-2'
        # self.helper.layout = Layout(Fieldset(

        # ))

        # form buttons
        self.helper.add_input(Submit('send_button', _('Reset')))


class PasswordResetView(PasswordResetViewAllauth):
    template_name = 'crispy_registration.html'
    form_class = PasswordResetForm


class PasswordChangeForm(ChangePasswordFormAllauth):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super().__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('login')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.lable_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-2'
        # self.helper.layout = Layout(Fieldset(
        #     _('Login'),
        #     'login',
        #
        #     'password',
        #     HTML('<a href="{% url "pass_reset_allauth" %}">Reset Password</a>'),
        # ))

        # form buttons
        self.helper.add_input(Submit('send_button', _('Change Password')))

class PasswordChangeView(PasswordChangeViewAllauth):
    template_name = 'crispy_registration.html'
    form_class = PasswordChangeForm

