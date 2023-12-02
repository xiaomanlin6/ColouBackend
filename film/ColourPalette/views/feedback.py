from django.views import View
from django.http import JsonResponse
from app01.models import FeedBack


class FeedbackView(View):
    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success'
        }

        content = request.data.get('content')
        FeedBack.objects.create(user=request.user, content=content)
        return JsonResponse(res)