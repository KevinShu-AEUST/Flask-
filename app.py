# coding=UTF-8
from flask import Flask
app=Flask(__name__)#_name_�N��ثe���檺�Ҳ�
@app.route("/")#�禡���˹�(Deractor):�H�������¦�A���Ѫ��[���\��
def home():
    return 'Hello Flask '
@app.route('/test')#�N��ڭ̭n�B�z���������|
def test():
    return 'This is Test'
if __name__=='_main_':#�p�G�H�D�{������
    app.run()#�ߨ�Ұʦ��A��

