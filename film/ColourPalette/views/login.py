from django import forms
from django.contrib import auth
from app01.models import UserInfo
from django.views import View
from django.http import JsonResponse


class LoginBaseForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Please Enter Username'})
    password = forms.CharField(error_messages={'required': 'Please Enter Password'})

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)


class LoginForm(LoginBaseForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)

        if not user:
            self.add_error('password', 'Wrong User name or password!')
            return self.cleaned_data
        self.cleaned_data['user'] = user
        return self.cleaned_data


# Authenticate Users
# Reference:https://docs.djangoproject.com/en/4.2/topics/auth/default/
# Cleaned Data: remove the relevant field form
# Reference: https://docs.djangoproject.com/en/4.2/ref/forms/api/
class SignForm(LoginBaseForm):
    re_password = forms.CharField(error_messages={'required': 'Please confirm your password'})

    # Check if the username exists
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_query = UserInfo.objects.filter(username=username)
        if user_query:
            self.add_error('username', 'User Exists')
        return self.cleaned_data

    # Check if the password are same
    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if not re_password:
            self.add_error('re_password', 'You must confirm your password')
        if password != re_password:
            self.add_error('re_password', 'Password not same')
        return self.cleaned_data


def clean_form(form):
    err_dict: dict = form.errors  # returns a dict that maps fields to the errors
    err_valid = list(err_dict.keys())[0]
    err_msg = err_dict[err_valid][0]
    return err_valid, err_msg


# Form.errors
# Reference: https://docs.djangoproject.com/en/4.2/ref/forms/api/


class LoginView(View):
    def post(self, request):
        response = {
            'code': 100,
            'msg': 'You are Logged in',  # custom status code 100 to You are logged in
            'self': None
        }
        form = LoginForm(request.data, request=request)
        if not form.is_valid():
            response['self'], response['msg'] = clean_form(form)  # assign error message
            return JsonResponse(response)
        # Login
        user = form.cleaned_data.get('user')
        auth.login(request, user)
        response['code'] = 0  # all tests pass
        return JsonResponse(response)


class SignView(View):
    def post(self, request):
        response = {
            'code': 200,
            'msg': 'You are Registered!',  # custom status code 200 to You are logged in
            'self': None
        }
        form = SignForm(request.data, request=request)
        if not form.is_valid():
            response['self'], response['msg'] = clean_form(form)
            return JsonResponse(response)
        email = request.data.get('email')
        if not email:
            response['msg'] = 'placeholder email'
            return JsonResponse(response)
        maiden_name = request.data.get('maidenName')
        friend_name = request.data.get('friendName')
        user = UserInfo.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        user.email = email
        user.maiden_name = maiden_name
        user.friend_name = friend_name
        user.save()
        auth.login(request, user)
        response['code'] = 0
        return JsonResponse(response)
