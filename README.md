# Python-SQL CLI Password Manager 

## Overview  
A Password Manager to securely manage and store passwords with URL, username, and passwords fields. A Master Password is used to authenticate into the manager "Vault", where all other passwords are stored.  

## Infrastructure  
A docker container with PostgresSQL is used to store passwords. To setup the a new Docker container, with PostgreSQL installed, refer to this article: https://dev.to/andre347/how-to-easily-create-a-postgres-database-in-docker-4moj - super easy setup! Follow the outlined steps within the article.

## Requried Libraries  
- Hashlib
- Cryptodome
- pbkdf2
- psycopg2
- os
- getpass
- sys 

## Setup  

### Step 1: Clone Project and Project Files   

```git clone https://github.com/collinsmc23/python-sql-password-manager```

### Step 2: Generate a Master Password Hash

There are "two factors". of authentiation included within the program. There are two options. You have to make sure the second_FA_location variable is either commented out or has a string inside the main.py program. If you do want to have a second factor of authentication, then you need to include hash the master_password_hash and the second_FA.  

Enter the master password hash inside the master_password_hash variable inside the master_password.py program.  

### Step 3: Connect to Docker Container  
Enter in correct username, database name, and password inside the db_connect.py file.  

### Step 4: Run Main.py  
Run main.py with all files inside the same directory.

```main.py [ARGUMENT] [OPTIONS}```  

Example to add Password: ```main.py -a https://cybercademy.org gcollins```  

Enter the one of the following paramters:

`-a or --add [WEBSITE URL] [USERNAME]`: Automatically generates a random 20 character string for password.  
`-q or --query [WEBSITE URL]`: Look up field by website URL.  
`-l or --list`: List all stored fields in password vault.  
`-d or --delete [WEBSITE URL]`: Delete a field by website URL.  
`-ap or --add_password [WEBSITE_URL] [USERNAME] [PASSWORD]`: Enter in a URL, username, and custom password.  
`-uurl or --update_url [NEW_URL] [OLD_URL]`: Update the URL with new URL to currently stored URL.  
`-uuname or --update_username [URL] [NEW_USERNAME]`: Update username of stored URL.
`-upasswd or --update_password [URL] [NEW_PASSWORD]`: Update new password by stored URL.
