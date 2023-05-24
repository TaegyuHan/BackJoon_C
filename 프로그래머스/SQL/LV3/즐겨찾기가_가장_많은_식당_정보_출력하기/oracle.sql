SELECT
    R.FOOD_TYPE,
    R.REST_ID,
    R.REST_NAME,
    R.FAVORITES
FROM
    REST_INFO R
JOIN
    (SELECT FOOD_TYPE, MAX(FAVORITES) AS MAX_FAVORITES
     FROM REST_INFO
     GROUP BY FOOD_TYPE) X
ON
    R.FOOD_TYPE = X.FOOD_TYPE
    AND R.FAVORITES = X.MAX_FAVORITES
ORDER BY
    R.FOOD_TYPE DESC;
