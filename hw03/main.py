import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<html>

<head>
    <meta charset="utf-8">
    <title>乘法表</title>

    <script type="text/javascript">
        function getvalue(){
            var n = document.getElementById("a1").value;
            if (n > 0 && n < 10) {
                document.write("<table style='border-collapse: collapse;'>");
                for (var i = 1; i <= n; i++) {
                    document.write('<tr>');
                    for (var j = 1; j <= n; j++){
                        document.write('<td style="border:#CC0000 1px solid;width:1em;height:1em;">'+i*j+'</td>'); 
                    }
                    document.write('</tr>');
                }
                document.write('</table>');
            } 
            else alert("请输入1-9之间的数字！")
        }
    </script>

    <style>
       
    </style>
</head>

<body>
    <input type="text" id="a1" placeholder="请输入数字1-9">
    <input type="button" value="确认" onclick="getvalue()">
</body>

</html>")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
