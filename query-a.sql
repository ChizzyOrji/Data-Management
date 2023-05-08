use `pollution-db2`;
SELECT 
    `date Time` AS date_time,
    `location` AS station_name,
    `NOx` AS highest_recorded_value
FROM
    readings,
    stations
WHERE
    `NOx` = (SELECT 
            MAX(`NOx`)
        FROM
            readings
        WHERE
            YEAR(`date Time`) = '2019')
        AND `stationid-fk` = `stationid`;