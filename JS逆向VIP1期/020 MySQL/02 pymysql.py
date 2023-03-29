import pymysql

# 打开数据库连接
host = 'localhost'
user = 'root'
pwd = '123456'
port = 3306
# cursorclass=pymysql.cursors.DictCursor 查询出来的结果 按照字典类型
db = pymysql.connect(database='atguigudb',host=host, user=user, password=pwd, port=port,cursorclass=pymysql.cursors.DictCursor)
print("connection successful")

# 使用cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL查询
cursor.execute("select * from countries")

# 使用 fetchone() 方法获取单条数据
data = cursor.fetchall()

print("data : %s " % data)

# 关闭数据库
db.close()

