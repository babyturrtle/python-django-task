WITH wins AS (
  SELECT 
    bid.client_number AS "client_number", 
    COUNT(bid.play_id) AS "Побед" 
  FROM 
    bid 
    INNER JOIN event_value ON bid.play_id = event_value.play_id 
  WHERE 
    bid.coefficient = event_value.value 
    AND event_value.outcome = "win" 
  GROUP BY 
    bid.client_number
), 
loses AS (
  SELECT 
    bid.client_number AS "client_number", 
    COUNT(bid.play_id) AS "Поражений" 
  FROM 
    bid 
    INNER JOIN event_value ON bid.play_id = event_value.play_id 
  WHERE 
    bid.coefficient = event_value.value 
    AND event_value.outcome = "lose" 
  GROUP BY 
    bid.client_number
) 
SELECT 
  wins.client_number, 
  wins.Побед, 
  loses.Поражений 
FROM 
  wins 
  INNER JOIN loses ON wins.client_number = loses.client_number 
ORDER BY 
  wins.client_number;
