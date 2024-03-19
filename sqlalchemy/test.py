from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

db_id = 'root'
db_pw = 'dsa804c'
db_ip = 'localhost'
db_port = 3306
db_name = 'adwsdb'
db_url = f'mysql+mysqldb://{db_id}:{db_pw}@{db_ip}:{db_port}/{db_name}'

engine = create_engine(db_url)
with engine.connect() as connection:
    
# Session = sessionmaker(bind=engine)
# session = Session()

sql = text('SELECT * FROM user')
ret = session.execute(sql)
for i in ret:
    print(i)

# 데이터 요청

# 테이터 삽입

# 데이터 삭제

# 데이터 수정