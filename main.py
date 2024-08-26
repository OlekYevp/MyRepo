from workFunctions.workFunc import getInfoWithFolder, setUpDate, engine

main_path = '/Users/oleksandrevpak/Desktop/itunes_dataset'

fileArray = getInfoWithFolder(main_path)
dataFra=setUpDate(fileArray)

conn = engine.connect()

dataFra.to_sql('sub_event', schema='public', con=conn, if_exists='replace', index=False)
conn.close()

# dataFra.to_csv('DataTest.csv')
# print(dataFra)