from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import (Category, Comment, CustomUser, EmailAndCode, Genre,
                        Review, Title)


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        allow_blank=False,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        exclude = ['id']


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        allow_blank=False,
        validators=[UniqueValidator(queryset=Genre.objects.all())]
    )

    class Meta:
        model = Genre
        exclude = ['id']


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'bio', 'email', 'role']


class GetTokenSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)
    expire_date = serializers.DateTimeField(required=False)

    def validate(self, data):
        email = data['email']
        confirm_code = data['confirmation_code']
        if not EmailAndCode.objects.filter(
                email=email, confirm_code=confirm_code).exists():
            raise serializers.ValidationError(
                'Invalid email or confirmation code')
        return data

    class Meta:
        model = EmailAndCode
        fields = ['email', 'confirmation_code', 'expire_date']


class ConfirmEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    confirm_code = serializers.CharField(required=False)
    expire_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        email = validated_data.get('email')
        try:
            instance = EmailAndCode.objects.get(email=email)
            return self.update(instance, validated_data)
        except ObjectDoesNotExist:
            return EmailAndCode.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.confirm_code = validated_data.get(
            'confirm_code')
        instance.expire_date = validated_data.get(
            'expire_date')
        instance.save()
        return instance

    class Meta:
        model = EmailAndCode
        fields = ['email', 'confirm_code', 'expire_date']


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    def validate(self, attrs):
        if not self.context['request'].method == 'POST':
            return attrs
        author = self.context['request'].user
        title = self.context['request'].parser_context['view'].kwargs.get(
            'title_id')
        if Review.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                'You can write only one review to this title.'
            )
        return attrs

    class Meta:
        model = Review
        fields = (
            'id', 'text', 'author', 'title', 'score', 'pub_date'
        )
        unique_together = ('author', 'title')

        extra_kwargs = {
            'title_id': {
                'validators': [
                    UniqueValidator(queryset=CustomUser.objects.all())
                ]
            },
            'author': {
                'validators': [
                    UniqueValidator(queryset=CustomUser.objects.all())
                ]
            },
        }


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
