from rest_framework import serializers
from .models import Transaction,Account

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self,request):
        amount = request.get("amount")
        request_account = request.get('account')
        print(request_account)
        account = Account.objects.filter(id=request_account.id).first()
        account.balance += amount
        account.save()
        return Transaction.objects.create(**request)