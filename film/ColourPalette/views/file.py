from django.views import View
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.core.files import File

class AvatarView(View):
    def post(self, request):
        res = {
            'code': 412,
            'msg': 'upload error'
        }
        file: InMemoryUploadedFile = request.FILES.get('file')
        if file:
            request.user.avatar = file
            request.user.save()
            res['code'] = 200
            res['msg'] = 'upload success'
        else:
            # Set default avatar
            default_avatar_path = settings.MEDIA_ROOT + '/default_avatar.jpg'
            with open(default_avatar_path, 'rb') as default_avatar_file:
                request.user.avatar.save('default_avatar.jpg', File(default_avatar_file), save=True)
            res['code'] = 200
            res['msg'] = 'default avatar set'

        return JsonResponse(res)
