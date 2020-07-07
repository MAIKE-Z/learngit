const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* 添加图片循环 */

for (let i = 1; i < 6; i++) {
	const newImage = document.createElement('img');
	newImage.setAttribute('src', 'images/pic'+i+'.jpg');
	thumbBar.appendChild(newImage);
	
	newImage.onclick=function(e){
		displayedImage.setAttribute('src', e.target.src);
	}
}
/*
	newImage.addEventListener(onclick,switchTo);
}

function switchTo(e){
	displayedImage.setAttribute(src, value: DOMString);
	console.log(e);
}*/

/* 编写 变暗/变量 按钮功能 */

btn.onclick= function(){
	if(btn.getAttribute('class')==='dark'){
		overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
		btn.textContent='变亮';
		btn.setAttribute('class','light');
	}
	else{
		btn.setAttribute('class','dark');
		overlay.style.backgroundColor = 'rgba(0,0,0,0)';
		btn.textContent='变暗';
	}

}