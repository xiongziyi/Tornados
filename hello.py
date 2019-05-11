import  tornado.web
import  tornado.ioloop
import  os
import  pymysql
class IndexHander(tornado.web.RequestHandler):
    def get(self):
        name = self.get_cookie("name")
        if name is None:
            name = "您未登录"
            self.render('login.html',name = name)
        else:
            # 配置模板
            self.render('login.html', name=name)
class picHander(tornado.web.RequestHandler):
    def get(self):
        if not self.get_cookie("name"):
            self.redirect('/index')
        else:
            name = self.get_cookie("name")
            print(name)
            self.render('pic.html',name=name)
class loginHander(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')
        password = self.get_body_argument('password')
        # 连接mysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='project')
        cursor = conn.cursor()
        temp = "insert into user_info (user_name,user_password) values ('%s','%s')" % (name,password)
        effect_row = cursor.execute(temp)
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if result:
            self.write('登录成功！')
        else:
            self.write('登录失败！')
        if  name !=None and password!=None:
            self.set_cookie("name", name, expires_days=10)
            # upload_path = os.path.join(os.path.dirname(__file__),'upload_files')  上传路径
            upload_path = os.path.join(os.path.dirname(__file__), 'statics\image')
            file_data  =  self.request.files['avatar']
            for meta in file_data:
                filename = meta['filename']
                filepath = os.path.join(upload_path, filename)
                with open(filepath,'wb') as f:
                    f.write(meta['body'])
            print("上传成功")
            self.redirect('index/pic')
class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
        <html>
          <head><title>Upload File</title></head>
          <body>
            <form action='file' enctype="multipart/form-data" method='post'>
            <input type='file' name='file'/><br/>
            <input type='submit' value='submit'/>
            </form>
          </body>
        </html>
        ''')

    def post(self):
        #文件的暂存路径
        upload_path=os.path.join(os.path.dirname(__file__),'upload_files')
        #提取表单中‘name’为‘file’的文件元数据
        file_metas=self.request.files['file']
        for meta in file_metas:
            filename=meta['filename']
            filepath=os.path.join(upload_path,filename)
            #有些文件需要已二进制的形式存储，实际中可以更改
            with open(filepath,'wb') as up:
                up.write(meta['body'])
            self.write('finished!')

    def post(self, filename):
        print('i download file handler : ', filename)
        # Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        # 读取的模式需要根据实际情况进行修改
        buf_size = 4096
        download_path = os.path.join(os.path.dirname(__file__), 'upload_files')
        with open(os.path.join(download_path,filename), 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                self.write(data)
        # 记得要finish
        self.finish()

def make_app():
    return  tornado.web.Application([
        (r"/index",IndexHander),
        (r"/login", loginHander),
        (r"/index/pic",picHander),
        (r'/file', UploadFileHandler),
    ],
    debug=True,
    template_path = 'templates',
    static_path='statics',
    # static_url_prefix='/static/'
    )#配置模板
if __name__== "__main__":
    app =  make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()