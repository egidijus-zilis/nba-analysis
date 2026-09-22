import os
import pandas
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

df_wins = pandas.read_csv("data/wins.csv")
df_shot_percentages = pandas.read_csv("data/shot_percentages.csv")

df_wins.to_sql("standings", engine, if_exists="replace", index=False)
df_shot_percentages.to_sql("shot_locations", engine, if_exists="replace", index=False)

print("Data uploaded to the database successfully.")