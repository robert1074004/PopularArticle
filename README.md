# PopularArticle API
這是一個使用Django建構的API。使用到JWT驗證，讓使用者需要登入獲取JWT token，才能對文章(Article)資源做CRUD操作。

## 安裝
1.git clone 專案到本地

    git clone https://github.com/robert1074004/PopularArticle

2.進入此專案

    cd PopularArticle

3.創建並激活虛擬環境(可選)

    python -m venv env

  適用於macOS和Linux

    source env/bin/activate

  適用於windows

    env\Scripts\activate

4.下載所需要的套件

    pip install -r requirements.txt

5.配置環境變數

    touch .env

  請參考.env.example檔，設定環境變數

6.運行數據遷移

    python manage.py migrate
    
7.製作雜湊後的密碼

  請先將password.py 中 your_password替換成你想設定的密碼

    python password.py

  複製顯示在終端機的密碼，等下新增種子資料要用
    
8.新增種子資料

  請先將user_seed_data.json中的{{ MyPassword }}替換成剛才複製的密碼
  
    python manage.py loaddata user_seed_data.json
    python manage.py loaddata seed_data.json

## 啟動專案
啟動伺服器

    python manage.py runserver
API 將運行在 http://localhost:8000/ 上

## API文件

以下是可用的API和操作

### 使用者登入
* URL：/login
* 方法 : POST
* 權限要求 : 無
* 參數
  * request body | account : string / password : string
  * params | 無   
* 回應
  * JWT token
  * 狀態碼 400 Bad Request（如果请求無效）

### 瀏覽文章
* URL：/articles/< int:pk >
* 方法 : GET
* 權限要求 : 登入用戶(JWT token)
* 參數
  * request body | 無
  * params | pk : int
* 回應
  * 狀態碼 200 OK
  * 返回單篇文章的 JSON 數據
  * 狀態碼 404 Not Found（如果找不到對應的文章）

### 新增文章
* URL：/articles/
* 方法 : POST
* 權限要求 : 登入用戶(JWT token)
* 參數
  * request body | title : string  / image : URLstring / content : text / pub_date : datetime 
  * params | 無   
* 回應
  * 狀態碼 201 Created
  * 返回單篇文章的 JSON 數據
  * 狀態碼 400 Bad Request（如果请求無效）

### 修改文章
* URL：/articles/< int:pk >
* 方法 : PUT
* 權限要求 : 登入用戶(JWT token)
* 參數
  * request body | title : string  / image : URLstring / content : text / pub_date : datetime
  * params | pk : int   
* 回應
  * 狀態碼 200 OK
  * 返回單篇文章的 JSON 數據
  * 狀態碼 400 Bad Request（如果请求無效）
  * 狀態碼 404 Not Found（如果找不到對應的文章）
 
### 刪除文章
* URL：/articles/< int:pk >
* 方法 : DELETE
* 權限要求 : 登入用戶(JWT token)
* 參數
  * request body | 無
  * params | pk : int  
* 回應
  * 狀態碼 204 No Content
  * 無返回數據
  * 狀態碼 404 Not Found（如果找不到對應的文章）

## 環境建置
[Python 3.7.0](https://www.python.org/downloads/)

[PostgreSQL](https://www.postgresql.org/)

## 開發人員
Robert
