# Secure Database Access System

Designed and implemented a secure web-based database portal that ensures data confidentiality, access control, and multi-factor authentication (MFA). This system allows only authorized users, based on their assigned roles (RBAC), to access or manipulate encrypted data stored securely in the backend database.
The platform encrypts all sensitive data using AES-256 encryption before storage and decrypts it only during authorized access. Role-based restrictions are enforced across views, limiting data visibility and CRUD operations. 

# Key Features:

    🔐 AES-256 Encryption of database records using PyCryptodome

    🧑‍💼 Role-Based Access Control (RBAC): Admin, Analyst, and General User roles

    📲 Multi-Factor Authentication (MFA) integrated for all logins

    🧠 Secure Key Management System (KMS) using environment variables or Vault

    🛡️ Middleware-based access filters for secure routing and data-level access

    📝 Audit logs for data access and login events (optional feature)
