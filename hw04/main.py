import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self，m,n):
        '''/m_row/n_col'''

        print(111112,33, type(m), type(n))
        
        m = int(m)
        n = int(n) if n is not None else m

      
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1，m+1)：
            html += '<TR>'
            for b in range(1,n+1):
                html += '<TD>%d</TD>' % ((a-1)*n+b)
            html +='</TR>' 

            html+='''

        </table>
        </body>
        <ml>
        '''


        self.write(html)

application = tornado.web.Application([
    (r"/([0-9]+)/(?:/([0-9]+))?", MainHandler),
]),debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
   

    import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self，m,n):
        '''/m_row/n_col'''

        print(111112,33, type(m), type(n))
        
        m = int(m)
        n = int(n) if n is not None else m

      
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1，m+1)：
            html += '<TR>'
            for b in range(1,n+1):
                html += '<TD>%d</TD>' % ((a-1)*n+b)
            html +='</TR>' 

            html+='''

        </table>
        </body>
        <ml>
        '''


        self.write(html)

application = tornado.web.Application([
    (r"/([0-9]+)/(?:/([0-9]+))?", MainHandler),
]),debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
   

    

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self，m,n):
        '''/m_row/n_col'''

        print(111112,33, type(m), type(n))
        
        m = int(m)
        n = int(n) if n is not None else m

      
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1，m+1)：
            html += '<TR>'
            for b in range(1,n+1):
                html += '<TD>%d</TD>' % ((a-1)*n+b)
            html +='</TR>' 

            html+='''

        </table>
        </body>
        <ml>
        '''


        self.write(html)

application = tornado.web.Application([
    (r"/([0-9]+)/(?:/([0-9]+))?", MainHandler),
]),debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
   

    
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self，m,n):
        '''/m_row/n_col'''

        print(111112,33, type(m), type(n))
        
        m = int(m)
        n = int(n) if n is not None else m

      
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1，m+1)：
            html += '<TR>'
            for b in range(1,n+1):
                html += '<TD>%d</TD>' % ((a-1)*n+b)
            html +='</TR>' 

            html+='''

        </table>
        </body>
        <ml>
        '''


        self.write(html)

application = tornado.web.Application([
    (r"/([0-9]+)/(?:/([0-9]+))?", MainHandler),
]),debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
   

    
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self，m,n):
        '''/m_row/n_col'''

        print(111112,33, type(m), type(n))
        
        m = int(m)
        n = int(n) if n is not None else m

      
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1，m+1)：
            html += '<TR>'
            for b in range(1,n+1):
                html += '<TD>%d</TD>' % ((a-1)*n+b)
            html +='</TR>' 

            html+='''

        </table>
        </body>
        <ml>
        '''


        self.write(html)

application = tornado.web.Application([
    (r"/([0-9]+)/(?:/([0-9]+))?", MainHandler),
]),debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
   

