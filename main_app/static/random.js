

let ul = document.querySelector('.card-container');
for (let i = ul.children.length; i >= 0; i--) {
    console.log(ul.children)
    ul.appendChild(ul.children[Math.random() * i | 0]);
}





