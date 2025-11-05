CREATE DATABASE certificate_verification;
USE certificate_verification;

CREATE TABLE Holder (
  Holder_ID INT PRIMARY KEY,
  Name VARCHAR(100),
  Email VARCHAR(100) UNIQUE,
  Contact_No VARCHAR(15),
  DOB DATE
);

CREATE TABLE Issuer (
  Issuer_ID INT PRIMARY KEY,
  Institution_Name VARCHAR(100),
  Contact_Email VARCHAR(100),
  Authorization_No VARCHAR(50) UNIQUE
);

CREATE TABLE Certificate (
  Certificate_ID INT PRIMARY KEY,
  Issue_Date DATE,
  Expiry_Date DATE,
  Certificate_Type VARCHAR(50),
  Status VARCHAR(20),
  Holder_ID INT,
  Issuer_ID INT,
  FOREIGN KEY (Holder_ID) REFERENCES Holder(Holder_ID),
  FOREIGN KEY (Issuer_ID) REFERENCES Issuer(Issuer_ID)
);

CREATE TABLE Verification_Log (
  Verification_ID INT PRIMARY KEY,
  Certificate_ID INT,
  Verifier_Name VARCHAR(100),
  Verification_Date DATE,
  Verification_Status VARCHAR(20),
  FOREIGN KEY (Certificate_ID) REFERENCES Certificate(Certificate_ID)
);
