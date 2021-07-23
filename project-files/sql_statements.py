

def insert_db_row():
    return """INSERT INTO Vault (URL, USRNAME, PASSWD) VALUES (%s, %s,%s)""" 
    
def delete_db_row(): 
    return """Delete from Vault where URL = %s"""

def update_db_url():
    return """UPDATE Vault SET url = %s WHERE url = %s"""

def update_db_usrname():
    return """UPDATE Vault SET usrname = %s WHERE url = %s""" 

def update_db_passwd():
    return """UPDATE Vault SET passwd = %s WHERE url = %s"""

def select_db_entry():
    return """SELECT * from vault where url = %s"""

def update_db():
    return """UPDATE Vault SET passwd = %s"""
