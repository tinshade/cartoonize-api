from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

#For handline file uploads
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

#Importing custom module
from api.cartoonize import cartoonize

#This function adds two numbers and returns the sum!
def addTwoNumbers(a,b):
    return a+b


class Additive(APIView):
    def post(self,request,*args,**kwargs):
        sumnum = addTwoNumbers(request.data.get('numone'), request.data.get('numtwo'))
        return Response(data={"sum":sumnum})


class Cartoonize(APIView):
    #curl -X POST -S -H -u "admin:password" -F "file=@img.jpg;type=image/jpg" 127.0.0.1:8000/resourceurl/imageUpload
    def post(self,request, format=None):
        up_file = request.data['file']
        user_name = str(request.data.get('name')) #User's name to save the file as
        pref_ext = str(request.data.get('ext')) #Preferred extension for output file
        curr_ext = up_file.name.split('.')[1]
        path = "./media/user_images/uploads/"
        #Writing the file to disk 
        destination = open(path+up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
        destination.close()
        results = cartoonize(user_name,up_file.name,curr_ext,pref_ext)
        if  results == "Success":
            url = f"/media/user_images/served/{user_name}.{pref_ext}"
            return Response(data={'download':url})
        elif results == "Invalid File Type":
            return Response(data={'response':"Invalid File Type. Only JPG allowed."})
        elif results == "Not Found":
            return Response(up_file.name, status=HTTP_404_NOT_FOUND)
        return Response(up_file.name, status=HTTP_400_BAD_REQUEST)



