from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite métodos GET, HEAD e OPTIONS para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Verifica se o usuário está autenticado e pertence ao grupo "admin"
        return request.user.is_authenticated and request.user.groups.filter(name='admin').exists()

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
        # Verifica se o usuário está autenticado e pertence ao grupo "admin"
            return request.user.is_authenticated
