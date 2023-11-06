from django.views import View
from django.http import JsonResponse


class RetrieveView(View):
    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success'
        }
        email = request.data.get('email')
        new_password = request.data.get('newPassword')
        if email != request.user.email:
            res['code'] = 500
            res['msg'] = 'placeholder correct email'
            return JsonResponse(res)
        request.user.set_password(new_password)
        request.user.save()
        return JsonResponse(res)