const search = document.getElementById('search-btn');
const query = document.getElementById('search-string');
const holder = document.getElementById('cards_container');
const noResult = document.getElementById('no_result');
var tmp = document.querySelector('#card_template');

async function searchArts(e) {
  e.preventDefault();

  if (query.value.length < 2) {
    return;
  }

  const config = {
    headers: {
      Accept: 'application/json',
    },
  };

  const result = await fetch('/api?q=' + query.value);
  const data = await result.json();

  holder.innerHTML = '';

  console.log(data);

  if (result.ok && data.length > 0) {
    noResult.classList.add('invisible');
    data.forEach((element) => {
      let clone = tmp.content.cloneNode(true);
      let title = clone.querySelector('#card-title');
      let author = clone.querySelector('#card-author');
      let desc = clone.querySelector('#card-text');
      let ctype = clone.querySelector('#card-type');
      let cdate = clone.querySelector('#card-date');
      let img = clone.querySelector('#card-thumb');

      title.textContent = element['title'];
      author.textContent = element['name'];
      desc.textContent = element['medium'];
      ctype.textContent = element['classification'];
      cdate.textContent = element['release_date'];
      // img.setAttribute('src', element['link']);

      holder.appendChild(clone);
    });
  } else {
    noResult.classList.remove('invisible');
  }

  // console.log(data);
}

search.addEventListener('click', (e) => searchArts(e));
