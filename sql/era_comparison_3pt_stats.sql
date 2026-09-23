SELECT
    CASE
        WHEN season IN ('2013-14', '2014-15', '2015-16') THEN 'old_era'
        ELSE 'new_era'
    END AS era,
    ROUND((AVG(total_3pa))::numeric, 0) AS avg_3pa,
    CORR(total_3pa, wins) AS correlation_wins_3pa,
    STDDEV_POP(total_3pa) AS std_3pa,
    ROUND((AVG(pct_3p))::numeric, 4) AS avg_pct_3p,
    CORR(pct_3p, wins) AS correlation_wins_pct_3p,
    STDDEV_POP(pct_3p) AS std_pct_3p,
    ROUND((AVG(pct_3pa_of_total))::numeric, 4) AS avg_pct_3pa_of_total,
    CORR(pct_3pa_of_total, wins) AS correlation_wins_pct_3pa_of_total
FROM (
    SELECT wins, season,
           "Corner3_FGA" + "AbovetheBreak3_FGA" AS total_3pa,
           ("Corner3_FGM" + "AbovetheBreak3_FGM")::float / ("Corner3_FGA" + "AbovetheBreak3_FGA") AS pct_3p,
           "RestrictedArea_FGA" + "InThePaint(Non-RA)_FGA" + "Mid-Range_FGA" + "Corner3_FGA" + "AbovetheBreak3_FGA" AS total_fga,
           ("Corner3_FGA" + "AbovetheBreak3_FGA")::float / 
           ("RestrictedArea_FGA" + "InThePaint(Non-RA)_FGA" + "Mid-Range_FGA" + "Corner3_FGA" + "AbovetheBreak3_FGA") AS pct_3pa_of_total
    FROM team_season_stats
) sub
GROUP BY era