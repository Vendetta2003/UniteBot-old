import requests
from bs4 import BeautifulSoup


def parse(htmlcode):
    c = 0  
    out = ""
    for ch in htmlcode:
        if(ch in "<>" ):
            c+=1
        elif(c%2==0):
            out+=ch
    data2 = out.split("\n")
    data3 = []
    for x in data2:
        if(x.strip()!=''):
            data3.append(x.strip())
    return(data3)

    
def get_card(name):
    url = f"https://uniteapi.dev/p/{name}"
    resp = requests.get(url)

    s = BeautifulSoup( resp.content , 'html.parser')
    data = s.find( class_ = "player-card" )
    #Extracting player stats
    data2 = parse(str(data))


    #Extracting image data      
    img2  = str(data.find(class_ = "player-card-image")).split("\n")[1]
    img_url = ""
    c = 0
    for x in img2:
        if(x=='"'):
            c+=1
        elif(c==1):
            img_url+=x
    img_url = "https://uniteapi.dev"+img_url



    info  = {}
    if("Master"  in data2):
        info={'Name':f'{data2[0]}' , 'Elo': f'{data2[1]}', 'Code':f'{data2[2]}', 'Level':f'{data2[3]}'
        , 'Rank':f'{data2[4]}' , 'Fp-points':f'{data2[6]}' , 'Tb':f'{data2[8]}' , 'Wins':f'{data2[10]}', 'Wr':f'{data2[12]}' , 'img':f'{img_url}'}
    else:
        info={'Name':f'{data2[0]}' , 'Elo':'N/A', 'Code':f'{data2[1]}', 'Level':f'{data2[2]}'
        , 'Rank':f'{data2[3]}' , 'Fp-points':f'{data2[5]}' , 'Tb':f'{data2[7]}' , 'Wins':f'{data2[9]}', 'Wr':f'{data2[11]}' , 'img':f'{img_url}'}


    return info

#print(get_card("Xml"))
