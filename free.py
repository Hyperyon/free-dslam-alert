# -*- coding:Utf-8 -*-
import urllib2 as get

start = "text-align:left; font-size:medium;"
end = "</p><p style='font-size:12px; text-align:left;'>"

def get_data():
    req = get.build_opener()
    req.addheaders = [('User-Agent', 'Mozilla/5.0')]
    data = req.open('https://www.free-reseau.fr/').read()
    return data

def parsing_data(data):
    data = data.split(start)[1].split(end)[0]
    dslam = data.split("'>")[1:]

    for i, element in enumerate(dslam):
        dslam[i] = element.split('</a>')[0]

    nb_dslam = str(len(dslam))+'%20DSLAMs%20HS%0A%0'
    dslam = '%0A'.join(dslam)
    return nb_dslam+dslam

def send_message(payload):
    req = get.build_opener()
    url = 'https://smsapi.free-mobile.fr/sendmsg?user=123456789&pass=p7YMLcLxxxxxx&msg='
    req.open(url+payload)

send_message(parsing_data(get_data()));
