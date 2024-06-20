import pymysql

class DBConnection:
    def __init__(self, host, user, password, port, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except pymysql.Error as e:
            print(f"Error closing database connection: {e}")

    def execute(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error executing SQL: {e}")
            return None

    def execute_and_fetchone(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchone()
        except pymysql.Error as e:
            print(f"Error executing SQL: {e}")
            return None

    def commit(self):
        try:
            self.connection.commit()
        except pymysql.Error as e:
            print(f"Error committing changes: {e}")

'''
db = DBConnection(host='192.168.239.138', user='root', password='123456', port=3306, database='clean')
db.connect()

# 执行 SQL 查询
result = db.execute("SELECT * FROM data_info")
print(result)

# 提交事务
db.commit()

# 关闭连接
db.close()
'''