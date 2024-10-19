-- A script to trigger a reduction
CREATE TRIGGER decrease BEFORE INSERT
ON orders FOR EACH ROW
-- Body or the trigger
UPDATE items SET items.quantity = items.quantity - NEW.number WHERE NEW.item_name = items.name 
