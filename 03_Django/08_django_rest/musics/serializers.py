from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistDetailSerializer(ArtistSerializer):
    musics = MusicSerializer(source ="music_set", many=True) #객체 전체를 들고 있기 때문에 many 는 true
    musics_count = serializers.IntegerField(source='music_set.count')

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('musics',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id', )

class MusicDetailSerializer(MusicSerializer):
    comments = CommentSerializer(source='comment_set', many=True)

    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comments',)