/* UI module: menu toggle, toast, filters, generic button behavior */
export function initUI() {
  initMenu();
  initToastListener();
  initSearch();
  initChips();
  initPrimaryButtons();
}

function initMenu() {
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  menuToggle?.addEventListener('click', () => {
    if (!nav) return;
    const isVisible = getComputedStyle(nav).display !== 'none';
    nav.style.display = isVisible ? 'none' : 'flex';
  });
}

function showToast(text, ms = 2000) {
  let t = document.getElementById('global-toast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'global-toast';
    t.style.cssText = 'position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:rgba(0,0,0,0.8);color:#fff;padding:10px 14px;border-radius:8px;z-index:10000;font-size:14px';
    document.body.appendChild(t);
  }
  t.textContent = text;
  t.style.opacity = '1';
  if (window.__toastTimer) clearTimeout(window.__toastTimer);
  window.__toastTimer = setTimeout(() => {
    t.style.opacity = '0';
  }, ms);
}

function initToastListener() {
  window.addEventListener('ui:toast', (e) => {
    showToast(e.detail?.text || '');
  });
}

function initSearch() {
  document.querySelectorAll('form.search').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const q = form.querySelector('input[type="search"]')?.value || '';
      showToast(`Поиск: «${q}» — пример результата`);
    });
  });
}

function initChips() {
  const chips = document.querySelectorAll('.chip');
  const seasonalCards = document.querySelectorAll('.seasonal .card');
  chips.forEach(chip => chip.addEventListener('click', () => {
    chips.forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
    const tag = chip.dataset.filter;
    seasonalCards.forEach(card => {
      const tags = card.dataset.tags || '';
      card.style.display = tag === 'all' || tags.includes(tag) ? '' : 'none';
    });
  }));
}

function initPrimaryButtons() {
  document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const href = btn.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        target?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        return;
      }
      if (!href) {
        e.preventDefault();
        showToast('Действие — пример (кнопка нажата)');
      }
    });
  });
}