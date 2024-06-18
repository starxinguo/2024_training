import zipfile

# 创建ZipFile对象
with zipfile.ZipFile('data.zip', 'r') as zip_ref:
    # 解压缩文件到当前目录
    zip_ref.extractall('.')