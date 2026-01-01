/* =============================================
   Project : Digital Certificate Verification System
   Feature : Constraints - Unique Email & Status Check
   Author  : Swaroop Kumar, Abhishek Yadav, Kuldeep
   ============================================= */

USE certificate_verification;

-- Ensure each holder has a unique email
ALTER TABLE Holder
ADD CONSTRAINT unique_email UNIQUE (Email);

-- Allow only specific certificate statuses
ALTER TABLE Certificate
ADD CONSTRAINT chk_status
CHECK (Status IN ('Valid', 'Expired', 'Revoked'));
