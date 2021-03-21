import requests 
import os
from datetime import datetime
import pandas
import numpy as np
import plotly.graph_objects as go

def GetData():
        
    data= ''
    n=0

    while True :#hit the server multiple times to get all the data

        ploads = {'api-key':'579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b','format':'csv',
        'offset':n,#change offset to get next slice of data
        'limit':10,#max

        }
        r=requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69',params=ploads)
        n+=10#increment offset
        data+=r.text
        if r.text == '':#break when no more data 
            break

    # WRITE DATA TO CSV ##

    time = datetime.now() #write new csv name of file is right now time
    text_file = open("csv/Air-{}.csv".format(time), "w")
    n = text_file.write(data)#write downloaded data 
    text_file.close()