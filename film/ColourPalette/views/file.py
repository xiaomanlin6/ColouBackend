from django.views import View
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
class AvatarView(View):
    def post(self, request):
        res = {
            'code': 412,
            'msg': 'upload error'
        }
        file: InMemoryUploadedFile = request.FILES.get('file')
        request.user.avatar = file
        request.user.save()
        res['code'] = 200
        res['msg'] = 'upload success'
        return JsonResponse(res)


