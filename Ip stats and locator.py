import geocoder # pip install geocoder

g = geocoder.ip('me') # replace 'me' for custom IP

print('ip address =',g.ip)
print('Country =',g.country)
print('City =',g.city)
print('Latitude =',g.lat)
print('Longitude =',g.lng)
print('Status =',g.status)
print('Hostname =',g.hostname)
print('ISP =',g.org)
