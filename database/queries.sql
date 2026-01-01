USE certificate_verification;

-- 1. Show all certificates
SELECT * FROM Certificate;

-- 2. List each holder with their certificate
SELECT h.Name, c.Certificate_Type, c.Status
FROM Holder h
JOIN Certificate c ON h.Holder_ID = c.Holder_ID;

-- 3. Find certificates issued by 'Tech University'
SELECT c.Certificate_ID, c.Certificate_Type
FROM Certificate c
JOIN Issuer i ON c.Issuer_ID = i.Issuer_ID
WHERE i.Institution_Name = 'Tech University';
