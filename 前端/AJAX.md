# AJAX
AJAX = Asynchronous JavaScript And XML.
AJAX组合了：
* 浏览器内建的 XMLHttpRequest 对象（从 web 服务器请求数据）
* JavaScript 和 HTML DOM（显示或使用数据）
## 特性
* 不刷新页面更新网页
* 在页面加载后从服务器请求数据
* 在页面加载后从服务器接收数据
* 在后台向服务器发送数据
```
function loadDoc() {
  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
    if (this.readyState  == 4 && this.status == 200) {
    myFunction(this);
     }
  };
  xhttp.open("GET", "music_list.xml", true);
  xhttp.send();
}
function myFunction(xml) {
  var i;
  var xmlDoc = xml.responseXML;
  var table="<tr><th>艺术家</th><th>曲目</th></tr>";
  var x = xmlDoc.getElementsByTagName("TRACK");
  for (i = 0; i <x.length;  i++) { 
    table += "<tr><td>" +
    x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue  +
    "</td><td>" +
    x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue  +
    "</td></tr>";
  }
   document.getElementById("demo").innerHTML = table;
} 
```

#学习/前端#