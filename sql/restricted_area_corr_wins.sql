SELECT
	CASE WHEN season IN ('2013-14', '2014-15', '2015-16') THEN 'old_era' ELSE 'new_era' END AS era,
Corr("RestrictedArea_FGA", wins) AS corr_RAfga_wins,
ROUND(AVG("RestrictedArea_FGA")::numeric, 0) AS avg_RAfga,
Corr("RestrictedArea_FG_PCT", wins) AS corr_RApct_wins,
ROUND(AVG("RestrictedArea_FG_PCT")::numeric, 4) AS avg_RApct
FROM team_season_stats tss 
GROUP BY era