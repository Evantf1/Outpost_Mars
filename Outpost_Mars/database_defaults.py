import database_worker


class Terrain:
    createStatement = 'CREATE TABLE TERRAIN (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(50), FILE_NAME VARCHAR(50), PASSIBILITY INTEGER)'
    dropStatement = 'DROP TABLE TERRAIN'

    defaultStatements = [
        "INSERT INTO TERRAIN (ID, NAME, FILE_NAME, PASSIBILITY) VALUES (1, 'Easy', 'terrain_easy.png', 0)",
        "INSERT INTO TERRAIN (ID, NAME, FILE_NAME, PASSIBILITY) VALUES (2, 'Moderate', 'terrain_moderate.png', 1)",
        "INSERT INTO TERRAIN (ID, NAME, FILE_NAME, PASSIBILITY) VALUES (3, 'Rough', 'terrain_rough.png', 2)",
        "INSERT INTO TERRAIN (ID, NAME, FILE_NAME, PASSIBILITY) VALUES (4, 'Impassible', 'terrain_impassible.png', 3)"
    ]

    @staticmethod
    def getTerrainById(id):
        # print(data)
        return database_worker.findAll('SELECT * FROM TERRAIN WHERE ID = ' + id)

    @staticmethod
    def getTerrainAll():
        # print(data)
        return database_worker.findAll('SELECT * FROM TERRAIN')

    @staticmethod
    def getTerrainByName(name):
        # print(data)
        return database_worker.findAll('SELECT * FROM TERRAIN WHERE NAME = ' + name)

    @staticmethod
    def getTerrainByPassibility(passibility):
        # print(data)
        return database_worker.findAll('SELECT * FROM TERRAIN WHERE PASSIBILITY = ' + passibility)

    @staticmethod
    def getTerrainByFileName(fileName):
        # print(data)
        return database_worker.findAll('SELECT * FROM TERRAIN WHERE FILE_NAME = ' + fileName)

    @staticmethod
    def createTerrain(name, fileName, passibility):
        database_worker.addRecord('INSERT INTO TERRAIN (NAME, FILE_NAME, PASSIBILITY) VALUES (' + name + ', ' + fileName + ', ' + passibility + ')')


class Structure:
    createStatement = 'CREATE TABLE STRUCTURE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(50), FILE_NAME VARCHAR(50))'
    dropStatement = 'DROP TABLE STRUCTURE'

    defaultStatements = [
        "INSERT INTO STRUCTURE (ID, NAME, FILE_NAME) VALUES (1, 'Fueler', 'structure_fueler.png')",
        "INSERT INTO STRUCTURE (ID, NAME, FILE_NAME) VALUES (2, 'Habitat', 'structure_habitat.png')",
        "INSERT INTO STRUCTURE (ID, NAME, FILE_NAME) VALUES (3, 'Horticulture', 'structure_horticulture.png')",
        "INSERT INTO STRUCTURE (ID, NAME, FILE_NAME) VALUES (4, 'Recycler', 'structure_recycler.png')",
        "INSERT INTO STRUCTURE (ID, NAME, FILE_NAME) VALUES (5, 'Lander', 'structure_lander.png')"
    ]

    @staticmethod
    def getStructureById(id):
        # print(data)
        return database_worker.findAll('SELECT * FROM STRUCTURE WHERE ID = ' + id)

    @staticmethod
    def getStructureAll():
        sql = 'SELECT * FROM STRUCTURE'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureByName(name):
        sql = 'SELECT * FROM STRUCTURE WHERE NAME = ' + name
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureByFileName(fileName):
        sql = 'SELECT * FROM STRUCTURE WHERE FILE_NAME = ' + fileName
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureByGivenField(field, value):
        sql = 'SELECT * FROM STRUCTURE WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createStructure(name, fileName):
        database_worker.addRecord('INSERT INTO STRUCTURE (NAME, FILE_NAME) VALUES (' + name + ', ' + fileName + ')')


class Resource:
    createStatement = 'CREATE TABLE RESOURCE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(50))'
    dropStatement = 'DROP TABLE RESOURCE'

    defaultStatements = [
        "INSERT INTO RESOURCE (ID, NAME) VALUES (1, 'Resource A')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (2, 'Resource B')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (3, 'Resource C')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (4, 'Resource F')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (5, 'Water')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (6, 'Electricity')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (7, 'Food')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (8, 'Air')",
        "INSERT INTO RESOURCE (ID, NAME) VALUES (9, 'Waste')"
    ]

    @staticmethod
    def getResourceById(id):
        sql = 'SELECT * FROM RESOURCE WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getResourceAll():
        sql = 'SELECT * FROM RESOURCE'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getResourceByName(name):
        sql = 'SELECT * FROM RESOURCE WHERE NAME = ' + name
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getResourceByGivenField(field, value):
        sql = 'SELECT * FROM RESOURCE WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createResource(name):
        database_worker.addRecord('INSERT INTO RESOURCE (NAME) VALUES (' + name + ')')


class Tile:
    createStatement = 'CREATE TABLE TILE (ID INTEGER PRIMARY KEY AUTOINCREMENT, X INTEGER, Y INTEGER, Z INTEGER)'
    dropStatement = 'DROP TABLE TILE'

    defaultStatements = []

    @staticmethod
    def getTileById(id):
        sql = 'SELECT * FROM TILE WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileAll():
        sql = 'SELECT * FROM TILE'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileByX(x):
        sql = 'SELECT * FROM TILE WHERE X = ' + x
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileByY(y):
        sql = 'SELECT * FROM TILE WHERE Y = ' + y
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileByZ(z):
        sql = 'SELECT * FROM TILE WHERE Z = ' + z
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileByXYZ(x, y, z):
        sql = 'SELECT * FROM TILE WHERE X = ' + x + ' AND Y = ' + y + ' AND Z = ' + z
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileByGivenField(field, value):
        sql = 'SELECT * FROM TILE WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createTile(x, y, z):
        database_worker.addRecord('INSERT INTO TILE (X, Y, Z) VALUES (' + str(x) + ', ' + str(y) + ', ' + str(z) + ')')

    @staticmethod
    def createTiles(records):
        database_worker.addRecords('INSERT INTO TILE (X, Y, Z) VALUES (?, ?, ?)', records)


class StructureResource:
    createStatement = 'CREATE TABLE STRUCTURE_RESOURCE (ID INTEGER PRIMARY KEY AUTOINCREMENT, STRUCTURE_ID INTEGER, RESOURCE_ID INTEGER, QUANTITY INTEGER, MAX INTEGER)'
    dropStatement = 'DROP TABLE STRUCTURE_RESOURCE'

    defaultStatements = []

    @staticmethod
    def getStructureResourceById(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceAll():
        sql = 'SELECT * FROM STRUCTURE_RESOURCE'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceByStructureId(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE WHERE STRUCTURE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceByResourceId(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE WHERE RESOURCE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceByQuantity(quantity):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE WHERE QUANTITY = ' + quantity
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceByMax(max):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE WHERE MAX = ' + max
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceByGivenField(field, value):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createStructureResource(structureId, resourceId, quantity, max):
        database_worker.addRecord('INSERT INTO STRUCTURE_RESOURCE (STRUCTURE_ID, RESOURCE_ID, QUANTITY, MAX) VALUES (' + structureId + ', ' + resourceId + ', ' + quantity + ', ' + max + ')')


class StructureResourceConsumption:
    createStatement = 'CREATE TABLE STRUCTURE_RESOURCE_CONSUMPTION (ID INTEGER PRIMARY KEY AUTOINCREMENT, STRUCTURE_ID INTEGER, RESOURCE_ID INTEGER, QUANTITY INTEGER)'
    dropStatement = 'DROP TABLE STRUCTURE_RESOURCE_CONSUMPTION'

    defaultStatements = [
        "INSERT INTO STRUCTURE_RESOURCE_CONSUMPTION (ID, STRUCTURE_ID, RESOURCE_ID, QUANTITY) VALUES (1, 1, 6, 1)",
        "INSERT INTO STRUCTURE_RESOURCE_CONSUMPTION (ID, STRUCTURE_ID, RESOURCE_ID, QUANTITY) VALUES (2, 1, 1, 10)"
    ]

    @staticmethod
    def getStructureResourceConsumptionById(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_CONSUMPTION WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceConsumptionAll():
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_CONSUMPTION'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceConsumptionByStructureId(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_CONSUMPTION WHERE STRUCTURE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceConsumptionByResourceId(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_CONSUMPTION WHERE RESOURCE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceConsumptionByQuantity(quantity):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_CONSUMPTION WHERE QUANTITY = ' + quantity
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceConsumptionByGivenField(field, value):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_CONSUMPTION WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createStructureResourceConsumption(structureId, resourceId, quantity):
        database_worker.addRecord('INSERT INTO STRUCTURE_RESOURCE_CONSUMPTION (STRUCTURE_ID, RESOURCE_ID, QUANTITY) VALUES (' + structureId + ', ' + resourceId + ', ' + quantity + ')')


class StructureResourceProduction:
    createStatement = 'CREATE TABLE STRUCTURE_RESOURCE_PRODUCTION (ID INTEGER PRIMARY KEY AUTOINCREMENT, STRUCTURE_ID INTEGER, RESOURCE_ID INTEGER, QUANTITY INTEGER)'
    dropStatement = 'DROP TABLE STRUCTURE_RESOURCE_PRODUCTION'

    defaultStatements = [
        "INSERT INTO STRUCTURE_RESOURCE_PRODUCTION (ID, STRUCTURE_ID, RESOURCE_ID, QUANTITY) VALUES (1, 1, 6, 2)",
        "INSERT INTO STRUCTURE_RESOURCE_PRODUCTION (ID, STRUCTURE_ID, RESOURCE_ID, QUANTITY) VALUES (2, 1, 1, 2)",
        "INSERT INTO STRUCTURE_RESOURCE_PRODUCTION (ID, STRUCTURE_ID, RESOURCE_ID, QUANTITY) VALUES (3, 1, 2, 1)",
    ]

    @staticmethod
    def getStructureResourceProductionById(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_PRODUCTION WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceProductionAll():
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_PRODUCTION'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceProductionByStructureId(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_PRODUCTION WHERE STRUCTURE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceProductionByResourceId(id):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_PRODUCTION WHERE RESOURCE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceProductionByQuantity(quantity):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_PRODUCTION WHERE QUANTITY = ' + quantity
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getStructureResourceProductionByGivenField(field, value):
        sql = 'SELECT * FROM STRUCTURE_RESOURCE_PRODUCTION WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createStructureResourceProduction(structureId, resourceId, quantity):
        database_worker.addRecord('INSERT INTO STRUCTURE_RESOURCE_PRODUCTION (STRUCTURE_ID, RESOURCE_ID, QUANTITY) VALUES (' + structureId + ', ' + resourceId + ', ' + quantity + ')')


class TileTerrain:
    createStatement = 'CREATE TABLE TILE_TERRAIN (ID INTEGER PRIMARY KEY AUTOINCREMENT, TILE_ID INTEGER, TERRAIN_ID INTEGER)'
    dropStatement = 'DROP TABLE TILE_TERRAIN'

    defaultStatements = []

    @staticmethod
    def getTileTerrainById(id):
        sql = 'SELECT * FROM TILE_TERRAIN WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileTerrainAll():
        sql = 'SELECT * FROM TILE_TERRAIN'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileTerrainByTileId(id):
        sql = 'SELECT * FROM TILE_TERRAIN WHERE TILE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileTerrainByTerrainId(id):
        sql = 'SELECT * FROM TILE_TERRAIN WHERE TERRAIN_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileTerrainByGivenField(field, value):
        sql = 'SELECT * FROM TILE_TERRAIN WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createTileTerrain(tileId, terrainId):
        database_worker.addRecord('INSERT INTO TILE_TERRAIN (TILE_ID, TERRAIN_ID) VALUES (' + tileId + ', ' + terrainId + ')')


class TileStructure:
    createStatement = 'CREATE TABLE TILE_STRUCTURE (ID INTEGER PRIMARY KEY AUTOINCREMENT, TILE_ID INTEGER, STRUCTURE_ID INTEGER)'
    dropStatement = 'DROP TABLE TILE_STRUCTURE'

    defaultStatements = []

    @staticmethod
    def getTileStructureById(id):
        sql = 'SELECT * FROM TILE_STRUCTURE WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileStructureAll():
        sql = 'SELECT * FROM TILE_STRUCTURE'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileStructureByTileId(id):
        sql = 'SELECT * FROM TILE_STRUCTURE WHERE TILE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileStructureByStructureId(id):
        sql = 'SELECT * FROM TILE_STRUCTURE WHERE STRUCTURE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileStructureByGivenField(field, value):
        sql = 'SELECT * FROM TILE_STRUCTURE WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createTileStructure(tileId, structureId):
        database_worker.addRecord('INSERT INTO TILE_STRUCTURE (TILE_ID, STRUCTURE_ID) VALUES (' + tileId + ', ' + structureId + ')')


class TileResource:
    createStatement = 'CREATE TABLE TILE_RESOURCE (ID INTEGER PRIMARY KEY AUTOINCREMENT, TILE_ID INTEGER, RESOURCE_ID INTEGER, QUANTITY INTEGER)'
    dropStatement = 'DROP TABLE TILE_RESOURCE'

    defaultStatements = []

    @staticmethod
    def getTileResourceById(id):
        sql = 'SELECT * FROM TILE_RESOURCE WHERE ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileResourceAll():
        sql = 'SELECT * FROM TILE_RESOURCE'
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileResourceByTileId(id):
        sql = 'SELECT * FROM TILE_RESOURCE WHERE TILE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileResourceByResourceId(id):
        sql = 'SELECT * FROM TILE_RESOURCE WHERE RESOURCE_ID = ' + id
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileResourceByResourceId(quantity):
        sql = 'SELECT * FROM TILE_RESOURCE WHERE QUANTITY = ' + quantity
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def getTileResourceByGivenField(field, value):
        sql = 'SELECT * FROM TILE_RESOURCE WHERE ' + field.upper() + ' = ' + value
        data = database_worker.findAll(sql)
        # print(data)
        return data

    @staticmethod
    def createTileResource(tileId, resourceId, quantity):
        database_worker.addRecord('INSERT INTO TILE_RESOURCE (TILE_ID, RESOURCE_ID, QUANTITY) VALUES (' + tileId + ', ' + resourceId + ', ' + quantity + ')')


