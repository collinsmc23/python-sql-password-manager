import password_generator
import sql_statements
import db_connect 
import psycopg2
import argparse
import master_password
import getpass
import sys
import hashlib 

def main():
    
    my_parser = argparse.ArgumentParser(description="Password Manager Vault: Create, Add, and Delete URL, Usernames, and Passwords", 
    usage="[options]")
    
    master_password_input = getpass.getpass("Master Password: ").encode()

    second_FA_location = "Dee Boo Dah".encode()

    master_password_hash = hashlib.sha256(master_password_input + second_FA_location).hexdigest()

    if master_password.query_master_pwd(master_password_input, second_FA_location) is True:
        
        connection = db_connect.connection_db()

        print("\nSucessfully Authenticated.\n")

    else:
        print("Failed to authenticate into server. Run the program again.")
        sys.exit() 
        

    my_parser.add_argument("-a", "--add", type=str, nargs=2, help="Add new entry", metavar=("[URL]", "[USERNAME]"))
    my_parser.add_argument("-q", "--query", type=str, nargs = 1, help="Look up entry by URL", metavar=("[URL]"))
    my_parser.add_argument("-l", "--list", action="store_true", help="List all entries in password vault")
    my_parser.add_argument("-d", "--delete", type=str, nargs=1, help="Delete entry by URL", metavar=("[URL]")) 
    my_parser.add_argument("-ap", "--add_password", type=str, nargs=3, help="Add manual password", metavar=("[URL]", "[USERNAME]", "[PASSWORD]")) 
    my_parser.add_argument("-uurl", "--update_url", type=str, nargs=2, help="Update a URL", metavar=("[NEW_URL]", "[OLD_URL]"))
    my_parser.add_argument("-uuname", "--update_username", type=str, nargs=2, help="Update a username in account", metavar=("[URL]", "[NEW_USERNAME]")) 
    my_parser.add_argument("-upasswd", "--update_password", type=str, nargs=2, help="Update a password in account", metavar=("[URL]", "[NEW_PASSWORD]"))


    args = my_parser.parse_args()

    cursor = connection.cursor()

    connection.commit()

    if args.add:
        URL = args.add[0]
        username = args.add[1]
        password = password_generator.password_gen(20)
        password_official = master_password.encrypt_password(password, master_password_hash)
        cursor.execute(sql.insert_db_row(), (URL, username, password_official))
        print("Record Added:" + "\n URL: {0}, Username: {1}, Password: {2} (Plaintext Password)".format(URL, username, password))
        print("Record Added:" + "\n URL: {0}, Username: {1}, Password: {2} (Encrypted Ciphertext to be Stored)".format(URL, username, password_official))

    if args.query:
        URL = args.query[0]
        cursor.execute(sql.select_db_entry(), (URL, ))
        record = cursor.fetchone()
        password_field = record[2]
        decrypt_password = master_password.decrypt_password(password_field, master_password_hash)

        if bool(record):
            print("Record: " + "\n URL: {0}, Username: {1}, Password: {2}".format(record[0], record[1], decrypt_password.decode('utf-8')))
            print("Record With Encrypted Password: " + "\n URL: {0}, Username: {1}, Password: {2}".format(record[0], record[1], record[2]))
        else:
            print("Could not find record matching the value of \'%s\'" % (URL))

    if args.delete:
        URL = args.delete[0]
        sql_delete_query = """Delete from Vault where URL = %s"""
        cursor.execute(sql_delete_query, (URL, ))

    if args.add_password:
        URL = args.add_password[0]
        username = args.add_password[1]
        password = args.add_password[2]
        password_official = master_password.encrypt_password(password, master_password_hash)
        cursor.execute(sql.insert_db_row(), (URL, username, password_official))
        print("Record added with custom password.")

    if args.update_url:
        new_URL = args.update_url[0]
        old_URL = args.update_url[1]
        cursor.execute(sql.update_db_url(), (new_URL, old_URL, ))

    if args.update_username:
        new_username = args.update_username[0]
        URL = args.update_username[1]
        cursor.execute(sql.update_db_usrname(), (new_username, URL ))

    if args.update_password:
        print("Please type in old password: ")
        new_password = args.update_password[0]
        URL = args.update_password[1]
        cursor.execute(sql.update_db_passwd(), (new_password, URL ))

    if args.list:
        cursor.execute("SELECT * from Vault")
        record = cursor.fetchall()  
        for i in range(len(record)):
            entry = record[i]
            for j in range(len(entry)):
                titles = ["URL: ", "Username: ", "Password: "]
                if titles[j] == "Password: ":
                    bytes_row = entry[j]
                    password = master_password.decrypt_password(bytes_row, master_password_hash)
                    print("Password: " + str(password.decode('utf-8')))
                else:
                    print(titles[j] + entry[j])

            
            print( "----------")
    
    connection.commit()

    cursor.close()

main()

