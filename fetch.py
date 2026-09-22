import pandas
import time
from nba_api.stats.endpoints import LeagueStandings
from nba_api.stats.endpoints import LeagueDashTeamShotLocations

seasons = ["2011-12", "2012-13", "2013-14", "2014-15", "2015-16",
           "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
all_seasons_standings = []
all_seasons_shot_percentages = []

for i in range(len(seasons)):
    standings = LeagueStandings(season=seasons[i], timeout=60)
    df_standings = standings.get_data_frames()[0]
    df_standings["Season"] = seasons[i]
    all_seasons_standings.append(df_standings[["Season", "TeamID", "TeamCity", "TeamName", "WINS", "LOSSES"]])

    shot_percentages = LeagueDashTeamShotLocations(season=seasons[i], timeout=60)
    df_shot_percentages = shot_percentages.get_data_frames()[0]
    df_shot_percentages["Season"] = seasons[i]
    all_seasons_shot_percentages.append(df_shot_percentages[[
        ("Season", ""),
        ("", "TEAM_ID"),
        ("", "TEAM_NAME"),
        ("Restricted Area", "FGM"),
        ("Restricted Area", "FGA"),
        ("Restricted Area", "FG_PCT"),
        ("In The Paint (Non-RA)", "FGM"),
        ("In The Paint (Non-RA)", "FGA"),
        ("In The Paint (Non-RA)", "FG_PCT"),
        ("Mid-Range", "FGM"),
        ("Mid-Range", "FGA"),
        ("Mid-Range", "FG_PCT"),
        ("Corner 3", "FGM"),
        ("Corner 3", "FGA"),
        ("Corner 3", "FG_PCT"),
        ("Above the Break 3", "FGM"),
        ("Above the Break 3", "FGA"),
        ("Above the Break 3", "FG_PCT"),
    ]])

    time.sleep(1)

df_all_seasons_wins = pandas.concat(all_seasons_standings, ignore_index=True)
df_all_seasons_shot_percentages = pandas.concat(all_seasons_shot_percentages, ignore_index=True)

new_columns = []
for col in df_all_seasons_shot_percentages.columns:
    if col[1] == "":
        naujas_vardas = col[0]
    elif col[0] == "":
        naujas_vardas = col[1]
    else:
        naujas_vardas = col[0] + "_" + col[1]
    new_columns.append(naujas_vardas)
df_all_seasons_shot_percentages.columns = new_columns
df_all_seasons_shot_percentages.columns = [col.replace(" ", "") for col in df_all_seasons_shot_percentages.columns]

df_all_seasons_wins.to_csv("data/wins.csv", index=False)
df_all_seasons_shot_percentages.to_csv("data/shot_percentages.csv", index=False)

print("Data saved to data/wins.csv and data/shot_percentages.csv")