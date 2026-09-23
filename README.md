# NBA shooting analysis: Shot Selection and Efficiency (2013-2016 vs 2023-2026)

## Purpose

This project analyzes NBA shot selection and shooting efficiency, and how they relate to team success, comparing two eras: 2013-16 and 2023-26.

## Data

Data is taken from stats.nba.com using nba_api.

Two datasets were pulled from nba_api:

- 'LeagueStandings' - providing wins, losses per team per season.
- 'LeagueDashTeamShotLocations' - providing field goals made/attempted by shot zone(Restricted Area, Paint, Mid-Range, Corner 3, Above the Break 3)

Data was taken from 2013-16 and 2023-26 seasons.

Specifically, 2011-2012 and 2019-2020 seasons were avoided due to the lockout and COVID, which shortened those seasons.

## Analysis 1: 3-Point Volume vs Efficiency

### Methodology

3-point shots come in two zones: Corner 3 and Above the Break 3. Volume was calculated by adding attempted shots from both zones. Efficiency was calculated by adding made shots from both zones and dividing by total attempted shots.

The data was divided in two eras to compare statistics between them:
- 'old_era' - 2013-16 seasons
- 'new_era' - 2023-26 seasons

Correlation between each metric and team wins was calculated using Pearson correlation, separately for each era.

### Findings

| Metric                     | Old Era (2013-16) | New Era (2023-26) |
|-----------------------------|:------------------:|:------------------:|
| Avg. 3PA                   |       1,843         |       2,987         |
| Std. dev. 3PA               |        327          |        285          |
| Corr(3PA, Wins)              |        0.32         |        0.09         |
| Avg. 3P%                   |       35.6%         |       36.3%         |
| Std. dev. 3P%                |       0.018         |       0.014         |
| Corr(3P%, Wins)              |        0.60         |        0.64         |
| 3PA share of total FGA       |       26.9%         |       40.9%         |
| Corr(3PA share, Wins)         |        0.33         |        0.09         |