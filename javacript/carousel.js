let carousel_items = document.querySelectorAll('.carousel-item');
let current = 0;

function showItem(all_items, shown_item) {
  for (let i=0; i<all_items.length; i++) {
    // change class shown to class hidden
    all_items[i].classList.remove('shown');
    all_items[i].classList.add('hidden');
  }
  shown_item.classList.remove('hidden');
  shown_item.classList.add('shown');
}

function autoAdvance() {
  current = (current + 1) % carousel_items.length;
  showItem(carousel_items, carousel_items[current]);
}

setInterval(autoAdvance, 3000);