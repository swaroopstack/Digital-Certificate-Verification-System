/* =============================================
   Project : Digital Certificate Verification System
   Feature : Archive - Store Expired Certificates
   Author  : Swaroop Kumar, Abhishek Yadav, Kuldeep
   ============================================= */

USE certificate_verification;

-- Create archive table if not exists
CREATE TABLE IF NOT EXISTS Certificate_Archive AS
SELECT * FROM Certificate WHERE 1=0;

-- Move expired certificates into archive
INSERT INTO Certificate_Archive
SELECT * FROM Certificate WHERE Status = 'Expired';
