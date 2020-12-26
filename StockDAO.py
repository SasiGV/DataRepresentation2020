# Create a DAO file to interact with the Database
# Adding StockDAO to the repository
#
# Need mysql-connector to interact with the DB. Added the connector to the venv and Requirement.txt
# pip install mysql-connector

# Using the DBconfig file from the class modules
import mysql.connector
import mysql.connector.errors
import dbconfig as cfg

# Change class name here
class StockDAO:
    db = ""
    
    #def __init__(self):
    def connectToDB(self):
        self.db = mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['username'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']

        )
        #print("Connection Made")
    
    def __init__(self):
        self.connectToDB()

    # Check for cnxn, if none make one.
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()


    def create(self, values):
        cursor = self.getCursor()
        sql = "insert into stock (category, name, quantity) values (%s, %s, %s)"
        #values1 = (category, name, quantity)
        cursor.execute(sql, values)

        self.db.commit()
        lastRowID = cursor.lastrowid
        cursor.close()
        return lastRowID
        
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from stock"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def convertToDictionary(self, result):
        colnames=['Id','category','Name', "Quantity"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
stockDAO  = StockDAO()
