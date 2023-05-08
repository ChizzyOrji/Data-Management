use `pollution-db2`;
SELECT 
    `date Time` AS date_time,
    `location` AS station,
    AVG(`PM2.5`) AS `average PM2.5`,
    AVG(`VPM2.5`) AS `average VPM2.5`
FROM
    readings,
    stations
WHERE
    YEAR(`date Time`) = '2019'
        AND TIME(`date Time`) = '08:00:00'
        AND `stationid-fk` = `stationid`
GROUP BY station
ORDER BY station ASC;