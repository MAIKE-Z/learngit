let myBotton = document.querySelector('button');
let myH1 = document.querySelector('h1');


function setUserName(){
	let myName = prompt('please input your name: ');
	if (myName==='' || myName === null) {
		setUserName();
	}
	else{
	localStorage.setItem('name', myName);
	myH1.textContent = 'hi, ' + myName;
	}
}


if (localStorage.getItem('name')) {
	let storedName = localStorage.getItem('name');
	myH1.textContent = 'hi, ' + storedName;

}
else {
	setUserName();
}


myBotton.onclick = function(){
	setUserName();
}