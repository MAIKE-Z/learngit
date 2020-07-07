# CSS
## 选择器
\# 选择id
. 选择类
a[title]选择标签属性
a:hover 选择伪类
a::first-line 选择伪元素
article>p 选择article的初代子元素

### li em
li里面的em标签
### .special
special类
### li + em
li后面的em标签
### a: link, a: visited
a的属性为visited或link
## 选择器优先级
内联样式(声明在style里)>ID选择器>类，属性，伪类选择器>元素，伪元素选择器
可以用！important来强制优先

## 继承
### inherit
属性名: inherit，使属性和父元素相同
### initial
使属性和浏览器默认相同
### unset
将属性重置，有inherit变inherit，没有变initial
### all
:initial, :inherit, :unset 对所有属性进行操作
## border box, content box
border box：size已经算上padding和border
content box(默认)：size只算content
## display: Flex
[Flex 布局教程：语法篇 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html)
- - - -
flex-flow: row wrap;方向，换行
```
display: flex;
align-items: center
justify-content: space-around;
```
对父元素用flex，子元素才会flex，可以对子元素用flex: 1来表示比例。 flex:1 100px,最小100px，比例1

## display: inline-block

## float
overflow
## display: grid
```    
display: grid;
grid-template-columns: 1fr 1fr; 
//repeat(auto-fill,minmax(200px,1fr))自动换列，至少为200像素
grid-gap: 10px;
```
## 居中方法
### 行内元素
text-align: center
### 定宽块状元素
margin: 0 auto
### 不定宽块状元素
```
display:flex
align-items:center
justify-content:spacing-arounding
```
float+position
inline block+text align
display:table+margin:0 auto
## 布局
多栏布局，flexbox，网格，默认都是响应式的
多栏布局： `column-count:3, column-width:10em;`
`flexbox: display:flex; 子元素flex:1;`
` grid: display: grid, grid-template-columns: 1fr 1fr` 
## 自我验证
[html、css基础考察](https://www.cnblogs.com/songjum/p/5466862.html)
## 两边固定中间自适应
* float
* absolute position
* flex
* 负margin-----margin top, margin left会向上左移动，right bottom会覆盖右下。文档流只能是后面的流向前面的，即文档流只能向左或向上流动，不能向下或向右移动。
* display: table
#学习/前端#