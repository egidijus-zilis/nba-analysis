import pandas
from nba_api.stats.endpoints import LeagueStandings

standings = LeagueStandings(season="2023-24")
df_standings = standings.get_data_frames()[0]
df_standings["Season"] = "2023-24"

print(df_standings.columns)
print(df_standings.head())
print(df_standings[["TeamID", "Season", "TeamCity", "TeamName", "WINS"]].sort_values(by="WINS", ascending=False))