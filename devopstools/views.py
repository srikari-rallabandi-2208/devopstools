from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TopResult, ProcessResult

from django.shortcuts import render
from .models import TopResult

def top_results(request):
    top_results = TopResult.objects.all().order_by('-created_at')
    context = {'top_results': top_results}
    return render(request, 'top_results.html', context)


@api_view(['POST'])
def save_top_results(request):
    cpu_data = request.data.get('cpu_data')
    memory_data = request.data.get('memory_data')

    if cpu_data and memory_data:
        top_result = TopResult.objects.create(cpu_data=cpu_data, memory_data=memory_data)
        return Response({'message': 'Top results saved successfully.'}, status=201)
    else:
        return Response({'message': 'Invalid data.'}, status=400)

@api_view(['POST'])
def save_ps_results(request):
    ps_results = request.data
    ProcessResult.objects.bulk_create([
        ProcessResult(**result) for result in ps_results
    ])
    return Response({'message': 'PS results saved successfully.'}, status=201)

def ps_results(request):
    process_results = ProcessResult.objects.all()
    context = {'process_results': process_results}
    return render(request, 'ps_results.html', context)