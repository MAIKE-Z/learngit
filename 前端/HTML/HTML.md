# HTML
## sublime text 快捷键
!+tab 自动生成html代码

## 表单框架
*  [Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)  for Python （比 [Flask](http://flask.pocoo.org/) 要重量级一些，但是有更多的工具和选项。）
*  [Express](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs)  for Node.js
*  [Laravel](https://laravel.com/)  for PHP
*  [Ruby On Rails](https://rubyonrails.org/)  for Ruby
*  [Phoenix](https://phoenixframework.org/)  for Elixir
## HTML DOM
HTML DOM 是 HTML 的标准对象模型和编程接口。它定义了：
* 作为对象的 HTML 元素
* 所有 HTML 元素的属性
* 访问所有 HTML 元素的方法
* 所有 HTML 元素的事件
换言之：HTML DOM 是关于如何获取、更改、添加或删除 HTML 元素的标准。
属性为值，方法为操作
### addEventListener
addEventListener(event, function, useCapture);
useCapture，布尔类型，指定事件冒泡还是事件捕获
* event不要加on，比如要用click而不是onclick
`element.addEventListener("click", function(){ alert("Hello World!"); });`
* 当传递参数值时，以参数形式使用调用指定函数的“匿名函数”
`element.addEventListener("click", function(){ myFunction(p1, p2); });`
* 删除已有HTML元素需要先找到它的父元素，再removeChild可以用
```
var child = document.getElementById("p1");
child.parentNode.removeChild(child);
```

#学习/前端#