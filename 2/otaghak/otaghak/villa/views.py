from django.http.response import HttpResponse, JsonResponse, FileResponse
import os
from django.shortcuts import render

def villa_hello(request):
    return HttpResponse("Hello Kelassor")

def villa_main(request):
    return HttpResponse("This is villa main page!")

def villa_city(request, city_name):
    return HttpResponse(f"Hello {city_name}")

def test_json(request):
    villa_detail = {
        'name' : "Test",
        'city' : 'tehran',
        'no' : '12346548'
    }
    return JsonResponse(villa_detail)


def test_file(request):
    file = os.path.join('/home/saeed/Kelassor/otaghak/otaghak/note.txt')
    return FileResponse(
        open(file, 'rb'),
        as_attachment=True
    )


def test_html(request, year):
    my_data = {
        'year':year,
        'month' : 12
    }
    return render(request, 'villa/main.html', context=my_data)