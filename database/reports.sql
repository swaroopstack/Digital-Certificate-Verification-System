/* =============================================
   Project : Digital Certificate Verification System
   Feature : Report - Complete Certificate Summary
   Author  : Swaroop Kumar, Abhishek Yadav, Kuldeep
   ============================================= */

USE certificate_verification;

SELECT 
  c.Certificate_ID,
  h.Name AS Holder_Name,
  i.Institution_Name AS Issuer_Name,
  c.Certificate_Type,
  c.Status AS Certificate_Status,
  v.Verification_Status,
  v.Verification_Date
FROM Certificate c
JOIN Holder h ON c.Holder_ID = h.Holder_ID
JOIN Issuer i ON c.Issuer_ID = i.Issuer_ID
LEFT JOIN Verification_Log v ON c.Certificate_ID = v.Certificate_ID;
