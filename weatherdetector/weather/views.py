from django.shortcuts import render
import json
from urllib.request import urlopen


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + \
            city + '&appid=1aa2aa9b7f1fd0c809af20313c3ea35d').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + \
                str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = ''

    return render(request, 'index.html', {'city': city, 'data': data})
