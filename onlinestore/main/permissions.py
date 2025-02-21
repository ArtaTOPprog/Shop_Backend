from rest_framework import permissions


class Delete_Admin(permissions.BasePermission): # удалять может только админ
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)


class Update_Author(permissions.BasePermission): # класс для того чтобы изменял только тот кто создал
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user