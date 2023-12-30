from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status 
from createnote.serializers import *
from rest_framework.decorators import api_view
from createnote.models import *

# Create your views here.
@api_view(['GET'])
def getNotesList(request):

    try:
        notes = Note.objects.all().order_by('-updated')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:  # Catch specific exceptions if possible
        print("Error:", e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getNoteDetail(request, pk):
    try:
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many=False)
        return  Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])    
def createNote(request):
    
    try:
        print(request.data)
        data = request.data
        body=data['note']
        
        note = Note.objects.create(
            body=body
        )
        print(body)
        note.save()
        n=Note.objects.all()
        serializer=NoteSerializer(n,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])  
def updateNote(request, pk):
    try:
        data = request.data
        note = Note.objects.get(id=pk)

       
        serializer = NoteSerializer(instance=note, data=data)
       
        note.body=request.data.get('note')
        if serializer.is_valid():
           
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# This function will delete a note
@api_view(['DELETE'])      
def deleteNote(request, pk):
    try:
        n=Note.objects.all()
        serializer=NoteSerializer(n,many=True)
        note = Note.objects.get(id=pk)
        note.delete()
        return Response(serializer.data,status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
