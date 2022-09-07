from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9302025d5b03793fb0c2d7ec0f578885').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+ ' '+ str(json_data['coord']['lat']),
            "temperature": str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure'])+'hPa',
            "humidity":str(json_data['main']['humidity'])+'%',
        }
    else:
        city = ' '
        data = {}
    return render(request, 'index.html',{'city':city,'data':data})