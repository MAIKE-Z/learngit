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




/*const list = document.createElement('ul');
const info = document.createElement('p');
const html = document.querySelector('html');

info.textContent = 'Below is a dynamic list. Click anywhere outside the list to add a new list item. Click an existing list item to change its text to something else.';

document.body.appendChild(info);
document.body.appendChild(list);

html.onclick = function() {
  const listItem = document.createElement('li');
  const listContent = prompt('What content do you want the list item to have?');
  listItem.textContent = listContent;
  list.appendChild(listItem);

  listItem.onclick = function(e) {
    e.stopPropagation();
    const listContent = prompt('Enter new content for your list item');
    this.textContent = listContent;
  }
}*/