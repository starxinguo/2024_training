import redis

try:
    # 连接 Redis 容器
    r = redis.Redis(host='192.168.239.138', port=6379,password='123456')

    # 增 (Set)
    r.set('name', 'John Doe')
    r.set('email', 'john@example.com')

    # 查 (Get)
    name = r.get('name')
    email = r.get('email')
    print(f"Name: {name.decode()}, Email: {email.decode()}")

    # 改 (Set)
    r.set('email', 'jane@example.com')
    updated_email = r.get('email')
    print(f"Updated email: {updated_email.decode()}")

    # 删 (Delete)
    r.delete('email')
    if not r.get('email'):
        print("Email key deleted successfully!")
    else:
        print("Failed to delete email key.")

except Exception as e:
    print(f"Error: {e}")