from app.db.sql_manager import SQLManager
#from app.db.nosql_manager import NoSQLManager

class DBManager:
    def __init__(self, use_sql=True, use_nosql=True):
        self.sql = SQLManager() if use_sql else None
        #self.nosql = NoSQLManager() if use_nosql else None

    def get_sql_session(self):
        if not self.sql:
            raise RuntimeError("SQL Manager not enabled")
        return self.sql.get_session()

    def session_scope(self):
        if not self.sql:
            raise RuntimeError("SQL Manager not enabled")
        return self.sql.get_session()

    # def get_nosql_collection(self, name):
    #     if not self.nosql:
    #         raise RuntimeError("NoSQL Manager not enabled")
    #     return self.nosql.get_collection(name)

    def close(self):
        if self.sql:
            self.sql.close()
