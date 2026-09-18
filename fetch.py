import pandas
from nba_api.stats.endpoints import LeagueStandings
from nba_api.stats.endpoints import LeagueDashTeamShotLocations

seasons = ["2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
all_seasons_standings = []
all_seasons_shot_percentages = []
df_all_seasons_wins = pandas.DataFrame()
df_all_seasons_shot_percentages = pandas.DataFrame()


for i in range(len(seasons)):
    standings = LeagueStandings(season=seasons[i])
    df_standings = standings.get_data_frames()[0]
    df_standings["Season"] = seasons[i]
    all_seasons_standings.append(df_standings[["Season", "TeamID", "TeamName", "TeamCity", "WINS", "LOSSES"]])

    shot_percentages = LeagueDashTeamShotLocations(season=seasons[i])
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
    


df_all_seasons_wins = pandas.concat(all_seasons_standings, ignore_index=True)
df_all_seasons_shot_percentages = pandas.concat(all_seasons_shot_percentages, ignore_index=True)
print(df_all_seasons_wins)
print(df_all_seasons_shot_percentages)
print(df_all_seasons_shot_percentages.columns)