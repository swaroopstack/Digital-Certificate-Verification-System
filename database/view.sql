USE certificate_verification;

CREATE VIEW valid_certificates_view AS
SELECT 
  c.Certificate_ID,
  c.Certificate_Type,
  h.Name AS Holder_Name,
  i.Institution_Name AS Issuer_Name,
  c.Issue_Date,
  c.Expiry_Date,
  c.Status
FROM Certificate c
JOIN Holder h ON c.Holder_ID = h.Holder_ID
JOIN Issuer i ON c.Issuer_ID = i.Issuer_ID
WHERE c.Status = 'Valid';
