from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'age', 'gender', 'email', 'phone_number', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_mail(self, value):
        if self.instance:
            if Candidate.objects.filter(email=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("This email is already in use.")
        else:
            if Candidate.objects.filter(email=value).exists():
                raise serializers.ValidationError("This email is already in use.")
        return value
    
    def validate_phone_number(self, value):
        value = value.strip()
        if not value.isdigit() and not (value.startswith('+') and value[1:].isdigit()):
            raise serializers.ValidationError("Phone number must contain only digits or start with +")
        return value