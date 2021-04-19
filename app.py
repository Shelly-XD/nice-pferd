from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from bs4 import BeautifulSoup
import subprocess
import requests
import platform
import json
import os
import re

app = Flask(__name__)

true, false, null = True, False, None

try:
    latest_commit_id = eval(requests.get("https://api.github.com/repos/augustin64/nice-pferd/commits/main").text)['sha']
except:
    print(" * Running offline mode")
    latest_commit_id = "null"

with open('./.git/refs/heads/main','r') as f:
    current_commit_id = f.read().replace('\n','')

if current_commit_id == latest_commit_id : running_latest = True
else : running_latest = False

print(' * Using latest nice-pferd version:',running_latest)

def updateStatus(status,max=100,base=0):
    status=((status+base)/max)*100

    if not os.path.exists("./static/downloads"):
        os.mkdir("./static/downloads")

    with open("./static/downloads/status","w") as f:
        f.write(str(round(status,2)))

    if status >= 100:
        print('Download complete')
    else :
        print('Status: '+ str(round(status,1)) + '%')


def downloadManga(dl_url,total_dls=1,current_dl=1,mangaId=""):
    status=0
    updateStatus(status,max=total_dls*100,base=(current_dl-1)*100)
    dl_url=dl_url.replace("%2F","/")
    chapter = dl_url.split("/")[-2].split("-")[-1]
    r=requests.get(dl_url)
    status+=10
    updateStatus(status,max=total_dls*100,base=(current_dl-1)*100)
    soup = BeautifulSoup(r.content, 'html.parser')
    images = soup.find_all("img", {"class": "wp-manga-chapter-img"})
    urls = [(i['src'].replace('\n','').replace('\t',''),i['id']) for i in images]
    status+=10
    updateStatus(status,max=total_dls*100,base=(current_dl-1)*100)

    try :
        os.mkdir("./static/downloads/" + mangaId + "!" + chapter)
    except:
        print("folder already exists")
    print("downloading "+chapter)

    for j in range(len(urls)) :
        i=urls[j]

        with open(("./static/downloads/"+mangaId+"!"+chapter+"/"+i[1]+'.jpg'), 'wb') as handle:
            response = requests.get(i[0], stream=True)

            if not response.ok:
                print(response)
            for block in response.iter_content(1024):

                if not block:
                    break
                handle.write(block)
        status+=(1/len(urls))*80
        updateStatus(status,max=total_dls*100,base=(current_dl-1)*100)
    updateStatus(current_dl*100,max=total_dls*100,base=(current_dl-1)*100)

    with open("./static/downloads.json") as json_file:
        data = json.load(json_file)
    data.append(str(mangaId+"!"+chapter))
    data.sort()

    with open("./static/downloads.json", 'w') as outfile:
        json.dump(data, outfile)


def download(request_data):
    mangaId = request_data.args.get('mangaId')
    actionType = request_data.args.get('type')

    if actionType == 'single':
        dl_url = request_data.args.get('url')
        if mangaId == "" :
            mangaId = ' '.join(dl_url.split('/')[-3].split('-'))
        print(mangaId)
        downloadManga(dl_url,mangaId=mangaId)
        print(dl_url)

    elif actionType == 'multiple':
        firstSegment = request_data.args.get('url1')
        lastSegment = request_data.args.get('url2')
        chapterStart = int(request_data.args.get('start'))
        chapterEnd = int(request_data.args.get('end'))

        if mangaId == "" :
            mangaId = ' '.join(firstSegment.split('/')[-2].split('-'))

        for i in range(chapterStart,chapterEnd+1):
            dl_url = firstSegment + str(i) + lastSegment
            downloadManga(dl_url,total_dls=chapterEnd-chapterStart+1,current_dl=i-chapterStart+1,mangaId=mangaId)
            print(dl_url)


def delete(request_data):
    chapterID = str(request_data.args.get('id'))

    for i in os.listdir('./static/downloads/'+chapterID):
        os.remove('./static/downloads/'+chapterID+'/'+i)
        print('removed',('./static/downloads/'+chapterID+'/'+i))
    os.rmdir('./static/downloads/'+chapterID)

    with open("./static/downloads.json") as json_file:
        data = json.load(json_file)
    data.remove(str(chapterID))
    data.sort()

    with open("./static/downloads.json", 'w') as outfile:
        json.dump(data, outfile)
    
    print('Successfully deleted')


def addBaseUrl(request_data):
    firstSegment = request_data.args.get('firstUrlSegment')
    lastSegment = request_data.args.get('lastUrlSegment')
    mangaName = request_data.args.get("mangaName")

    with open("./static/baseurl.json",'r') as f:
        doc = f.read()
    baseurl=eval(doc)
    baseurl[mangaName] = [firstSegment,lastSegment]

    with open("./static/baseurl.json", 'w') as outfile:
        json.dump(baseurl, outfile)


@app.route("/index")
@app.route("/")
def home():
    with open("./static/downloads.json",'r') as f:
        doc = f.read()
    data = eval(doc)

    if len(data) == 0:
        data.append(" ")

    with open("./static/baseurl.json") as f:
        doc = f.read()
    baseurl=eval(doc)
    return render_template('index.html',data=data,baseurl=baseurl, running_latest=running_latest)

@app.route('/scanreader.html')
@app.route('/scanreader')
def scanreader():
    chapter = request.args.get('chapter')

    if os.path.exists('./static/downloads/'+ chapter):
        pattern = r'image-(.*).jpg'
        raw_list = [int(re.match(pattern,i).group(1)) for i in os.listdir('./static/downloads/'+ chapter)]
        raw_list.sort()
        sorted_paths = [('./static/downloads/' + chapter + '/' + 'image-'+ str(i) +'.jpg' ) for i in raw_list]
        print(sorted_paths)
        return render_template('scanreader.html',data=sorted_paths,mangaid=chapter)
    else:
        return render_template('404.html')

@app.route('/get')
def get():
    action = request.args.get('action')

    if action == 'download' :
        download(request)

    if action == 'delete' :
        delete(request)

    if action == 'log':
        print(request.args.get('log'))

    if action == 'addbaseurl' :
        addBaseUrl(request)

    return action



if __name__ == "__main__":
    app.run(debug = False)
