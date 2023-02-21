eel.expose(username)


function username(user) {
	console.log(user)
	$("#Username").text(user);
}








// dynamic menu active link
let list = document.querySelectorAll('.list');
function activeLink() {
	// body...
	list.forEach((item) => 
	item.classList.remove('active'));
	this.classList.add('active');
}

list.forEach((item) => 
	item.addEventListener('click',activeLink))