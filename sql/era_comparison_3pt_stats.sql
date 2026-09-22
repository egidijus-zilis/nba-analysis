SELECT 
    CASE 
        WHEN season IN ('2013-14', '2014-15', '2015-16') THEN 'old_era'
        ELSE 'new_era'
    END AS era,
    round((AVG(total_3pa))::numeric, 0) as avg_3pa,
    CORR(total_3pa, wins) AS correlation_wins_3pa,        
    STDDEV(total_3pa) AS std_3pa,
    round((AVG(pct_3p))::numeric, 4) as avg_pct_3p,
    CORR(pct_3p, wins) as correlation_wins_pct_3p,    
    STDDEV(pct_3p) AS std_pct_3p
FROM (
    SELECT wins, season,
           "Corner3_FGA" + "AbovetheBreak3_FGA" AS total_3pa,
           ("Corner3_FGM" + "AbovetheBreak3_FGM")::float / ("Corner3_FGA" + "AbovetheBreak3_FGA") as pct_3p
    FROM team_season_stats
) sub
GROUP BY era