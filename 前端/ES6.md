# ES6
## let和var
let不能重复声明，没有变量提升，可以配合for循环，块级变量，不属于window对象，会有暂时性死区(在申明前就赋值)
* let有块作用域而var没有，如果在循环中用let 声明了变量 i，那么只有在循环内，变量 i 才是可见的。
```
var i = 7;
for (var i = 0; i < 10; i++) {
  // 一些语句
}
// 此处，i 为 10

let i = 7;
for (let i = 0; i < 10; i++) {
  // 一些语句
}
// 此处 i 为 7
```
* 通过var关键词定义的全局变量属于 window 对象：
```
var carName = "porsche";
// 此处的代码可使用 window.carName
```
通过let关键词定义的全局变量不属于 window 对象：
```
let carName = "porsche";
// 此处的代码不可使用 window.carName
```
* 允许在程序的任何位置使用 var 重新声明 JavaScript 变量，而let只能声明一次，除非在不同的作用域/块。
* var的声明会提升到顶端。（只有声明可以，如果初始化赋值不行）
* 不通过关键词 var 创建的变量总是全局的，即使它们在函数中创建。
- - - -
const对象或者数组可以更改属性但是不能重新赋值，不同作用域/块可以重新赋值
## 字符串拼接
```
var str1 = `我是${name}，今年${age}岁，性别${sex}的了，爱好${hobby}`;
```
用在字符串边界加上`即可。
## ...深拷贝
```
      function show(...arr){
        arr.push(8);
        console.log(arr);
    }
    show(12,5);  //12 5 8
```

## map对象
## for...in, for...of
## 箭头函数
```
//ES5函数写法
    var sum = function(a,b){
        return a+b;
    }
    alert(sum(12,5));
//ES6函数写法
    let sum = (a,b) => {
        return a+b;
    }
    alert(sum(12,5));
  //进化一下  ---   省略花括号
    let sum = (a,b) => a+b;
    alert(sum(12,5));
```
## 继承，面向对象工厂模式
ES5需要定义父类，用this.属性来赋值，把函数挂在prototype上。在子类的定义中，用父类.apply(this.arguments)来获得父类函数。再通过子类.prototype=new 父类来获得父类的函数。最后子类.prototype.constructor=子类来覆盖构造函数。

ES6
* class，不是function
* 属性写在constructor里
* constructor和方法之间没有；，可以给属性设置初始值
```
    class Person{
        constructor(name,age=25){  //可以给属性初始值或默认值,正常es的function函数也可以给默认值
            this.name = name;
            this.age = age;
        }
        showName(){
            return this.name;   
        }
        showAge(){
            return this.age;
        }   
    }
    
    var p1 = new Person('alice',18);
    alert(p1.showAge());   // 18
```

ES6继承
```
  //父类构造函数Person
   class Person{
        constructor(name,age){
            this.name = name;
            this.age = age;
        }
        showName(){
            return this.name;   
        }
        
        showAge(){
            return this.age;
        }   
    }
//子类继承父类
    class Worker extends Person{
            constructor(name,age,job='搬砖的'){   //继承父类属性，并新加属性给默认值
            super(name,age);    
//这里必须传参，也就是需要把原来构造函数的参数传入。
//子类必须在constructor方法中调用super方法，否则新建实例时会报错。
//这是因为子类没有自己的this对象，而是继承父类的this对象，然后对其进行加工。如果不调用super方法，子类就得不到this对象。
            this.job = job;
        }
      //给子类定义新方法showJob
            showJob(){
            return this.job;
        }   

    }
    //调用
    var w1 = new Worker('rose',17);
    alert(w1.showJob());
    alert(w1.showName());
```

## export default和export的使用方式
* 导入模块：使用import模块名称from模块标识符（import表示路径）
* 暴露成员方式：使用export default和export向外暴露成员（exfault default只允许向外暴露一次，且import时可以任意指定名字）


#学习/前端#