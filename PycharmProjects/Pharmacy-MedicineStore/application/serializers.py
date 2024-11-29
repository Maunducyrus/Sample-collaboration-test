from rest_framework import serializers, response

from application.models import Company, CompanyBank


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = '__all__'

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerializer(instance.company_id).data
        return response