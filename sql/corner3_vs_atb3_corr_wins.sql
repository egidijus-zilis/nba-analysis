SELECT
    CASE WHEN season IN ('2013-14','2014-15','2015-16') THEN 'old_era' ELSE 'new_era' END as era,
    ROUND(CORR("Corner3_FG_PCT", wins)::numeric, 4) as corr_corner3,
    ROUND(CORR("AbovetheBreak3_FG_PCT", wins)::numeric, 4) as corr_atb3,
    ROUND(AVG("Corner3_FG_PCT")::numeric, 4) as avg_corner3,
    ROUND(AVG("AbovetheBreak3_FG_PCT")::numeric, 4) as avg_atb3
FROM team_season_stats
GROUP BY era