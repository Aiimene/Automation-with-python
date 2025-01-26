import camelot 
#first install the library camelot-py and before that we have to install tk and ghostscript
#Camelot, a popular library for extracting tables from PDFs

tables = camelot.read_pdf("foo.pdf", pages="1", flavor="stream")
print(tables) # -> <TableList n=1> thats means there one table

# export file into csv file

tables.export("foo.csv" , f="csv" , compress=True)
tables[0].to_csv("foo.csv")
