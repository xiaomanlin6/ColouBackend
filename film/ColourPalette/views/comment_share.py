from django.views import View
from django.http import JsonResponse
from app01.models import CommentSharing


class CommentView(View):
    def post(self, request, nid):
        res = {
            'msg': 'success！',
            'code': 412,
            'self': None
        }
        data = request.data
        if not request.user.username:
            res['msg'] = 'please login'
            return JsonResponse(res)
        content = data.get('content')
        if not content:
            res['msg'] = 'placeholder input'
            res['self'] = 'content'
            return JsonResponse(res)
        pid = data.get('pid')

        if pid:
            CommentSharing.objects.create(
                content=content,
                user=request.user,
                sharing_id=nid,
                parent_comment_id=pid
            )

        else:
            CommentSharing.objects.create(
                content=content,
                user=request.user,
                sharing_id=nid
            )

        res['code'] = 200
        return JsonResponse(res)
