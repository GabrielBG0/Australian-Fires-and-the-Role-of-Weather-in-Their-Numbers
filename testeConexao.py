import psycopg2

con = psycopg2.connect(dbname='datawarehouse',
                       host='localhost', user='gabriel', password='gyfu')
con.close()
