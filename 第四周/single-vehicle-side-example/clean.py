import pymysql
import os
import json
import pandas as pd

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file.")
        return None

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
cursor.execute("USE clean")

#创建对应的表
sql = """
CREATE TABLE data_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_path VARCHAR(255),
    image_timestamp BIGINT,
    pointcloud_path VARCHAR(255),
    point_cloud_stamp BIGINT,
    calib_camera_intrinsic_path VARCHAR(255),
    calib_camera_intrinsic_json JSON,
    calib_lidar_to_camera_path VARCHAR(255),
    calib_lidar_to_camera_json JSON,
    label_camera_std_path VARCHAR(255),
    label_camera_std_json JSON,
    label_lidar_std_path VARCHAR(255),
    label_lidar_std_json JSON
)
"""
cursor.execute(sql)

with open('data_info.json', 'r') as f:
    data_info_list = json.load(f)

# 遍历 data_info_list 并插入数据到 MySQL 表中
for data_info in data_info_list:
    sql = """
    INSERT INTO data_info (
        image_path, image_timestamp, pointcloud_path, point_cloud_stamp,
        calib_camera_intrinsic_path, calib_camera_intrinsic_json,
        calib_lidar_to_camera_path, calib_lidar_to_camera_json,
        label_camera_std_path, label_camera_std_json,
        label_lidar_std_path, label_lidar_std_json
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data_info["image_path"],
        data_info["image_timestamp"],
        data_info["pointcloud_path"],
        data_info["point_cloud_stamp"],
        data_info["calib_camera_intrinsic_path"],
        json.dumps(read_json_file(data_info["calib_camera_intrinsic_path"])),
        data_info["calib_lidar_to_camera_path"],
        json.dumps(read_json_file(data_info["calib_lidar_to_camera_path"])),
        data_info["label_camera_std_path"],
        json.dumps(read_json_file(data_info["label_camera_std_path"])),
        data_info["label_lidar_std_path"],
        json.dumps(read_json_file(data_info["label_lidar_std_path"]))
    )
    cursor.execute(sql, values)

db.commit()