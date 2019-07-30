from .models import Authors, Articles, Publication
from rest_framework import serializers


class AuthorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
