from django.views import View
from django.http import JsonResponse
from app01.models import Comment, Color


class CommentView(View):
    def post(self, request, nid):
        res = {
            'code': 300,
            'msg': 'Comment Successfully' # custom status code 300 to Comment Successfully
        }
        data = request.data
        content = data.get('comment_content')
        if not content:
            res['msg'] = 'Please enter your comment'
            return JsonResponse(res)

        Comment.objects.create(
                color_id=nid,
                content=content,
                user=request.user
            )
        color_obj = Color.objects.filter(nid=nid).first()
        #.first() is used to retrieve the first record that matches the filter criteria
        color_obj.comment_count += 1
        color_obj.save()
        res['code'] = 0
        return JsonResponse(res)
