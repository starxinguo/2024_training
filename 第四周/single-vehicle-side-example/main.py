from venv import logger
from fastapi import FastAPI,HTTPException
from fastapi.responses import FileResponse
import os
import json
from pydantic import BaseModel
import pymysql
import logging


# 连接到 MySQL 数据库
db = pymysql.connect(
    host='192.168.239.138',
    user='root',
    password='123456',
    port=3306
)
cursor = db.cursor()

app = FastAPI()

class ImageData(BaseModel):
    image_path: str
    calib_camera_intrinsic_json: str
    calib_lidar_to_camera_json: str
    label_camera_std_json: str
    label_lidar_std_json: str

cursor.execute("USE clean")
@app.get("/images/{image_filename}")
def get_image(image_filename: str):
    """
    根据图像文件名获取图像文件,如果找不到图像文件,返回 404 错误。
    """
    image_path = os.path.join("image", image_filename)
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path)

@app.get("/get_image_data_by_filename/{image_filename}")
def get_image_data_by_filename(image_filename: str):
    try:
        sql = """
        SELECT
            image_path,
            calib_camera_intrinsic_json,
            calib_lidar_to_camera_json,
            label_camera_std_json,
            label_lidar_std_json
        FROM data_info
        WHERE image_path LIKE %s
        """
        image_http_url = f"http://127.0.0.1:8000/images/{image_filename}"
        cursor.execute(sql, (f"%{image_filename}%",))
        result = cursor.fetchone()
        if result:
            return ImageData(
                image_path=image_http_url,
                calib_camera_intrinsic_json=result[1],
                calib_lidar_to_camera_json=result[2],
                label_camera_std_json=result[3],
                label_lidar_std_json=result[4]
            )
        else:
            return {"message": f"No data found for image filename '{image_filename}'"}
    except Exception as e:
        logger.error(f"Error in get_image_data_by_filename: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)