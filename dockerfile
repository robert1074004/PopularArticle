#指定使用python的版本
FROM python:3.7

# 將 PYTHONUNBUFFERED 設定為 1，可以確保 Python 直接將輸出寫入標準輸出流（stdout），這樣在 Docker 容器中運行 Django 時，你可以即時看到應用的輸出日誌和訊息，而不需要等到緩衝區填滿後才顯示。開發和調試 Django 應用時特別有用
ENV PYTHONUNBUFFERED 1

# 創建並設置工作目錄
WORKDIR /PopularArticles

# 將你的 Django 專案文件複製到容器中
# COPY . /PopularArticles/

#複製requirements.txt 到容器中
COPY requirements.txt requirements.txt

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt
# --no-cache-dir 是 pip install 的一個選項，用於告訴 pip 在安裝 Python 套件時不使用緩存目錄。

# 公開 Django 應用所使用的端口（預設是 8000）
EXPOSE 8000


# 執行 Django 開發伺服器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#使用 "0.0.0.0:8000" 是為了讓容器內的 Django 服務可以通過主機的網路接口對外提供服務，而不僅僅是在容器內部訪問。假如是用127.0.0.1:8000只能在容器內部的網路接口上監聽，而無法通過容器外部的網路接口訪問。