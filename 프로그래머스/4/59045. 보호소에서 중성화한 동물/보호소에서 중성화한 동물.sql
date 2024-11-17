-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM (SELECT ANIMAL_ID
     FROM ANIMAL_INS
     WHERE SEX_UPON_INTAKE LIKE 'Intact%') I
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.SEX_UPON_OUTCOME REGEXP('Spayed|Neutered')
ORDER BY I.ANIMAL_ID