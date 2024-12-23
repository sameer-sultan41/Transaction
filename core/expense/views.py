from rest_framework.response import Response  # Import Response
from .models import Transaction
from .serializer import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

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
         return Response({
            "status": 200,
         "message": "Transactions fetched successfully"
        })
    
    def post(self, request):
        return Response({
            "status": 200,
            "message": "Transaction created successfully"
        })
    
    def put(self, request):
        return Response({
            "status": 200,
            "message": "Transaction updated successfully"
        })
    
    def delete(self, request):
        return Response({
            "status": 200,
            "message": "Transaction deleted successfully"
        })