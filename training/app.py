from flask import Flask #載入Flask
from flask import request #載入 Request物件
from flask import redirect #載入redirect函式
import json
# coding=UTF-8

#建立Application 物件
app=Flask(
    __name__,
    static_folder='public',#靜態檔案的資料夾名稱
    static_url_path='/' #靜態檔案對應的網址路徑
    )
#所有在 public 資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱
#建立路徑/getSum對應的處理函示
#利用要求字串(Query String)提供彈性 : /getSum?max=最大數字
@app.route('/getSum')
def getSum(): #min+(min+1)+(min+2)+(min+3)+...+max
    #接收要求字串中的參數資料
    maxNumber=request.args.get('max',100)
    maxNumber=int(maxNumber)
    minNumber=request.args.get('min',1)
    minNumber=int(minNumber)
    #以下運算 min+(min+1)+(min+2)+(min+3)+...+max 總和的迴圈邏輯
    result=0
    for n in range(minNumber,maxNumber+1):
        result=result+n
    return '結果:' + str(result)

#建立路徑 / 對應的處理函式
@app.route('/')
def index():
    lang=request.headers.get('accept-language')
    if lang.startswith('en'):
        return redirect('/en/')
    else:
        return redirect('/zh/') 
    # print('請求方法',request.method)
    # print('通訊協定',request.scheme)
    # print('主機名稱',request.host)
    # print('路徑',request.path)
    # print('完整的網址',request.url)
    # print('瀏覽器和作業系統',request.headers.get('user-agent'))
    # print('語言偏好',request.headers.get('accept-language'))
    # print('引薦網址',request.headers.get('referrer'))
    #print('語言偏好',lang)
#建立路徑 /en/ 對應的處理函式
@app.route('/en/')
def index_english():
    return json.dumps({
        'status':'ok',
        'text':'Hello World'
    })   
#建立路徑 /zh/ 對應的處理函式
@app.route('/zh/')
def index_chinese():
    return json.dumps({
        'status':'ok',
        'text':'您好，歡迎光臨'
    },ensure_ascii=False)  #指示不要用 ASCII 編碼處理中文
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