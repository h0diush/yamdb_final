import datetime as dt

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api.models import CustomUser, EmailAndCode
from api.serializers import GetTokenSerializer, ConfirmEmailSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    EmailAndCode.objects.filter(expire_date__lte=timezone.now()).delete()
    serializer = GetTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    conf_code = serializer.validated_data.get('confirmation_code')
    EmailAndCode.objects.filter(email=email, confirm_code=conf_code).delete()
    user = get_object_or_404(CustomUser, email=email)
    token = AccessToken.for_user(user)
    return Response({'token': str(token)},
                    status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def confirm_email(request):
    """Send an email with confirmation code to a passed email address."""
    EmailAndCode.objects.filter(expire_date__lte=timezone.now()).delete()
    serializer = ConfirmEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    user = get_object_or_404(CustomUser, email=email)
    conf_code = CustomUser.objects.make_random_password(length=16)
    expr_date = timezone.now() + dt.timedelta(minutes=5)
    user.email_user(
        'Email confirmation',
        f'Your confirmation code: {conf_code}')
    serializer.save(confirm_code=conf_code, expire_date=expr_date)
    return Response(data={'email': email}, status=status.HTTP_200_OK)
