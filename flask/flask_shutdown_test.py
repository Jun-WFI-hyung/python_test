from flask import Flask
from werkzeug.serving import make_server

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def run_flask():
    # Flask 애플리케이션을 내장 서버로 실행
    server = make_server('localhost', 5000, app)
    server.serve_forever()

def stop_flask():
    # 서버를 종료하기 위한 함수를 얻어옴
    func = app.make_shutdown_server_func()
    
    # 종료 함수를 호출하여 서버 종료
    func()

if __name__ == '__main__':
    # Flask 애플리케이션 실행
    run_flask()

    # 여기서 다른 작업 수행

    # Flask 애플리케이션 종료
    stop_flask()
