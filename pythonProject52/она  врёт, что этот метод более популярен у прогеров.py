from sqlalchemy import create_engine, Table, column, Integer, String, MetaData, select

conn_str =f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
# и создание объекта Engine для  подключения к базе данных
engine = create_engine(conn_str)
# создаём объект MetaData для описания таблици базы данных
metadata = MetaData(schema='sql')
# создаём объекта Table для работы с таблицей
pokemon_table = Table('pokemon', metadata,
    #column=("id", Integer, primary_key=True),
    #column=("name", String),
    #column=("type", String),
    #column=("type2", String),
    #column=("hp", Integer),
    #column=("attack", Integer),
    #column=("defence", Integer),
    #column=("speed", Integer),)
# и подключаемся к базе данных:
connection = engine.connect()
# выполнение запроса на чтение:
select_query = select([pokemon_table]). Limit(10)
result = connection.execute(select_query)
# и обработка результатов запроса
for row in result:
    print(row)
connection.close()