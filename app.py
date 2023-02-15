# coding=UTF-8
from flask import Flask
app=Flask(__name__)#_name_代表目前執行的模組
@app.route("/")#函式的裝飾(Deractor):以函視為基礎，提供附加的功能
def home():
    return 'Hello Flask '
@app.route('/test')#代表我們要處理的網站路徑
def test():
    return 'This is Test'
if __name__=='_main_':#如果以主程式執行
    app.run()#立刻啟動伺服器

