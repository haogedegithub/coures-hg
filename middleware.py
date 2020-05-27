from django.utils.deprecation import MiddlewareMixin
from course import views as course_views
from django.shortcuts import reverse
class MyMiddleware(MiddlewareMixin):
    def __init__(self,get_response=None):
        super().__init__(get_response)
        # 初始化中间件
        print('init_mymiddleware')

    def process_request(self,request):
        # request.context = {}
        # if 'session_user' in request.session.keys():
        #     request.context['session_user'] = request.session['session_user']
        request.context = dict(
            session_user = request.session['session_user'] if 'session_user' in request.session.keys() else None
        )

        if (not request.context['session_user'])\
                and (request.path.startwith('/video') or request.path.startwith('/user'))\
                and request.path not in [reverse('user_login'),reverse('user_register')]:
            request.context['login_message'] = '请先登录'
            return course_views.index_handler(request)


    def process_response(self,request,response):
        # 必须return response
        print('process_response')
        return response


