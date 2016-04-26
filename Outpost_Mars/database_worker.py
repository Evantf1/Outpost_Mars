import _sqlite3
import database_defaults

# TODO README
# TODO to reset the database, include this file and do database_worker.buildSchema()


def buildSchema():
    _DatabaseWorker().resetSchema()
    _DatabaseWorker().buildTables()

def findOne(sql):
    return _DatabaseWorker().selectOneWithSQL(sql)

def findAll(sql):
    return _DatabaseWorker().selectAllWithSQL(sql)

def addRecord(sql):
    return _DatabaseWorker().addRecordWithSQL(sql)

def addRecords(sql, records):
    return _DatabaseWorker().addRecordsWithSQL(sql, records)

def findNextIdForTable(table):
    return _DatabaseWorker().findNextIdForTable(table)


class _DatabaseWorker:

    _database_name = 'test.db'

    _allTables = [
        database_defaults.Tile(),
        database_defaults.Terrain(),
        database_defaults.TileStructure(),
        database_defaults.TileTerrain(),
        database_defaults.Resource(),
        database_defaults.Structure(),
        database_defaults.TileResource(),
        database_defaults.StructureResource(),
        database_defaults.StructureResourceProduction(),
        database_defaults.StructureResourceConsumption()
    ]

    @staticmethod
    def resetSchema():
        for tableWrapper in _DatabaseWorker._allTables:
            try:
                # print('Running SQL: ' + tableWrapper.dropStatement)
                _DatabaseWorker.runSql(tableWrapper.dropStatement)
            except _sqlite3.OperationalError:
                print('ERROR: resetSchema: Could not drop table. It might not exist.')

    @staticmethod
    def buildTables():
        for tableWrapper in _DatabaseWorker._allTables:
            try:
                # print('Running SQL: ' + tableWrapper.createStatement)
                _DatabaseWorker.runSql(tableWrapper.createStatement)
                # print('SUCCESS: buildTables: The table was built.')
            except _sqlite3.OperationalError:
                print('ERROR: builtTables: The table could not be built. It might already exist.')

            if tableWrapper.defaultStatements is not None:
                for insertStatement in tableWrapper.defaultStatements:
                    try:
                        # print('Running SQL: ' + insertStatement)
                        _DatabaseWorker.runSql(insertStatement)
                        # print('SUCCESS: buildTables: The table was populated.')
                    except _sqlite3.OperationalError:
                        print('ERROR: builtTables: The record could not be inserted.')

    @staticmethod
    def createConnection(database):
        _DatabaseWorker.validateSqlAndCursor(database)

        try:
            connection = _sqlite3.connect(database)
        except _sqlite3.DatabaseError:
            print('ERROR: createConnection: Could not create a connection for the given database: ' + database)

        return connection

    @staticmethod
    def commitConnection(connection):
        _DatabaseWorker.validateSqlAndCursor(connection)

        try:
            connection.commit()
            # print('SUCCESS: commitConnection: Committed the connection.')
        except _sqlite3.DatabaseError:
            print('ERROR: commitConnection: Could not commit the connection.')

    @staticmethod
    def validateSqlAndCursor(param):
        if param is None:
            # print('ERROR: function validateSqlAndCursor: provided param cannot be None.')
            raise RuntimeError

    @staticmethod
    def runSql(sql):
        _DatabaseWorker.validateSqlAndCursor(sql)

        connection = _DatabaseWorker.createConnection(_DatabaseWorker._database_name)
        cursor = connection.cursor()
        cursor.execute(sql)

        connection.commit()

    @staticmethod
    def selectOneWithSQL(sql):
        _DatabaseWorker.validateSqlAndCursor(sql)

        try:
            connection = _DatabaseWorker.createConnection(_DatabaseWorker._database_name)
            cursor = connection.cursor()
            # print('Running SQL: ' + sql)
            cursor.execute(sql)
            # print('SUCCESS: selectOneWithSQL: The select was successful.')
            return cursor.fetchone()
        except _sqlite3.OperationalError:
            # print('ERROR: selectOneWithSQL: The select failed.')
            return None

    @staticmethod
    def selectAllWithSQL(sql):
        _DatabaseWorker.validateSqlAndCursor(sql)

        try:
            connection = _DatabaseWorker.createConnection(_DatabaseWorker._database_name)
            cursor = connection.cursor()
            # print('Running SQL: ' + sql)
            cursor.execute(sql)
            # print('SUCCESS: selectAllWithSQL: The select was successful.')
            return cursor.fetchall()
        except _sqlite3.OperationalError:
            # print('ERROR: selectAllWithSQL: The select failed.')
            return None

    @staticmethod
    def addRecordWithSQL(sql):
        _DatabaseWorker.validateSqlAndCursor(sql)

        # try:
        connection = _DatabaseWorker.createConnection(_DatabaseWorker._database_name)
        cursor = connection.cursor()
        # print('Running SQL: ' + sql)
        cursor.execute(sql)
        # print('SUCCESS: addRecordWithSQL: The record was added.')
        connection.commit()
        # except _sqlite3.OperationalError:
            # print('ERROR: addRecordWithSQL: The record could not be added.')

    @staticmethod
    def addRecordsWithSQL(sql, records):
        _DatabaseWorker.validateSqlAndCursor(sql)
        _DatabaseWorker.validateSqlAndCursor(records)

        # try:
        connection = _DatabaseWorker.createConnection(_DatabaseWorker._database_name)
        cursor = connection.cursor()
        # print('Running SQL: ' + sql)
        cursor.executemany(sql, records)
        # print('SUCCESS: addRecordWithSQL: The record was added.')
        connection.commit()
        # except _sqlite3.OperationalError:
            # print('ERROR: addRecordWithSQL: The record could not be added.')

    @staticmethod
    def findNextIdForTable(table):
        _DatabaseWorker.validateSqlAndCursor(table)

        sql = 'SELECT MAX(ID) + 1 AS ID FROM ' + table

        try:
            connection = _DatabaseWorker.createConnection(_DatabaseWorker._database_name)
            cursor = connection.cursor()
            # print('Running SQL: ' + sql)
            cursor.execute(sql)
            # print('SUCCESS: findNextIdFOrTable: The ID was found for TABLE: ' + table)
            data = cursor.fetchone()
            # print(data)
            # print(data[0])
            if data[0] is None:
                return 1

            # print('Returning data')
            return data[0]
        except _sqlite3.OperationalError:
            # print('ERROR: findNextIdFOrTable: The ID could not be found for TABLE: ' + table)
            return 1
