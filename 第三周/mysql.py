import pymysql

try:
    # 连接 MySQL 数据库
    db = pymysql.connect(
        host='192.168.239.138',
        user='root',
        password='123456',
        port=3306
    )

    # 创建游标对象
    cursor = db.cursor()

    # 切换到 my_database 数据库
    cursor.execute("USE my_database")

    # 增 (Insert)
    new_data = [
        ('John Doe', 'john@example.com'),
        ('Jane Smith', 'jane@example.com')
    ]
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.executemany(sql, new_data)
    db.commit()
    print("Data inserted successfully!")

    # 查 (Select)
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # 改 (Update)
    update_data = ('Jane Doe', 'jane@example.com', 2)
    sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
    cursor.execute(sql, update_data)
    db.commit()
    print("Data updated successfully!")

    # 再查一次,确认更新
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # 删 (Delete)
    delete_id = 1
    sql = "DELETE FROM users WHERE id=%s"
    cursor.execute(sql, (delete_id,))
    db.commit()
    print("Data deleted successfully!")

    # 最后再查一次,确认删除
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # 关闭连接
    cursor.close()
    db.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")
    db.rollback()