WITH all_teams AS (
  SELECT 
    play_id, 
    home_team AS team 
  FROM 
    event_entity 
  UNION 
  SELECT 
    play_id, 
    away_team AS team 
  FROM 
    event_entity
) 
SELECT 
  CONCAT(team1, " - ", team2) AS game, 
  COUNT(*) AS games_count 
FROM 
  (
    SELECT 
      play_id, 
      MIN(team) as team1, 
      MAX(team) AS team2 
    FROM 
      all_teams 
    GROUP BY 
      play_id
  ) AS ordered_teams 
GROUP BY 
  team1, 
  team2 
ORDER BY 
  COUNT(*) ASC;
