let container = document.querySelector(`#con`);

const search = window.location.search;
let i = new URL(location.href).searchParams.undefined

let yourUrlString = new URL(location.href).searchParams.undefined

let parser = document.createElement('a');
parser.href = yourUrlString;
let qqq = parser.pathname.split('/')
console.log(qqq[3])
let qwe = qqq[3]
let res = parseInt(qqq[3])
console.log(res)
album = albums[res]
console.log(album)
container.innerHTML += `
                <h1>${album.name}</h1>
                <div class="row">
                    <div class="col p"><p class="p1">${album.description}</p></div>
//                    <div class="col"><img src="${album.img}" alt="${res}"></div>
                </div>`
console.log(list_links, container)

//container.innerHTML += `
//<ul class="sp_a">
//<li><a href="index.html">Вернуться назад</a></li>
//<li><a href="1.html?i=0">Какаято штука номер 1</a></li>
//<li><a href="1.html?i=1">Какаято штука номер 2</a></li>
//<li><a href="1.html?i=2">Какаято штука номер 3</a></li>
//</ul>

//`


