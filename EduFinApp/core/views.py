from django.http import JsonResponse
from core.models import Testing
from core.serializers import TestingSerializer

def testing_view(request):
    testing_records = Testing.objects.all()
    serializer = TestingSerializer(testing_records, many=True)
    return JsonResponse(serializer.data, safe=False)

def testing_detail(request, id):
    try:
        testing_record = Testing.objects.get(id=id)  
    except Testing.DoesNotExist:
        return JsonResponse({"error": "Record not found"}, status=404)
    
    serializer = TestingSerializer(testing_record)
    return JsonResponse(serializer.data)