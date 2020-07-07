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
* clearInterval很有必要
* setInterval返回一个定时器标记，需要有一个timer来做标记，clearInterval通过标记来清除相应的定时器
* 定时器方法都是在window对象上的，所以里面的this默认指向window（ window.setInteval ( function, time)；）
- - - -
1. 问：通过计时器设置自动切换焦点图，时间长了发现网页没有自动切换，哪里出了问题？怎么解决？（自动切换焦点图.html）

2. 问：为什么要用aLi[i].index保存i，为什么直接用i不行？（自动切换焦点图.html）
```
    for(var i=0; i<aLi.length; i++){
		aLi[i].index = i;
		aLi[i].onclick = function(){
			num = this.index;
			fnTab();
			}
		}
```

答：看起来执行函数在for循环里执行，但不是这样的，它只是绑定事件，事件触发才会执行，事件触发时页面已经加载完了，事件全部绑定，for循环肯定已经完成。onclick只在事件触发时执行，所以用this。
::不能把外部循环的变量带入触发事件中来，建议用this。::可以用let解决

3. 问：为什么autoPlay没有()（自动切换焦点图.html）？
答：如果加了(), 那么会直接执行函数，而不是把存储函数的变量传给onmouseout。加括号的，就代表将会执行函数体代码。不加括号的，都是把函数名称作为函数的指针。它只是传递了函数体所在的地址位置，在需要的时候好找到函数体去执行。
::以后调用其他函数时需要注意需不要要（）::

## 闭包
1. 我的理解是，闭包就是能够读取其他函数内部变量的函数。由于在Javascript语言中，只有函数内部的子函数才能读取局部变量，因此可以把闭包简单理解成"定义在一个函数内部的函数"。
2. 闭包使得函数中的变量被保存在内存中，所以内存消耗很大，不能滥用闭包
```
　　function f1(){
　　　　let n=999;
　　　　function f2(){
　　　　　　return n;
　　　　}//闭包，使得可以在函数外部访问n
　　　　return f2;
　　}
   var result=f1();
   alert(result());
```



#学习/前端#