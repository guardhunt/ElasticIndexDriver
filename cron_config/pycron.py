import datetime

with open("testDateInfo.txt", "a") as outFile:
  print(str(datetime.datetime.now()))
  outFile.write('\n'+str(datetime.datetime.now()))

