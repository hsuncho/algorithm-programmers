-- 코드를 입력하세요
SELECT HISTORY_ID,
    CASE
        WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 90
            THEN c.DAILY_FEE 
                * (100 - (
                    SELECT DISCOUNT_RATE
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE DURATION_TYPE = '90일 이상'
                        AND CAR_TYPE = '트럭'
                )) / 100
                * (DATEDIFF(h.END_DATE, h.START_DATE) + 1)
        WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 30
            THEN c.DAILY_FEE 
                * (100 - (
                    SELECT DISCOUNT_RATE
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE DURATION_TYPE = '30일 이상'
                        AND CAR_TYPE = '트럭'
                )) / 100
                * (DATEDIFF(h.END_DATE, h.START_DATE) + 1)
        WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 7
            THEN c.DAILY_FEE 
                * (100 - (
                    SELECT DISCOUNT_RATE
                    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                    WHERE DURATION_TYPE = '7일 이상'
                        AND CAR_TYPE = '트럭'
                )) / 100
                * (DATEDIFF(h.END_DATE, h.START_DATE) + 1)
        ELSE c.DAILY_FEE * (DATEDIFF(h.END_DATE, h.START_DATE) + 1)
    END AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
JOIN CAR_RENTAL_COMPANY_CAR c
    ON h.CAR_ID = c.CAR_ID
WHERE c.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC;
