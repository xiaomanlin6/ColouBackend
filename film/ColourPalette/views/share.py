from django.views import View
from django.http import JsonResponse
from app01.models import Sharing

class ShareView(View):
    def post(self, request):
        res = {
            'code': 412,
            'msg': 'success！'
        }
        title = request.data.get('title')
        content = request.data.get('content')

        Sharing.objects.create(title=title, content=content, user=request.user)

        res['code'] = 200
        return JsonResponse(res)
