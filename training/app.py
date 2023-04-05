from flask import Flask #載入Flask
from flask import request #載入 Request物件
# coding=UTF-8

#建立Appkication 物件
app=Flask(
    __name__,
    static_folder='public',#靜態檔案的資料夾名稱
    static_url_path='/www' #靜態檔案對應的網址路徑
    )
#所有在 public 資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱

#建立路徑 / 對應的處理函式
@app.route('/')
def index():
    # print('請求方法',request.method)
    # print('通訊協定',request.scheme)
    # print('主機名稱',request.host)
    # print('路徑',request.path)
    # print('完整的網址',request.url)
    # print('瀏覽器和作業系統',request.headers.get('user-agent'))
    # print('語言偏好',request.headers.get('accept-language'))
    # print('引薦網址',request.headers.get('referrer'))
    lang=request.headers.get('accept-language')
    print('語言偏好',lang)
    if lang.startswith('en'):
        return 'Hello Flask '
    else:
        return '您好，歡迎光臨'
    
        
    


    
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