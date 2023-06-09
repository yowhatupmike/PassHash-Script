# PassHash-Script
 script that performs password hashing, salting, and verification using the passlib library.

This script utilizes the bcrypt algorithm for password hashing, which incorporates salt and multiple rounds of hashing to enhance security. The register_user function generates a salt and hashes the password before securely storing it in your database. The verify_password function retrieves the hashed password from the database, and then uses bcrypt.verify to compare the provided password with the stored hashed password.
