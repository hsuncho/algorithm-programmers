SELECT
    i.ID,
    n.FISH_NAME,
    i.LENGTH
FROM FISH_INFO i
JOIN FISH_NAME_INFO n
    ON i.FISH_TYPE = n.FISH_TYPE
WHERE i.LENGTH = (
                    SELECT MAX(LENGTH) 
                    FROM FISH_INFO f
                    WHERE i.FISH_TYPE = f.FISH_TYPE
                )
ORDER BY i.ID;