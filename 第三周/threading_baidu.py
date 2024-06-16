import threading
import requests

def download_page(url):
    """下载指定URL的页面数据"""
    response = requests.get(url)
    print(f"Downloaded {url}")
    return response.text

def main():
    """主函数"""
    url = "https://www.baidu.com"

    # 创建线程
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=download_page, args=(url,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("All downloads complete.")

if __name__ == "__main__":
    main()