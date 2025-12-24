// app/static/js/main.js

// Проверяем, находимся ли мы на странице каталога
if (document.getElementById('catalog-list')) {
    const hotels = [
        { slug: 'Hotel+A', title: 'Hotel A — Центр', price: 'от 4 500 ₽/ночь', stars: '★★★★☆' },
        { slug: 'Hotel+B', title: 'Hotel B — Набережная', price: 'от 6 200 ₽/ночь', stars: '★★★★★' },
        { slug: 'Hotel+C', title: 'Hotel C — Парковая зона', price: 'от 3 900 ₽/ночь', stars: '★★★★☆' },
        { slug: 'Sea Resort', title: 'Sea Resort', price: 'от 7 800 ₽/ночь', stars: '★★★★★' },
        { slug: 'Mountain Lodge', title: 'Mountain Lodge', price: 'от 5 600 ₽/ночь', stars: '★★★★☆' },
        { slug: 'City Boutique', title: 'City Boutique', price: 'от 4 100 ₽/ночь', stars: '★★★☆☆' },
        { slug: 'Coastal Inn', title: 'Coastal Inn', price: 'от 6 300 ₽/ночь', stars: '★★★★☆' }
    ];

    const container = document.getElementById('catalog-list');
    container.innerHTML = hotels.map(h => `
      <article class="card">
        <a class="card-link" href="/hotel?hotel=${encodeURIComponent(h.slug)}">
          <img src="https://placehold.co/600x400/000000/F4EB49/png?text=${encodeURIComponent(h.title)}" alt="${h.title}">
        </a>
        <div class="card-body">
          <h3><a class="card-link" href="/hotel?hotel=${encodeURIComponent(h.slug)}">${h.title}</a></h3>
          <div class="meta">
            <span class="price">${h.price}</span>
            <span class="stars" aria-label="Рейтинг">${h.stars}</span>
          </div>
          <button class="btn-outline">Добавить в корзину</button>
        </div>
      </article>
    `).join('');
}
/* Entry point: initialize modules and wire basic behavior */
import { initUI } from './ui.js';
import { initCart, addItemFromButton, openCart } from './cart.js';
import { initPanels } from './panels.js';

// initialize subsystems
initUI();
initCart();
initPanels();

// wire add-to-cart buttons (delegated wiring is in UI but keep compatibility)
document.querySelectorAll('.card .btn-outline').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    addItemFromButton(btn);
  });
});

// cart button
const cartBtn = document.querySelector('.cart-btn');
cartBtn?.addEventListener('click', (e) => { e.preventDefault(); openCart(); });