from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from core.models import Testing, Transaction, Category, Budget
from core.serializers import TestingSerializer, TransactionSerializer, CategorySerializer, BudgetSerializer

class TestingListView(APIView):
    def get(self, request):
        testings = Testing.objects.all()
        serializer = TestingSerializer(testings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id, user):
        try:
            return Transaction.objects.get(id=id, user=user)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, id):
        transaction = self.get_object(id, request.user)
        if transaction is None:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, id):
        transaction = self.get_object(id, request.user)
        if transaction is None:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        transaction = self.get_object(id, request.user)
        if transaction is None:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def testing_view(request, id=None):
    if id is not None:
        try:
            transaction = Transaction.objects.get(id=id)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user)
    else:
        transactions = Transaction.objects.all()

    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BudgetListView(APIView):
    def get(self, request):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BudgetDetailView(APIView):
    def get_object(self, id):
        try:
            return Budget.objects.get(id=id)
        except Budget.DoesNotExist:
            return None

    def get(self, request, id):
        budget = self.get_object(id)
        if budget is None:
            return Response({"error": "Budget not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, id):
        budget = self.get_object(id)
        if budget is None:
            return Response({"error": "Budget not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        budget = self.get_object(id)
        if budget is None:
            return Response({"error": "Budget not found"}, status=status.HTTP_404_NOT_FOUND)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)