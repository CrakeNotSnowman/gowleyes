from flask import Flask, request, render_template
import kmmessage
import time
app = Flask(__name__)
from utils import docsToEReader

'''
(A copy of) An unholy collection of Bodge Flask Server Edition


'''

@app.route("/")
def hello():
    '''
    Default landing page
    '''
    return "Hello World"

@app.route("/text", methods=['GET', 'POST'])
def text(inputText = "No"):
    '''
    Page which the extension goes to

    On a successful post command, page will grab info from 'currentTab'
    and pass it along to the docsToEReader program

    Because the extension is only providing the url, (not whatever the 
    browser is working on) the destination must be something a python script
    can sepperately reach and obtain




    '''

    if request.method =="POST":
        taburl = request.form.get('currentTab')
        print(taburl)

        print('>',taburl)
        if 'arxiv' in taburl:
            # Super naive check
            docsToEReader.run_arxiv_vanity_bodge(taburl)
        else:
            print(taburl)
            print("Could not proccess at this time, arxiv only")
        #for imd in cmd:
        #    print(imd)
    else:
        taburl = inputText
    #kmmessage.sms_message_Send("", "It works! \nPython Execution!") # This works :) 
    time.sleep(1)


    #print(request)
    #print(request.values)
    #return request.args['data']
    return taburl


if __name__ == "__main__":
    app.run(port=7000, debug=True)