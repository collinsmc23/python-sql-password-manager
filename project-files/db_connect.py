import psycopg2

def connection_db(): 
    # Enter password under ******** field. 
    connection = psycopg2.connect("dbname=Vault-DB user=postgres password=********") 
    return connection
