from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    # 登录验证中间件
    while_list =[
        '/api/user/vcode/fetch',
        'api/user/vcode/submit',

    ]
    def process_request(self, request):
       if request.path in self.while_list:
           return
       uid = request.session.get('uid')
       if not uid:
           return JsonResponse({'code':1002,'data':'用户未登录'})
