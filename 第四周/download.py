import os
import requests
import zipfile


def download_and_extract_file(url, save_path, file_name, extract_path='.'):
    """
    下载文件并解压到指定路径

    Args:
        url (str): 下载文件的URL
        save_path (str): 文件保存路径
        file_name (str): 文件名
        extract_path (str, optional): 解压文件的路径, 默认为当前目录. Defaults to '.'.
    """
    try:
        # 确保保存路径存在
        os.makedirs(save_path, exist_ok=True)

        # 组合保存路径和文件名
        save_file_path = os.path.join(save_path, file_name)

        # 发送GET请求并获取响应
        response = requests.get(url)

        # 检查请求是否成功
        response.raise_for_status()

        # 将响应内容保存到文件中
        with open(save_file_path, 'wb') as f:
            f.write(response.content)

        print(f"文件 {file_name} 已保存到 {save_path}")

        # 解压缩文件
        with zipfile.ZipFile(save_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        print(f"文件 {file_name} 已解压到 {extract_path}")
    except requests.exceptions.RequestException as e:
        print(f"下载文件时发生错误: {e}")
    except OSError as e:
        print(f"保存或解压文件时发生错误: {e}")
    except zipfile.BadZipFile as e:
        print(f"文件 {file_name} 不是有效的 ZIP 文件: {e}")
    except Exception as e:
        print(f"未知错误: {e}")


# 指定要下载和解压的文件信息
download_url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16213950939799552.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-18T08%3A10%3A14Z%2F604800%2F%2Fb6e9563f9f028306e6a34d867cca72b312bbd0620aed5c8b3a080dc13030efac'
save_path = '/path/to/save/directory'
file_name = 'data.zip'
extract_path = '/path/to/extract/directory'

# 调用下载并解压文件的函数
download_and_extract_file(download_url, save_path, file_name, extract_path)