SELECT wands_table.id, wands_property.age, wands_table.coins_needed, wands_table.power
FROM Wands_Property wands_property
JOIN Wands wands_table ON wands_property.code = wands_table.code
WHERE wands_property.is_evil = 0
    AND wands_table.coins_needed =  (SELECT MIN(wands_table2.coins_needed)
                                    FROM Wands wands_table2
                                    JOIN Wands_Property wands_property2
                                    ON wands_table2.code = wands_property2.code
                                    WHERE wands_property2.age = wands_property.age
                                    AND wands_table2.power = wands_table.power)
ORDER BY wands_table.power DESC, wands_property.age DESC;