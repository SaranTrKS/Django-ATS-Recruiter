from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Case, When, Value, IntegerField, Q, Sum, Count
from django.db.models.functions import Length, Lower
from .models import Candidate
from .serializers import CandidateSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def candidate_list(request):
    """
    List all candidates or create a new candidate
    """

    if request.method == "GET":
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def candidate_detail(request, pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)
    
    elif request.method in ["PUT", "PATCH"]:
        serializer = CandidateSerializer(candidate, data=request.data, partial=request.method=="PATCH")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET'])
def search_candidates(request):
    """
    Search candidates by name with relevancy-based sorting
    """
    query = request.query_params.get('q', '')
   
    if not query:
        return Response({"error": "Search query parameter 'q' is required"}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    search_words = query.lower().split()

    candidates = Candidate.objects.all()

    name_q = Q()

    for word in search_words:
        name_q |= Q(name__icontains=word)

    candidates = candidates.filter(name_q)

    print(candidates)

    relevancy_cases = []
    for word in search_words:
        relevancy_cases.append(
            Case(
                When(name__icontains=word, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        )
    
    candidates = candidates.annotate(
        relevancy=sum(relevancy_cases)
    )
    
    candidates = candidates.order_by('-relevancy', 'name')
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data)
