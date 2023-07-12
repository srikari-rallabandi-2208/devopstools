from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TopResult

@api_view(['POST'])
def save_top_results(request):
    cpu_data = request.data.get('cpu_data')
    memory_data = request.data.get('memory_data')

    if cpu_data: # and memory_data:
        top_result = TopResult.objects.create(cpu_data=cpu_data)#, memory_data=memory_data)
        return Response({'message': 'Top results saved successfully.'}, status=201)
    else:
        return Response({'message': 'Invalid data.'}, status=400)
