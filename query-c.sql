use `pollution-db2`;
SELECT 
    YEAR(`date Time`) AS date_time,
    AVG(`PM2.5`) AS `average PM2.5`,
    AVG(`VPM2.5`) AS `average VPM2.5`,
    `location` AS station
FROM
    readings,
    stations
WHERE
    YEAR(`date Time`) BETWEEN '2010' AND '2019'
        AND TIME(`date Time`) = '08:00:00'
        AND `stationid-fk` = `stationid`
GROUP BY station
ORDER BY station ASC;