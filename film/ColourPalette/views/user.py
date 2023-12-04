from django import forms
from django.contrib import auth
from django.views import View
from django.http import JsonResponse
from app01.models import UserInfo


class UserSetupView(View):
#Update User information when first time login
    def put(self, request):
        res = {
            'code': 600,
            'msg': 'Profile Update Successfully'
        }
        nid = request.data.get('nid')
        user_name = request.data.get('userName')
        user_gender = request.data.get('userGender')
        user_company = request.data.get('userCompany')
        email = request.data.get('email')

        user_query = UserInfo.objects.filter(nid=nid)
        user_query.update(name=user_name, gender=user_gender, company=user_company, email=email)

        res['code'] = 200
        return JsonResponse(res)

class EditPasswordForm(forms.Form):
    pwd = forms.CharField(min_length=6, error_messages={'required': 'Invalid Update', 'min_length': 'Pass should be longer than 6 digits'})
    re_pwd = forms.CharField(min_length=6, error_messages={'required': 'confirm password', 'min_length': 'Pass should be longer than 6 digits'})

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd != re_pwd:
            self.add_error('re_pwd', 'confirm password error')
        return self.cleaned_data

def clean_form(form):
    err_dict: dict = form.errors
    err_valid = list(err_dict.keys())[0]
    err_msg = err_dict[err_valid][0]
    return err_valid, err_msg


class EditPasswordView(View):
    def post(self, request):
        res = {
            "msg": 'success！',
            'self': None,
            'code': 412,
        }
        data = request.data
        form = EditPasswordForm(data, request=request)
        if not form.is_valid():
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)
        username = request.data.get('username')
        user = UserInfo.objects.filter(username=username).first()
        maiden_name = request.data.get('maidenName')
        friend_name = request.data.get('friendName')
        if user.maiden_name != maiden_name or user.friend_name != friend_name:
            res['msg'] = 'question is error'
            return JsonResponse(res)
        user.set_password(data['pwd'])
        user.save()
        auth.logout(request)

        res['code'] = 0
        return JsonResponse(res)
