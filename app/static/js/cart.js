/* Cart module: manages cart state and renders the cart panel */
let cart = [];
let cartCountEl = null;
let cartBtnEl = null;

function formatPrice(n) {
  return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' ₽';
}

export function initCart() {
  cartCountEl = document.querySelector('.cart-count');
  cartBtnEl = document.querySelector('.cart-btn');
  createCartPanel();
  renderCart();
}

export function getCart() {
  return cart;
}

export function createCartPanel() {
  if (document.getElementById('cart-panel')) return;
  const panel = document.createElement('aside');
  panel.id = 'cart-panel';
  panel.innerHTML = `
    <div class="cart-backdrop" id="cart-backdrop"></div>
    <div class="cart-sheet" role="dialog" aria-label="Корзина">
      <header class="cart-header">
        <h3>Корзина</h3>
        <button id="cart-close" aria-label="Закрыть">✕</button>
      </header>
      <div id="cart-items" class="cart-items"></div>
      <footer class="cart-footer">
        <div class="cart-total">Итог: <span id="cart-total">0 ₽</span></div>
        <div class="cart-actions">
          <button id="cart-clear" class="btn-outline">Очистить</button>
          <button id="cart-checkout" class="btn-primary">Оформить</button>
        </div>
      </footer>
    </div>
  `;
  document.body.appendChild(panel);

  const style = document.createElement('style');
  style.textContent = `
    #cart-panel { position: fixed; inset: 0; z-index: 9999; display: none; }
    #cart-backdrop { position:absolute; inset:0; background:rgba(0,0,0,0.35); }
    .cart-sheet { position: absolute; right: 16px; top: 10vh; width: 360px; max-width: calc(100% - 32px); background:var(--bg); border-radius:12px; box-shadow:0 20px 50px rgba(0,0,0,0.2); overflow:hidden; display:flex; flex-direction:column; max-height:80vh; }
    .cart-header { display:flex; justify-content:space-between; align-items:center; padding:12px 16px; border-bottom:1px solid var(--border); }
    .cart-items { padding:12px 16px; overflow:auto; flex:1; display:grid; gap:10px; }
    .cart-item { display:flex; justify-content:space-between; gap:12px; align-items:center; border:1px solid var(--border); padding:8px; border-radius:8px; background:var(--card-bg); }
    .cart-footer { padding:12px 16px; border-top:1px solid var(--border); display:flex; justify-content:space-between; align-items:center; gap:12px; }
    .cart-actions { display:flex; gap:8px; }
    #cart-panel.show { display:block; }
    .cart-empty { color:var(--muted); text-align:center; padding:16px 0; }
  `;
  document.head.appendChild(style);

  document.getElementById('cart-close').addEventListener('click', hideCart);
  document.getElementById('cart-backdrop').addEventListener('click', hideCart);
  document.getElementById('cart-clear').addEventListener('click', () => {
    cart = [];
    renderCart();
    const { showToast } = awaitToast();
    showToast('Корзина очищена');
  });
  document.getElementById('cart-checkout').addEventListener('click', () => {
    const { showToast } = awaitToast();
    if (cart.length === 0) {
      showToast('Корзина пуста');
      return;
    }
    showToast('Переход к оформлению — пример');
    hideCart();
  });

  function awaitToast() {
    // dynamic import to avoid circular dependency ordering with ui.js
    return { showToast: (text) => {
      const evt = new CustomEvent('ui:toast', { detail: { text } });
      window.dispatchEvent(evt);
    }};
  }
}

export function renderCart() {
  createCartPanel();
  const list = document.getElementById('cart-items');
  const totalEl = document.getElementById('cart-total');
  list.innerHTML = '';
  if (cart.length === 0) {
    list.innerHTML = `<div class="cart-empty">В корзине нет товаров</div>`;
    totalEl.textContent = '0 ₽';
    updateCartCount();
    return;
  }
  let total = 0;
  cart.forEach((it, idx) => {
    const numeric = Number(String(it.price).replace(/[^\d]/g, '')) || 0;
    total += numeric * it.qty;
    const item = document.createElement('div');
    item.className = 'cart-item';
    item.innerHTML = `
      <div style="flex:1;min-width:0;">
        <div style="font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${it.title}</div>
        <div style="color:var(--muted);font-size:13px">${it.price} × ${it.qty}</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;align-items:flex-end;">
        <div>
          <button class="cart-decr" data-idx="${idx}" aria-label="Уменьшить">−</button>
          <button class="cart-incr" data-idx="${idx}" aria-label="Увеличить">+</button>
        </div>
        <button class="cart-remove" data-idx="${idx}" aria-label="Удалить">Удалить</button>
      </div>
    `;
    list.appendChild(item);
  });
  totalEl.textContent = formatPrice(total);
  updateCartCount();

  list.querySelectorAll('.cart-remove').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const idx = Number(btn.dataset.idx);
      cart.splice(idx, 1);
      renderCart();
    });
  });
  list.querySelectorAll('.cart-incr').forEach(btn => {
    btn.addEventListener('click', () => {
      const idx = Number(btn.dataset.idx);
      cart[idx].qty += 1;
      renderCart();
    });
  });
  list.querySelectorAll('.cart-decr').forEach(btn => {
    btn.addEventListener('click', () => {
      const idx = Number(btn.dataset.idx);
      cart[idx].qty = Math.max(1, cart[idx].qty - 1);
      renderCart();
    });
  });
}

export function updateCartCount() {
  if (!cartCountEl) cartCountEl = document.querySelector('.cart-count');
  const totalQty = cart.reduce((s, i) => s + i.qty, 0);
  if (cartCountEl) cartCountEl.textContent = String(totalQty);
  if (cartBtnEl) cartBtnEl.classList.toggle('has-items', totalQty > 0);
}

export function openCart() {
  createCartPanel();
  document.getElementById('cart-panel').classList.add('show');
  renderCart();
}

export function hideCart() {
  const panel = document.getElementById('cart-panel');
  if (panel) panel.classList.remove('show');
}

export function addItemFromButton(btn) {
  const card = btn.closest('.card');
  if (!card) {
    const ev = new CustomEvent('ui:toast', { detail: { text: 'Не удалось добавить в корзину' } });
    window.dispatchEvent(ev);
    return;
  }
  const titleEl = card.querySelector('h3') || card.querySelector('img');
  const title = titleEl ? titleEl.textContent.trim() : 'Товар';
  const priceEl = card.querySelector('.price');
  const price = priceEl ? priceEl.textContent.trim() : '0 ₽';
  const id = (title + '|' + price);
  const existing = cart.find(c => c.id === id);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ id, title, price, qty: 1 });
  }
  renderCart();
  openCart();
  const ev = new CustomEvent('ui:toast', { detail: { text: 'Добавлено в корзину' } });
  window.dispatchEvent(ev);
}