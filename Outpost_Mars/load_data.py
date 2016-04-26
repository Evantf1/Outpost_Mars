import database_worker
import database_defaults

# This will hard reset the schema and populate the default values
database_worker.buildSchema()

# Test a get
database_defaults.Terrain.getTerrainAll()



