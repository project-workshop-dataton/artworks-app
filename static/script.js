// создаем привязку к объектам
const search = document.getElementById('search-btn');
const query = document.getElementById('search-string');
const holder = document.getElementById('cards_container');
const noResult = document.getElementById('no_result');
var tmp = document.querySelector('#card_template');

async function onEnter(e) {
  if (e.keyCode == 13) {
    search.click();
  }
}

async function searchArts(e) {
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

  if (result.ok && data.length > 0) {
    noResult.classList.add('invisible');
    data.forEach((element) => {
      let clone = tmp.content.cloneNode(true);
      let card = clone.querySelector('.card');
      let title = clone.querySelector('#card-title');
      let author = clone.querySelector('#card-author');
      let desc = clone.querySelector('#card-text');
      let ctype = clone.querySelector('#card-type');
      let cdate = clone.querySelector('#card-date');
      let img = clone.querySelector('#card-thumb');
      let like = clone.querySelector('#like-btn');
      let dislike = clone.querySelector('#dislike-btn');

      card.setAttribute('data-id', element['artwork_id']);
      title.textContent = element['pub_title'];
      author.textContent = element['name'];
      desc.textContent = element['medium'];
      ctype.textContent = element['classification'];
      cdate.textContent = element['pub_year'];
      img.setAttribute('src', element['link']);
      like.addEventListener('click', (e) => sendFeedback(element['artwork_id'], 1));
      dislike.addEventListener('click', (e) => sendFeedback(element['artwork_id'], 0));

      holder.appendChild(clone);
    });
  } else {
    noResult.classList.remove('invisible');
  }
}

async function sendFeedback(id, fb) {
  fetch('/api/feedback', {
    method: 'post',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      q: query.value,
      id: id,
      feedback: fb,
    }),
  });
}

query.addEventListener('keydown', (e) => onEnter(e));
search.addEventListener('click', (e) => searchArts(e));
