from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIsSuperuserTitleCategoryGenre(BasePermission):
    """
    Предоставление прав доступа для администратора и супер юзера
    на добавление и удаление категорий, жанров и произведений.
    """
    message = 'Доступно только администратору!'

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_admin)


class AuthorOrAdminOrModeratorReviewComment(BasePermission):
    """
    Предоставление прав доступа для авторов, модератора
    и администратора на изменение отзывов и комментариев.
    """
    message = 'Изменение чужого контента запрещено!'

    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or request.user == obj.author)


class IsAdminOrIsSuperuser(BasePermission):
    """Права доступа для админа и суперюзера."""
    message = 'Доступно только администратору!'

    def has_permission(self, request, view):
        return request.user.is_admin
