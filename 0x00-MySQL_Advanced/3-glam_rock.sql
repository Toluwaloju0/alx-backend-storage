-- A script to get a band and compute it longetivity
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan FROM metal_bands 
WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;