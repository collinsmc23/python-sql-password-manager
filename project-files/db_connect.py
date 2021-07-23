import psycopg2

def connection_db(): 
    # Enter password under ******** field. 
    return psycopg2.connect("dbname=Vault-DB user=postgres password=********")
