from django.shortcuts import render
from .models import Ip
from .helpers import ApiGet


# def get_user_ip():
#     # r = urllib2.urlopen('https://api.ipify.org')
#     # response = json.loads(r.read())
#     # return "ipify address is: " + response
#     ip = get('https://api.ipify.org').text
#     print 'My public IP address is:', ip
#     return ip

# def get_ip_details(ip):
#     ip_json = get("http://ip-api.com/json/" + ip).json()
#     print "detailed ip info: " + str(ip_json)
#     return ip_json

def ip_index(request):
    string_call = ApiGet('https://api.ipify.org', request)
    user_ip = string_call.get_string_response()
    print user_ip
    location_call = ApiGet("http://ip-api.com/json/" + user_ip, request)
    location_details = location_call.get_json_response()
    print str(location_details)
    # ip_url = "http://www.telize.com/geoip?callback=?"
    # api = ApiGet(ip_url, request)
    return render(request, 'ip/ip_index.html', {'user_ip': user_ip, 'location_details': location_details})
