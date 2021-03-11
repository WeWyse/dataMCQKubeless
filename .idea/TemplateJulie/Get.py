def GetDataFromMySQL(table, column):
  import mysql.connector


  connector = mysql.connector.connect(host="http://172.17.0.3:8085/api/v1/qcm_test",
                                      user="admin", password="admin",
                                      database="dataMCQ")

  cursor = connector.cursor()
  query = ("""SELECT %s FROM %s """ %(', '.join(column),table))
  rows = cursor.fetchall()
  number = 1
  for row in rows:
    print('question ', number, ' : ', row)
    number = number + 1



# Opérations à réaliser sur la base ...
conn.close()
return
