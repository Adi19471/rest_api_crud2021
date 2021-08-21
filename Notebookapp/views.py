from django.shortcuts import render
# serlizers import
from .serializers import BookSerializers
# modesl import
from .models import BooksModel
from rest_framework .response import Response
# Create your views here.
from rest_framework.decorators import api_view



@api_view(['GET'])
def newbook_view(request):

    booksobj = BooksModel.objects.all()
    serializers_class = BookSerializers(booksobj,many=True)
    return Response({'status': 200,'paypal':serializers_class.data})


@api_view(['POST'])
# post the data

def postNootbook_view(request):
    booksobj = BooksModel.objects.all() # query set data
    serializers_class = BookSerializers(data= request.data)
    if serializers_class.is_valid():
        serializers_class.save()


    return Response(serializers_class.data)


# upate the data # id abased only chainged
@api_view(['POST'])
def updateNotebook_view(request,id):
    chainge_data = BooksModel.objects.get(id=id)
    check_serilizers_class_data = BookSerializers(instance=chainge_data,data=request.data)
    if check_serilizers_class_data.is_valid():
        check_serilizers_class_data.save()

    return  Response(check_serilizers_class_data.data)

# deletee the founction
@api_view(['DELETE'])
def deleteNotbook_view(request,id):
    delete_Class_obj = BooksModel.objects.get(id=id)
    delete_Class_obj.delete()


    return  Response("YOUR DATA HAS DELETED NOT RETRIVED")
