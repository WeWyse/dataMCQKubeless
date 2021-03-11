def getQuestionAndCaptureAnswer(table, column):
  import mysql.connector


  connector = mysql.connector.connect(host="http://172.17.0.3:8085/api/v1/qcm_test",
                                      user="admin", password="admin",
                                      database="dataMCQ")

  cursor = connector.cursor()
  query = ("""SELECT %s FROM %s """ %(', '.join(column),table))
  cursor.execute(query)
  rows = cursor.fetchall()
  number = 1
  for row in rows:
    print('question ', number, ' : ', row[0])
    number = number + 1
    print('Réponse A :', row[1])
    print('Réponse B :', row[2])
    print('Réponse C :', row[3])
    print('Réponse D :', row[4])

  res = str(input())
# attraper reponse

  conn.close()
  return res
