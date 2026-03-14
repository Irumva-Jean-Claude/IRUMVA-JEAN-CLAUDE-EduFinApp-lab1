from rest_framework import serializers
from core.models import Testing, Transaction, Category, Budget


class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'title', 'amount', 'transaction_type', 'category', 'date', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_name(self, value):
        """Case-insensitive uniqueness check."""
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("A category with this name already exists.")
        return value


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'name', 'limit_amount', 'month', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']