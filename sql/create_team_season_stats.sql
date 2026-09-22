CREATE TABLE team_season_stats AS
SELECT s.team_id, s.season,
       s.team_city || ' ' || s.team_name AS team_name,
       s.wins, s.losses,
       sl."RestrictedArea_FGM", sl."RestrictedArea_FGA", sl."RestrictedArea_FG_PCT",
       sl."Mid-Range_FGM", sl."Mid-Range_FGA", sl."Mid-Range_FG_PCT",
       sl."Corner3_FGM", sl."Corner3_FGA", sl."Corner3_FG_PCT",
       sl."AbovetheBreak3_FGM", sl."AbovetheBreak3_FGA", sl."AbovetheBreak3_FG_PCT"
FROM standings s
JOIN shot_locations sl
USING (team_id, season)