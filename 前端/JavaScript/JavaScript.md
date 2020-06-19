# JavaScript
## 定时器

```
let timer=null;
function autoPlay(){
	timer=setInterval(function(),time);
}

xxx.onClick=funtion(){
	clearInterval(timer);
}
```
clearInterval很有必要
setInterval返回一个定时器标记，需要有一个timer来做标记，clearInterval通过标记来清除相应的定时器
定时器方法都是在window对象上的，所以里面的this默认指向window（ window.setInteval ( function, time)；）

* 问题1：通过计时器设置自动切换焦点图，时间长了发现网页没有自动切换，哪里出了问题？怎么解决？（自动切换焦点图.html）

* 问题2：为什么要用aLi[i].index保存i，为什么直接用i不行？（自动切换焦点图.html）
```
    for(var i=0; i<aLi.length; i++){
		aLi[i].index = i;
		aLi[i].onclick = function(){
			num = this.index;
			fnTab();
			}
		}
```

答2：看起来执行函数在for循环里执行，但不是这样的，它只是绑定事件，事件触发才会执行，事件触发时页面已经加载完了，事件全部绑定，for循环肯定已经完成。onclick只在事件触发时执行，所以用this。
不能把外部循环的i带入触发事件中来，建议用this。

* 问题3：为什么autoPlay没有()（自动切换焦点图.html）？
答3：()里的是一串字符串类型的js代码，这是set和clearInterval，还有set和clearTimeout的特性，只需要函数名就行。