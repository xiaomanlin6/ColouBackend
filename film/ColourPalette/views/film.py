from django.db.models import F
from django.http import JsonResponse
from django.views import View
from app01.models import Color


class ArticleDiggView(View):
    def post(self, request, nid):
        status = {
            'code': 400,
            'msg': 'Liked',# custom status code 400 to Comment Successfully
            'isDigg': True,
            'data': 0
        }

        if not request.user.username:
            status['msg'] = 'Please log in first'
            return JsonResponse(status)
        status['code'] = 0

        is_liked = request.user.digg_film.filter(nid=nid)
        num = 1
        if is_liked:
            request.user.digg_film.remove(nid) #remove the liked palette from the user
            num = -1
            status['msg'] = 'Cancel Like'
            status['isDigg'] = False
        else:
            request.user.digg_film.add(nid)

        film_query = Color.objects.filter(nid=nid)
        film_query.update(digg_count=F('digg_count') + num)
        #F('digg_count') represents the current value of the digg_count field in the records that match the queryset.
        digg_count = film_query.first().digg_count
        status['data'] = digg_count
        return JsonResponse(status)


class FilmView(View):
    def get(self, request):
        status = {
            'code': 500,
            'msg': 'success', #custom status code 500 to success get
            'data': [],
        }
        name = request.GET.get('name')
        sort = request.GET.get('sort')
        film = Color.objects.filter(content__contains=name)
        if sort:
            film = film.order_by(f'-{sort}')

        for IndividualFilm in film:
            status['data'].append({
                'nid': IndividualFilm.nid,
                'title': IndividualFilm.title,
                'username': IndividualFilm.user.username,
                'digg_count': IndividualFilm.digg_count,
                'comment_count': IndividualFilm.comment_count,
                'create_time': str(IndividualFilm.create_time),
            })

        status['code'] = 200
        return JsonResponse(status)

    def post(self, request):
        res = {
            'code': 600,
            'msg': 'success',#custom status code 600 to success post
            'data': {}
        }
        colorResult = request.data.get('colorResult')
        Color.objects.create(content=colorResult, title='Palette', user=request.user)
        return JsonResponse(res)
