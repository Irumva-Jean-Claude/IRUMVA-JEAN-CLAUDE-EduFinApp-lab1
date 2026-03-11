from django.http import JsonResponse
from django.shortcuts import render
from core.models import Testing
from .serializers import TestingSerializer

def health_check(request):
    """
    Returns a simple health check response.
    """
    return JsonResponse({'status': 'ok'})

def testing_view(request):
    """
    List all testing records from the database.
    """
    # 1. Query all Testing records from the database
    records = Testing.objects.all()
    # 2. Serialize them (many=True is for a list of objects)
    serializer = TestingSerializer(records, many=True)
    # 3. Return the JSON (safe=False is for returning a list)
    return JsonResponse(serializer.data, safe=False)

def testing_detail_view(request, id):
    """
    Retrieve a single testing record by its id, handling 'Not Found' errors.
    """
    try:
        # 1. Retrieve a single object by its primary key (id)
        record = Testing.objects.get(pk=id)
        # 2. Serialize the single object
        serializer = TestingSerializer(record)
        # 3. Return the single object's JSON data
        return JsonResponse(serializer.data)
    except Testing.DoesNotExist:
        # Handle the case where the record is not found
        return JsonResponse({'error': 'Record not found'}, status=404)