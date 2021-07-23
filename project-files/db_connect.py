import psycopg2

def connection_db(): 
    connection = psycopg2.connect("dbname=Vault-DB user=postgres password=docker") 
    return connection