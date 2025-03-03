from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Candidate
from .serializers import CandidateSerializer


@api_view(["POST"])
def create_candidate(request):
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_candidate(request,pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CandidateSerializer(candidate, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_candidate(request, pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    candidate.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def get_candidates(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_candidate(request, pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CandidateSerializer(candidate)
    return Response(serializer.data)