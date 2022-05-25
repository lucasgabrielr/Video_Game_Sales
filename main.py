from sqlalchemy import create_engine
import pandas as pd
engine = create_engine(
    'postgresql+psycopg2://root:root@localhost/video_game_sales')


sql = '''
select distinct("Publisher") from public."Video_Game_Sales";
'''

df = pd.read_sql_query(sql,engine)

print(df)