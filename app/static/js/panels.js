/* Panels module: account/auth/register panels */
export function initPanels() {
  const accountLink = document.getElementById('account-link');
  accountLink?.addEventListener('click', (e) => {
    e.preventDefault();
    openAccount();
  });
  const authLink = document.getElementById('auth-link');
  authLink?.addEventListener('click', (e) => {
    e.preventDefault();
    openAuth();
  });
  const registerLink = document.getElementById('register-link');
  registerLink?.addEventListener('click', (e) => {
    e.preventDefault();
    openRegister();
  });
}

function emitToast(text) {
  window.dispatchEvent(new CustomEvent('ui:toast', { detail: { text } }));
}

export function openAccount() {
  createAccountPanel();
  document.getElementById('account-panel').classList.add('show');
}

export function hideAccount() {
  const panel = document.getElementById('account-panel');
  if (panel) panel.classList.remove('show');
}

export function createAccountPanel() {
  if (document.getElementById('account-panel')) return;
  const panel = document.createElement('aside');
  panel.id = 'account-panel';
  panel.innerHTML = `
    <div class="account-backdrop" id="account-backdrop"></div>
    <div class="account-sheet" role="dialog" aria-label="Личный кабинет">
      <header class="account-header">
        <h3>Личный кабинет</h3>
        <button id="account-close" aria-label="Закрыть">✕</button>
      </header>
      <div class="account-body">
        <div class="account-info">
          <div style="display:flex;gap:12px;align-items:center;">
            <div style="width:56px;height:56px;background:var(--panel);border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:700;color:var(--muted)">U</div>
            <div>
              <div style="font-weight:700">Гость</div>
              <div style="color:var(--muted);font-size:13px">guest@example.com</div>
            </div>
          </div>
          <div style="margin-top:12px;display:grid;gap:8px;">
            <button id="view-bookings" class="btn-outline">Мои бронирования</button>
            <button id="edit-profile" class="btn-outline">Редактировать профиль</button>
            <button id="logout" class="btn-outline">Выйти</button>
          </div>
        </div>
      </div>
    </div>
  `;
  document.body.appendChild(panel);

  const style = document.createElement('style');
  style.textContent = `
    #account-panel { position: fixed; inset: 0; z-index: 10001; display: none; }
    .account-backdrop { position:absolute; inset:0; background:rgba(0,0,0,0.35); }
    .account-sheet { position: absolute; right: 16px; top: 12vh; width: 360px; max-width: calc(100% - 32px); background:var(--bg); border-radius:12px; box-shadow:0 20px 50px rgba(0,0,0,0.2); overflow:hidden; display:flex; flex-direction:column; }
    .account-header { display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--border); }
    .account-body { padding:16px; }
    #account-panel.show { display:block; }
  `;
  document.head.appendChild(style);

  document.getElementById('account-close').addEventListener('click', hideAccount);
  document.getElementById('account-backdrop').addEventListener('click', hideAccount);
  document.getElementById('view-bookings').addEventListener('click', () => emitToast('Переход в раздел бронирований — пример'));
  document.getElementById('edit-profile').addEventListener('click', () => emitToast('Редактирование профиля — пример'));
  document.getElementById('logout').addEventListener('click', () => {
    emitToast('Вы вышли — пример');
    hideAccount();
  });
}

// Auth panel
export function openAuth() {
  createAuthPanel();
  document.getElementById('auth-panel').classList.add('show');
}
export function hideAuth() {
  const p = document.getElementById('auth-panel');
  if (p) p.classList.remove('show');
}
export function createAuthPanel() {
  if (document.getElementById('auth-panel')) return;
  const panel = document.createElement('aside');
  panel.id = 'auth-panel';
  panel.innerHTML = `
    <div class="auth-backdrop" id="auth-backdrop"></div>
    <div class="auth-sheet" role="dialog" aria-label="Авторизация">
      <header class="auth-header">
        <h3>Авторизация</h3>
        <button id="auth-close" aria-label="Закрыть">✕</button>
      </header>
      <div class="auth-body">
        <form id="auth-form" style="display:grid;gap:10px;">
          <input type="email" id="auth-email" placeholder="Email" required style="padding:10px;border:1px solid var(--border);border-radius:8px;">
          <input type="password" id="auth-pass" placeholder="Пароль" required style="padding:10px;border:1px solid var(--border);border-radius:8px;">
          <div style="display:flex;gap:8px;justify-content:flex-end;">
            <button type="button" id="auth-cancel" class="btn-outline">Отмена</button>
            <button type="submit" class="btn-primary">Войти</button>
          </div>
        </form>
      </div>
    </div>
  `;
  document.body.appendChild(panel);

  const style = document.createElement('style');
  style.textContent = `
    #auth-panel { position: fixed; inset: 0; z-index: 10002; display: none; }
    .auth-backdrop { position:absolute; inset:0; background:rgba(0,0,0,0.35); }
    .auth-sheet { position: absolute; right: 16px; top: 12vh; width: 360px; max-width: calc(100% - 32px); background:var(--bg); border-radius:12px; box-shadow:0 20px 50px rgba(0,0,0,0.2); overflow:hidden; display:flex; flex-direction:column; }
    .auth-header { display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--border); }
    .auth-body { padding:16px; }
    #auth-panel.show { display:block; }
  `;
  document.head.appendChild(style);

  document.getElementById('auth-close').addEventListener('click', hideAuth);
  document.getElementById('auth-backdrop').addEventListener('click', hideAuth);
  document.getElementById('auth-cancel').addEventListener('click', hideAuth);
  document.getElementById('auth-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('auth-email').value;
    emitToast(`Вход как ${email} — пример`);
    hideAuth();
  });
}

// Register panel
export function openRegister() {
  createRegisterPanel();
  document.getElementById('register-panel').classList.add('show');
}
export function hideRegister() {
  const p = document.getElementById('register-panel');
  if (p) p.classList.remove('show');
}
export function createRegisterPanel() {
  if (document.getElementById('register-panel')) return;
  const panel = document.createElement('aside');
  panel.id = 'register-panel';
  panel.innerHTML = `
    <div class="register-backdrop" id="register-backdrop"></div>
    <div class="register-sheet" role="dialog" aria-label="Регистрация">
      <header class="register-header">
        <h3>Регистрация</h3>
        <button id="register-close" aria-label="Закрыть">✕</button>
      </header>
      <div class="register-body">
        <form id="register-form" style="display:grid;gap:10px;">
          <input type="text" id="reg-name" placeholder="Имя" required style="padding:10px;border:1px solid var(--border);border-radius:8px;">
          <input type="email" id="reg-email" placeholder="Email" required style="padding:10px;border:1px solid var(--border);border-radius:8px;">
          <input type="password" id="reg-pass" placeholder="Пароль" required style="padding:10px;border:1px solid var(--border);border-radius:8px;">
          <div style="display:flex;gap:8px;justify-content:flex-end;">
            <button type="button" id="register-cancel" class="btn-outline">Отмена</button>
            <button type="submit" class="btn-primary">Зарегистрироваться</button>
          </div>
        </form>
      </div>
    </div>
  `;
  document.body.appendChild(panel);

  const style = document.createElement('style');
  style.textContent = `
    #register-panel { position: fixed; inset: 0; z-index: 10002; display: none; }
    .register-backdrop { position:absolute; inset:0; background:rgba(0,0,0,0.35); }
    .register-sheet { position: absolute; right: 16px; top: 12vh; width: 420px; max-width: calc(100% - 32px); background:var(--bg); border-radius:12px; box-shadow:0 20px 50px rgba(0,0,0,0.2); overflow:hidden; display:flex; flex-direction:column; }
    .register-header { display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--border); }
    .register-body { padding:16px; }
    #register-panel.show { display:block; }
  `;
  document.head.appendChild(style);

  document.getElementById('register-close').addEventListener('click', hideRegister);
  document.getElementById('register-backdrop').addEventListener('click', hideRegister);
  document.getElementById('register-cancel').addEventListener('click', hideRegister);
  document.getElementById('register-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('reg-name').value;
    emitToast(`Спасибо за регистрацию, ${name} — пример`);
    hideRegister();
  });
}