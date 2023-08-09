from rest_framework import serializers
from .models import *

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['id', 'transaction', 'coin', 'type', 'notify', 'email_template', 'date']

    def create(self, validated_data):
        data = dict()
        transaction = validated_data['transaction']
        data['address'] = transaction.transactionHash
        data['logo'] = transaction.logo
        data['scam_reports'] = transaction.scam_reports
        data['risk'] = 'In Progress'
        SocialMedia.objects.create(**data)
        return super().create(validated_data)

    def to_representation(self, instance):
        _response = super().to_representation(instance)
        transaction = Transaction.objects.get(id=_response['transaction'])
        _transaction = TransactionSerializer(instance=transaction)
        _response['transaction']=_transaction.data
        return _response

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

