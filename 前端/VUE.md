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