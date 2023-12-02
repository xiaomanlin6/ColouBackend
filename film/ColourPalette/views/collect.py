from django.views import View
from django.http import JsonResponse
from app01.models import Collect


class CollectView(View):
    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success'
        }
        nid = request.data.get('nid')
        collect_obj = Collect.objects.filter(color_id=nid, user=request.user)
        if collect_obj:
            res['code'] = 500,
            res['msg'] = 'please do not collect simaple color item'
            return JsonResponse(res)
        Collect.objects.create(color_id=nid, user=request.user)
        return JsonResponse(res)

    def get(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': []
        }
        collect_obj = Collect.objects.filter(user=request.user).all()
        for collect in collect_obj:
            res['data'].append({
                'nid': collect.nid,
                'color_id': collect.color.nid,
                'username': collect.user.username,
                'color': collect.color.title,
                'create_date': str(collect.create_time)[:10]
            })
        return JsonResponse(res)