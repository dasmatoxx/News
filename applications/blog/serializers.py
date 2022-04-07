from rest_framework import serializers

from applications.blog.models import New, NewsImage


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = New
        fields = ('title', 'description', 'date_published')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = NewsImageSerializer(NewsImage.objects.filter(news=instance.id),
                                           many=True, context=self.context).data
        return rep
