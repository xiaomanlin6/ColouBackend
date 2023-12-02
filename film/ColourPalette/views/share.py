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
<<<<<<< HEAD
=======

    def get(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': []
        }
        
        share_list = Sharing.objects.all()
        for share in share_list:
            res['data'].append({
                'nid': share.nid,
                'title': share.title,
                'username': share.user.username,
                'create_date': str(share.create_date)[:10]
            })
        return JsonResponse(res)
>>>>>>> 5270947da5fb8bfa8f1ed3f2d841d02f6ea432be
