from django.http import JsonResponse
from core.models import Testing
from core.serializers import TestingSerializer

# View for all records
def testing_view(request):
    testing_records = Testing.objects.all()
    serializer = TestingSerializer(testing_records, many=True)
    return JsonResponse(serializer.data, safe=False)

# View for single record by ID
def testing_detail(request, id):
    try:
        record = Testing.objects.get(id=id)
        serializer = TestingSerializer(record)
        return JsonResponse(serializer.data, safe=False)
    except Testing.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)