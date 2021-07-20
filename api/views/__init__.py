from .authentication import confirm_email, get_token
from .category_viewset import CategoryViewSet
from .comment_viewset import CommentViewSet
from .genre_viewset import GenreViewSet
from .review_viewset import ReviewViewSet
from .title_viewset import TitleViewSet
from .user_viewset import UserViewSet

__All__ = [confirm_email, get_token, CategoryViewSet, CommentViewSet,
           GenreViewSet, ReviewViewSet, TitleViewSet, UserViewSet]
