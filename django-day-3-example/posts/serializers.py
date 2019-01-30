from rest_framework.serializers import ModelSerializer

from posts.models import Post, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'created_at', 'comments')
