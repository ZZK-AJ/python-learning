#Author:zzk
#coding=utf-8
import re
text = '''<html>
<head>
  <meta charset="UTF-8">
  <title>你好你好</title>
  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
</head>
<body>
  <div style="text-align:center;clear:both;">
    <script src="/follow.js" type="text/javascript"></script>
  </div>
  <div class='heart3d'>
    <div class='rib1'><body>akljfkjkj</body></div>
    <div class='rib2'></div>
    <div class='rib3'></div>
    <div class='rib4'></div>
  </div>
</body>
</html>'''
m = re.search(r'<body>([\s\S]*)</body>',text)

print m.group(0)



