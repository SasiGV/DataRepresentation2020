from StockDAO import stockDAO

stock1 = {
    'id': 16,
    'category': 'Stationary',
    'name': 'HandBook',
    'quantity': 500
    }

stock2 = {
    'id': 8,
    'category': 'Stationary',
    'name': 'HandBook',
    'quantity': 330
    }

#returnvalue = stockDAO.create(stock1)
#print(returnvalue)

#returnvalue = stockDAO.getAll()
#print(returnvalue)
returnValue = stockDAO.findByID(stock1['id'])
print("find By Id")
print(returnValue)

#returnValue= stockDAO.update(16)
#print("Update Stock id ", stock1['id'])
#print(returnValue)
#returnValue = stockDAO.findByID(stock2['id'])
#print(returnValue)

#returnValue = stockDAO.delete(stock2['id'])
#print(returnValue)
#returnValue = stockDAO.getAll()
#print(returnValue)

#Update Test
#stockDAO.update((200,4))
#result = stockDAO.findByID(4)
#print(result)
