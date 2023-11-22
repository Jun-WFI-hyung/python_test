from flask import Flask                                                         
import threading
app = Flask(__name__)



def myIVR():
  print("-----------------Thrd1-myIVR --------------------")
  app = Flask(__name__)
  app.run(debug=False)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
  return str(resp)

@app.route("/mainFlow", methods=['GET', 'POST'])
def mainFlow():
    """Respond to """
    resp = VoiceResponse()

def myTest():
  print("E2Etest")
  thrd1 = threading.Thread(target=myIVR, args=[])
  thrd1.start()
  print("trigger event")
#xyz()

################################################################
def main():
    myTest()

if __name__ == '__main__':
    main()