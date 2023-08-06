# PopularArticle API
這是一個使用Django建構的API。使用到JWT驗證，讓使用者需要登入獲取JWT token，才能對文章(Article)資源做CRUD操作。

## 安裝
1.git clone 專案到本地

    git clone https://github.com/robert1074004/PopularArticle

2.進入此專案

    cd PopularArticle
    

3.配置環境變數

    touch .env

  請參考.env.example檔，設定環境變數

4.配置使用者密碼

  打開PopularArticles/polls/scripts/user_seed.py，將your_password改成你想要設定的密碼

5.建置docker容器並運行

    docker-compose build

    docker-compose up

6.開啟另一個cmd或powershell , 進入django的container

    docker ps  #有兩個正在運行的service

    docker exec -it <Container ID> bash  #選擇django的service進入

7.運行數據遷移

    python manage.py migrate
       
8.新增種子資料

    python manage.py runscript user_seed
    python manage.py runscript article_seed


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
