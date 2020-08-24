# from rest_framework.serializers import ModelSerializer
# from django.contrib.auth.models import User

# class UserSerializer(ModelSerializer):
#     entry = serializers.PrimaryKeyRelatedField(many=True, queryset=Entry.objects.all())
#     class Meta:
#         model = User

#         fields = ['id', 'email', 'is_active', 'is_staff', 'is_admin', 'timestamp', 'entry']