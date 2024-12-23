from rest_framework.response import Response  # Import Response
from .models import Transaction
from .serializer import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Sum

# Create your views here.
@api_view(["GET"])
def get_transactions(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer(queryset, many=True)
    return Response({
        "status": 200,
        "data": serializer.data
    })


class TransactionAPI(APIView):

    def get(self, request):
        queryset = Transaction.objects.all().order_by("-id")
        serializer = TransactionSerializer(queryset, many=True)
        return Response({
            "status": 200,
            "total": queryset.aggregate(total=Sum("amount"))["total"] or 0,
            "data": serializer.data
        })
    
    def post(self, request):
        request_data = request.data
        print(request_data)
        serializer = TransactionSerializer(data=request_data)
        if not serializer.is_valid():
            return Response({
                "status": 400,
                "message": "Transaction post failed"
            })
        serializer.save()
        return Response({
            "status": 200,
            "data": serializer.data,
            "message": "Transaction post successfully"
        })
    
    def put(self, request):
        request_data = request.data
        transaction_id = request_data.get("id")
        if not transaction_id:
            return Response({
                "status": 400,
                "message": "Transaction ID is required"
            })
        transaction = Transaction.objects.get(id=transaction_id)
        serializer = TransactionSerializer(transaction, data=request_data,
                                           )
        if not serializer.is_valid():
            return Response({
                "status": 400,
                "message": "Transaction update failed"
            })
        serializer.save()
        return Response({
            "status": 200,
            "data": serializer.data,
            "message": "Transaction updated successfully"
        })
    
    def patch(self, request):
        request_data = request.data
        transaction_id = request_data.get("id")
        if not transaction_id:
            return Response({
                "status": 400,
                "message": "Transaction ID is required"
            })
        transaction = Transaction.objects.get(id=transaction_id)
        serializer = TransactionSerializer(transaction, data=request_data,
                                           partial=True)
        if not serializer.is_valid():
            return Response({
                "status": 400,
                "message": "Transaction update failed"
            })
        serializer.save()
        return Response({
            "status": 200,
            "data": serializer.data,
            "message": "Transaction updated successfully"
        })
    
    def delete(self, request):
        request_data = request.data
        transaction_id = request_data.get("id")
        if not transaction_id:
            return Response({
                "status": 400,
                "message": "Transaction ID is required"
            })
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.delete()
        return Response({
            "status": 200,
            "data": {},
            "message": "Transaction deleted successfully"
        })