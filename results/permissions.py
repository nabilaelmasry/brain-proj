from rest_framework import permissions

class ResultUserOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.result_user == request.user

class ResultUserReadDeleteOrAdminUpdate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' or request.method == 'PATCH':
            return bool(request.user and request.user.is_staff)
        else:
            return obj.result_user == request.user or request.user.is_staff
