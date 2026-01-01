USE certificate_verification;

DELIMITER $$

CREATE TRIGGER update_certificate_status
BEFORE SELECT ON Certificate
FOR EACH ROW
BEGIN
  UPDATE Certificate
  SET Status = 'Expired'
  WHERE Expiry_Date < CURDATE() AND Status != 'Expired';
END$$

DELIMITER ;
