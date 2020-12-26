from StockDAO import stockDAO

stock1 = {
    'id': 6,
    'category': 'Stationary',
    'name': 'HandBook',
    'quantity': 120
    }

stock2 = {
    'id': 5,
    'category': 'Stationary',
    'name': 'HandBook',
    'quantity': 20
    }

#returnvalue = stockDAO.create(stock1)
#print(returnvalue)

#returnvalue = stockDAO.getAll()
#print(returnvalue)
returnValue = stockDAO.findByID(stock1['id'])
print("find By Id")
print(returnValue)

stockDAO.update(stock1['id'])
print("Update Stock id 6")
print(returnValue)
#returnValue = stockDAO.findById(stock2['id'])
#print(returnValue)

#returnValue = stockDAO.delete(stock2['id'])
#print(returnValue)
#returnValue = stockDAO.getAll()
#print(returnValue)
