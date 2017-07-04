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
    nra = []
    nb_dslam = str(len(dslam))+'%20DSLAMs%20HS%0A'

    for i, element in enumerate(dslam):
        element = element.split('</a>')[0].split('-')[0]
        dslam[i] = element
        if element != dslam[i-1]: #remove double
            nra.append(element)

    nra = '%0A'.join(nra)
    return nb_dslam+nra

def send_message(payload):
    req = get.build_opener()
    url = 'https://smsapi.free-mobile.fr/sendmsg?user=1023xxxx&pass=p7YMLcLxxxxxxx&msg='
    req.open(url+payload)

send_message(parsing_data(get_data()));
