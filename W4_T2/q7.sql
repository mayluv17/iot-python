DELETE FROM device WHERE id = (SELECT MIN(id) FROM device)