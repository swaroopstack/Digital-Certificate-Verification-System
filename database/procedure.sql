USE certificate_verification;

DELIMITER $$

CREATE PROCEDURE VerifyCertificate(IN cert_id INT)
BEGIN
  DECLARE cert_status VARCHAR(20);
  
  SELECT Status INTO cert_status
  FROM Certificate
  WHERE Certificate_ID = cert_id;

  IF cert_status = 'Valid' THEN
    INSERT INTO Verification_Log (Verification_ID, Certificate_ID, Verifier_Name, Verification_Date, Verification_Status)
    VALUES (
      (SELECT IFNULL(MAX(Verification_ID), 9000) + 1 FROM Verification_Log),
      cert_id, 'System_Verifier', CURDATE(), 'Verified'
    );
  ELSE
    INSERT INTO Verification_Log (Verification_ID, Certificate_ID, Verifier_Name, Verification_Date, Verification_Status)
    VALUES (
      (SELECT IFNULL(MAX(Verification_ID), 9000) + 1 FROM Verification_Log),
      cert_id, 'System_Verifier', CURDATE(), 'Invalid'
    );
  END IF;
END$$

DELIMITER ;
