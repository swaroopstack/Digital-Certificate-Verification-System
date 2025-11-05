USE certificate_verification;

INSERT INTO Holder VALUES
(1, 'Aarav Mehta', 'aarav@gmail.com', '9876543210', '2000-08-15'),
(2, 'Neha Patel', 'neha@gmail.com', '9998887770', '1999-02-20');

INSERT INTO Issuer VALUES
(101, 'Tech University', 'admin@techuni.edu', 'AUTH123'),
(102, 'Code Institute', 'info@codeinst.org', 'AUTH456');

INSERT INTO Certificate VALUES
(501, '2024-05-10', '2030-05-10', 'B.Tech Degree', 'Valid', 1, 101),
(502, '2023-01-01', '2028-01-01', 'Python Certification', 'Valid', 2, 102);

INSERT INTO Verification_Log VALUES
(9001, 501, 'HR Infosys', '2025-02-15', 'Verified'),
(9002, 502, 'TechCorp HR', '2025-03-01', 'Verified');
