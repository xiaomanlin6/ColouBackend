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
        user_company = request.data.get('userNation')
        email = request.data.get('email')

        user_query = UserInfo.objects.filter(nid=nid)
        user_query.update(name=user_name, gender=user_gender, company=user_company, email=email)

        res['code'] = 200
        return JsonResponse(res)
