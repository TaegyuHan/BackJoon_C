SELECT
    DISTINCT H.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
JOIN (
    SELECT *
    FROM CAR_RENTAL_COMPANY_CAR AS C
    WHERE C.CAR_TYPE = '세단'
) AS J
ON H.CAR_ID	= J.CAR_ID
WHERE MONTH(H.START_DATE) = '10'
ORDER BY CAR_ID DESC