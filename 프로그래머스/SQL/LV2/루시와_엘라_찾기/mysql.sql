SELECT
    A.ANIMAL_ID,
    A.NAME,
    A.SEX_UPON_INTAKE
FROM ANIMAL_INS AS A
WHERE
    A.NAME = 'Lucy'
    OR A.NAME = 'Ella'
    OR A.NAME = 'Pickle'
    OR A.NAME = 'Rogan'
    OR A.NAME = 'Sabrina'
    OR A.NAME = 'Mitty'