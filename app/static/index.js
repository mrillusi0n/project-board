const username = document.getElementById('user');

username.addEventListener("focusout", () => {
    getUser(username.value).catch((e) => {
        console.log(e);
    });
});

username.addEventListener("focusin", () => {
    username.style.background = "#f7faff";
});

async function getUser(id) {
    if (!id) {
        username.style.background = "#ff495c1f";
        return;
    }

    let response = await fetch('http://localhost:5000/user/' + id);
	let data = await response.json();
	
	console.log(data);
    
    if (data.user) {
        username.style.background = "#eaffde";
    } else {
        username.style.background = "#ff495c1f";
    }
}