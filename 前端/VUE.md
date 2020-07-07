# VUE
![](VUE/(null))
![](VUE/66C2FC9E-54E2-4ED1-9040-8B40CCBFBBDA.png)
## 安装
1. 安装在~ 
sudo npm install -g vue-cli
3.0 安装 sudo npm install -g @vue/cli
2.9.6 安装 npm install vue-cli -g

在项目目录下sudo vue init webpack vue_project
cd vue_project
sudo cnpm install
npm run dev
访问 localhost:8080[vue_project](http://localhost:8080/)


init  从模板生成新项目
list   列出可用的官方模板
build  创建新项目的原型
create 创建（警告：仅用于v3以上版本）
vue ui  启动脚手架图形界面（3.0以上版本）

npm install 安装依赖
npm run dev 或 npm run serve 启动项目

2. 下载vue文件直接饮用
3. CDN
```
<!-- 开发环境版本，包含了有帮助的命令行警告 -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<!-- 生产环境版本，优化了尺寸和速度 -->
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
```
## 模板语法
* 只插值一次` <span v-once>{{msg}}</span>`
* 原始HTML`<p>Using v-html directive: <span v-html="rawHtml"></span></p>`
* 属性`<div v-bind:id="dynamicId"></div>`    `<button v-bind:disabled="isButtonDisabled">Button</button>`
* `<p v-if="seen">现在你看到我了</p>   seen=ture`
* 动态参数`<a v-bind:[attributeName]="url"> ... </a>` 会强制转化参数名为小写
* 修饰符`<form v-on:submit.prevent="onSubmit">...</form>` event.preventDefault()
* 缩写
```
<!-- 完整语法 -->
<a v-bind:href="url">...</a>

<!-- 缩写 -->
<a :href="url">...</a>

<!-- 动态参数的缩写 (2.6.0+) -->
<a :[key]="url"> ... </a>
```

```
<!-- 完整语法 -->
<a v-on:click="doSomething">...</a>

<!-- 缩写 -->
<a @click="doSomething">...</a>

<!-- 动态参数的缩写 (2.6.0+) -->
<a @[event]="doSomething"> ... </a>
```
* 计算属性缓存VS方法
计算属性(computed)只有在相关响应式依赖发生改变时才会重新求值。
方法(methods)在每次触发重新渲染时都会再次执行。
* 侦听器 watch，适用于当数据变化时需要执行异步或者开销较大的操作。
## Class和style的绑定
* `<div v-bind:class="{ active: isActive }"></div>`  active这个class是否存在取决于isActive的true or false。这2个名字随意。动态绑定可以和普通的class attribute共存，也可以多个动态绑定
* 数组语法`<div v-bind:class="[activeClass, errorClass]"></div>`
`<div v-bind:class="[isActive ? activeClass : '']"></div>`==`<div v-bind:class="{ active: isActive }"></div>`
## V-if和V-show
```
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```
v-if只有在指令表达式为truthy值时被渲染，如果部位truthy，不渲染
v-show任何时候都会渲染，只是display会变成none
一般来说，v-if 有更高的切换开销，而 v-show 有更高的初始渲染开销。因此，如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。
v-for和v-if一起使用时，v-for有更高的优先级
## 列表渲染
```
<div v-for="item in items" v-bind:key="item.id">
  <!-- 内容 -->
</div>
```
## 事件处理
v-on=“xxx”缩写@xxx
特殊变量@event 访问原始DOM事件
修饰符
* .stop
* .prevent
* .capture
* .self
* .once
* .passive
### .exact修饰符
```
<!-- 即使 Alt 或 Shift 被一同按下时也会触发 -->
<button v-on:click.ctrl="onClick">A</button>

<!-- 有且只有 Ctrl 被按下的时候才触发 -->
<button v-on:click.ctrl.exact="onCtrlClick">A</button>

<!-- 没有任何系统修饰符被按下的时候才触发 -->
<button v-on:click.exact="onClick">A</button>
```
## 绑定表单
```
<input v-model="message" placeholder="edit me">
<p>Message is: {{ message }}</p>
```
* 双向绑定，在input中输入了值更改了message属性的值，那么p标签中message的值也会改变。
```
<!-- 当选中时，`picked` 为字符串 "a" -->
<input type="radio" v-model="picked" value="a">

<!-- `toggle` 为 true 或 false -->
<input type="checkbox" v-model="toggle">

<!-- 当选中第一个选项时，`selected` 为字符串 "abc" -->
<select v-model="selected">
  <option value="abc">ABC</option>
</select>
```
+ 通过更改value值来改变selected值，如果要绑定到Vue实例上，要用v-bind
修饰符
* v-model.lazy 在“change”时而非“input”时更新
* .number 自动将用户的输入值转为数值类型
* .trim 自动过滤用户输入的首尾空白字符
## 组件
```
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
```
然后在html中用<button-counter></button-counter>标签就可以
* 组件的data必须是一个函数，否则就会影响到所有组件实例
props，自定义的attributes
```
Vue.component('blog-post', {
  props: ['title'],
  template: '<h3>{{ title }}</h3>'
})
```
* 组件必须有一个根元素
```
<button v-on:click="$emit('enlarge-text', 0.1)">
  Enlarge text
</button>
```
```
<blog-post
  ...
  v-on:enlarge-text="postFontSize += $event"
></blog-post>
```
* 子组件通过$emit方法传入事件名称来触发一个事件。在这里，enlarge-text方法定意思在父组件中。$event方法可以帮助父组件访问到被抛出的值（若处理事件的是一个方法，那么这个值会被当做第一个参数传入方法）





## computed和watch
* computed：是计算属性，依赖其它属性值，并且 computed 的值有缓存，只有它依赖的属性值发生改变，下一次获取 computed 的值时才会重新计算 computed 的值；
* watch：没有缓存性，更多的是「观察」的作用，类似于某些数据的监听回调 ，每当监听的数据变化时都会执行回调进行后续操作；当我们需要深度监听对象中的属性时，可以打开deep：true选项，这样便会对对象中的每一项进行监听
* 运用场景:
	* 当我们需要进行数值计算，并且依赖于其它数据时，应该使用 computed，因为可以利用 computed 的缓存特性，避免每次获取值时，都要重新计算；
	* 当我们需要在数据变化时执行异步或开销较大的操作时，应该使用 watch，使用watch选项允许我们执行异步操作 ( 访问一个 API )，限制我们执行该操作的频率，并在我们得到最终结果前，设置中间状态。这些都是计算属性无法做到的。

