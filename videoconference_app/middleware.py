from django.utils.deprecation import MiddlewareMixin

class ActiveUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            active_users = request.session.get('active_users', set())
            if request.user.id not in active_users:
                active_users.add(request.user.id)
            request.session['active_users'] = list(active_users)

    def process_response(self, request, response):
        if request.user.is_authenticated:
            active_users = request.session.get('active_users', set())
            if request.user.id not in active_users:
                active_users.add(request.user.id)
            request.session['active_users'] = list(active_users)
        return response
