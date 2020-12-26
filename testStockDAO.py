from StockDAO import stockDAO

stock1 = {
    'category': 'Stationary',
    'name': 'Notebook',
    'quantity': 12
    }

returnvalue = stockDAO.create(stock1)
print(returnvalue)

#returnvalue = stockDAO.getAll()
#print(returnvalue)
