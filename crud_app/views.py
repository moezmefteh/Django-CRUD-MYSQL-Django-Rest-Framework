from django.shortcuts import render
from crud_app.models import Tutorial

from rest_framework.decorators import api_view
from crud_app.serializers import TutorialSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status



@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
        # GET list of tutorials
        if request.method == 'GET':
            tutorials = Tutorial.objects.all()
            title = request.GET.get('title', None)
            if title is not None:
                tutorials = tutorials.filter(title__icontains=title)
            tutorials_serializer = TutorialSerializer(tutorials, many=True)
            return Response(tutorials_serializer.data)
        #  POST a new tutorial,
        elif request.method == 'POST':
            tutorial_data = JSONParser().parse(request)
            tutorial_serializer = TutorialSerializer(data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return Response( status=status.HTTP_201_CREATED) 
            return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # DELETE all tutorials
        elif request.method == 'DELETE':
            count = Tutorial.objects.all().delete()
            return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
           
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
             tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
              return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return Response(tutorial_serializer.data) 
    
    
    # put an object
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return Response(tutorial_serializer.data) 
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    # # delete
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET'])
def tutorial_list_published(request):
  tutorials = Tutorial.objects.filter(published=True)   
  if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)

@api_view(['GET','PUT','DELETE'])
def tutorial_detail_title(request,title):
    # find Tutorial by pk (id)
    try: 
            salaire_title = Tutorial.objects.get(title=title) 
    except Tutorial.DoesNotExist: 
              return Response({'message': 'The salary does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        salaire_serializer = TutorialSerializer(salaire_title) 
        return Response(salaire_serializer.data) 
    
    # put a Tutorial
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        salaire_serializer = TutorialSerializer(salaire_title, data=data) 
        if salaire_serializer.is_valid(): 
            salaire_serializer.save() 
            return Response( status=status.HTTP_201_CREATED) 
        return Response(salaire_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a Tutorial by pk
    elif request.method == 'DELETE': 
        salaire_title.delete() 
        return Response({'message': 'title was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

