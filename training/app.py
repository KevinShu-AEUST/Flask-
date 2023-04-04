
from flask import Flask#載入Flask
# coding=UTF-8

#建立Appkication 物件
app=Flask(
    __name__,
    static_folder='public',#靜態檔案的資料夾名稱
    static_url_path='/www' #靜態檔案對應的網址路徑
    )
#所有在 public 資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱

#建立路徑 / 對應的處理函式
@app.route("/")#函式的裝飾(Deractor):以函式為基礎，提供附加的功能
def home():
    return 'Hello Flask '
@app.route('/test')#代表我們要處理的網站路徑
def test():
    return 'This is Test'
@app.route('/data')#代表我們要處理的網站路徑
def testsecond():
    return 'My data'
#動態路由:建立路徑 /user/使用者名稱 對應的處理函示
#動態路由:
app.route('/user/<username>')
app.run()#立刻啟動伺服器