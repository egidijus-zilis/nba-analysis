SELECT
	era,	
	AVG(mid_range_share) AS avg_mid_range_share,
	corr(mid_range_share, wins) AS corr_mid_range_share_wins
FROM (
	SELECT
		wins,
		CASE WHEN season IN ('2013-14', '2014-15', '2015-16') THEN 'old_era' ELSE 'new_era' END AS era,
		"Mid-Range_FGA"::float / ("RestrictedArea_FGA" + "InThePaint(Non-RA)_FGA" + "Mid-Range_FGA" + "Corner3_FGA" + "AbovetheBreak3_FGA") AS mid_range_share
	FROM team_season_stats tss 
) sub
GROUP BY era
	
	