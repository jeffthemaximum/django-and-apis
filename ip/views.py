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
def save_to_db(user_ip, location_details, user):
    ip = Ip(
        user=user,
        address=user_ip,
        city=location_details['city'],
        state=location_details['region'],
        country=location_details['country'],
        zip=location_details['zip'],
        isp_provider=location_details['isp'],
        organization=location_details['org']
        )
    ip.save()


def query_db(user):
    ips = Ip.objects.filter(user=user).order_by('date_used').reverse()
    return ips


def ip_index(request):
    # get ip address
    string_call = ApiGet('https://api.ipify.org', request)
    user_ip = string_call.get_string_response()
    print user_ip

    #get ip address details
    location_call = ApiGet("http://ip-api.com/json/" + user_ip, request)
    location_details = location_call.get_json_response()
    print str(location_details)

    #save to db, #query db
    if request.user.is_authenticated():
        ips = query_db(request.user)
        save_to_db(user_ip, location_details, request.user)
        return render(request, 'ip/ip_index.html', {'user_ip': user_ip, 'location_details': location_details, 'ips': ips})

    return render(request, 'ip/ip_index.html', {'user_ip': user_ip, 'location_details': location_details})
