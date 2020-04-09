from djoser.serializers import TokenSerializer
from rest_framework import serializers
from djoser.conf import settings as djoser_settings
from stream_chat import StreamChat
from django.conf import settings


class StreamTokenSerializer(TokenSerializer):
    stream_token = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = djoser_settings.TOKEN_MODEL
        fields = ('auth_token', 'stream_token', 'user_id', 'user_name')

    def get_stream_token(self, obj):
        client = StreamChat(api_key=settings.STREAM_API_KEY, api_secret=settings.STREAM_API_SECRET)
        token = client.create_token(str(obj.user.id))

        return token

    def get_user_id(self, obj):
        return str(obj.user.id)

    def get_user_name(self, obj):
        return obj.user.get_full_name() or obj.user.username