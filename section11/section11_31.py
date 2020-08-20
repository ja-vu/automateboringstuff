import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon','Fat-Tail','Cleo']
#print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
f = open('c:\\Workspace\\automateboringstuff\\section11\\hello.txt','a')
f.write("Bacon is good\n\n")
f.close()
