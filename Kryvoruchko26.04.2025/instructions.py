<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>ZeroHabits — Еко блог</title>
<style>
:root {
  --bg: #f3fff3;
  --text: #0a2a0a;
  --card: rgba(255,255,255,0.5);
  --glass: blur(12px);
  --accent: #2ecc71;
}
.dark {
  --bg: #050510;
  --text: #d0ffd0;
  --card: rgba(255,255,255,0.05);
  --accent: #6aff9b;
}
body {
  margin:0; font-family:Arial; background:var(--bg); color:var(--text);
  transition:0.4s ease;
}
header{
  position:fixed; top:0; left:0; right:0; display:flex;
  justify-content:space-between; padding:15px 30px;
  backdrop-filter:var(--glass); background:var(--card);
  z-index:1000; border-bottom:1px solid rgba(255,255,255,0.2);
}
nav a{
  margin:0 15px; text-decoration:none; color:var(--text);
  font-weight:bold; transition:0.3s; cursor:pointer;
}
nav a:hover{ color:var(--accent); }
button {
  padding:10px 18px; border:none; border-radius:10px; cursor:pointer;
  font-weight:bold; background:var(--accent); color:black;
  transition:0.3s; backdrop-filter:var(--glass);
}
button:hover{ transform:scale(1.07); }
.section{ padding:120px 20px 60px; display:none; animation:fade 0.6s ease; }
.active{ display:block; }
@keyframes fade { from{opacity:0; transform:translateY(30px);} to{opacity:1; transform:translateY(0);} }
.card{
  background:var(--card); backdrop-filter:var(--glass);
  padding:20px; margin:20px auto; max-width:800px; border-radius:15px;
  transition:0.3s; border:1px solid rgba(255,255,255,0.15);
}
.card:hover{ transform:translateY(-5px) scale(1.02); }
.subcard{background:var(--card); backdrop-filter:var(--glass); padding:15px; margin:15px 0; border-radius:12px; border:1px solid rgba(255,255,255,0.12);} </style>
</head>
<body>
<header>
  <div><strong>ZeroHabits</strong></div>
  <nav>
    <a onclick="openPage('home')">Головна</a>
    <a onclick="openPage('articles')">Статті</a>
    <a onclick="openPage('categories')">Категорії</a>
    <a onclick="openPage('resources')">Ресурси</a>
    <a onclick="openPage('subscribe')">Підписка</a>
  </nav>
  <button onclick="toggleTheme()">Тема</button>
</header>

<div id="home" class="section active">
  <div class="card">
    <h1>Вітаємо у ZeroHabits!</h1>
    <p>ZeroHabits — це сучасний екоблог, створений для тих, хто хоче жити свідомо, зменшити свій вплив на планету та впроваджувати zero‑waste практики у своє повсякденне життя.</p>
    <p>Ми досліджуємо актуальні теми: сортування сміття, переробка, апсайклінг, сталий стиль життя, безпечна косметика, екотовари, відмова від пластику, екологічні технології, тренди зеленої енергетики та багато іншого.</p>
  </div>
  <div class="card">
    <h2>Що ви знайдете на сайті?</h2>
    <ul>
      <li>Глибокі та доступні статті на екотеми.</li>
      <li>Покрокові гайди: як перейти на zero‑waste.</li>
      <li>Категорії з корисними добірками.</li>
      <li>Екологічні ресурси — від застосунків до послуг переробки.</li>
      <li>Розсилку з найкращими порадами щотижня.</li>
      <li>Поради від експертів, підбірки товарів та відео.</li>
    </ul>
  </div>
</div>
</div>

<div id="articles" class="section">
  <div class="card"><h2>Статті</h2><p>Підбірка найкращих тематичних матеріалів.</p></div>

  <div class="card">
    <h3>Як перейти на zero‑waste за 30 днів</h3>
    <p>Покрокова програма для плавного переходу на екологічні звички.</p>
    <div class="subcard"><strong>Тиждень 1:</strong> Аналіз відходів, сортування, перші зміни.</div>
    <div class="subcard"><strong>Тиждень 2:</strong> Заміна одноразових товарів на багаторазові.</div>
    <div class="subcard"><strong>Тиждень 3:</strong> Zero‑waste кухня, зменшення харчових втрат.</div>
    <div class="subcard"><strong>Тиждень 4:</strong> Економія, розумні покупки, планування.</div>
  </div>

  <div class="card">
    <h3>10 продуктів, які можна купувати без пластику</h3>
    <div class="subcard">Овочі та фрукти з ринку або фермерських лавок.</div>
    <div class="subcard">Крупи, рис, макарони у власну тару з магазинів на вагу.</div>
    <div class="subcard">Вода у багаторазову пляшку, refill‑станції.</div>
  </div>

  <div class="card">
    <h3>Як працює переробка: повний гайд</h3>
    <div class="subcard">Що можна переробляти: скло, метал, PET, папір.</div>
    <div class="subcard">Підготовка відходів: мити, сушити, стискати.</div>
    <div class="subcard">Типові помилки та як їх уникнути.</div>
  </div>
</div>

<div id="categories"" class="section">
  <div class="card"><h2>Категорії</h2><p>Оберіть тему, що вас цікавить:</p></div>

  <div class="card">
    <h3>♻ Zero‑Waste Практики</h3>
    <p>Поради, лайфхаки, чек‑листи українських екоблогерів і міжнародних експертів.</p>
  </div>
  <div class="card">
    <h3>🌱 Екотовари</h3>
    <p>Огляди багаторазових пляшок, термочашок, екоторбинок, воскових обгорток та сталих брендів.</p>
  </div>
  <div class="card">
    <h3>🔋 Енергоефективність</h3>
    <p>Сонячні панелі, банки енергії, розумні системи будинку та тренди відновлюваної енергетики.</p>
  </div>
  <div class="card">
    <h3>🥦 Екокухня</h3>
    <p>Рецепти, які мінімізують відходи, правильне зберігання продуктів, поради проти харчових втрат.</p>
  </div>
</div>
</div>

<div id="resources" class="section">
  <div class="card"><h2>Ресурси</h2><p>Найкорисніші інструменти та сервіси.</p></div>

  <div class="card">
    <h3>Еко‑карта України</h3>
    <p>Інтерактивна мапа пунктів прийому вторсировини, станцій сортування, ремонт‑центрів та громадських ініціатив.</p>
  </div>
  <div class="card">
    <h3>Додатки для контролю відходів</h3>
    <ul>
      <li>RecycleMap — пункти переробки;</li>
      <li>TooGoodToGo — порятунок їжі в ресторанах;</li>
      <li>Olio — обмін продуктами між людьми;</li>
      <li>CleanSpot — знайти переробні станції.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Екологічні гіди</h3>
    <p>Повні PDF‑гайди з сортування, zero‑waste, списки дозволених та заборонених матеріалів.</p>
  </div>
</div>
</div>

<div id="subscribe" class="section">
  <div class="card"><h2>Підписка</h2><p>Отримуйте щотижневу розсилку з порадами, еконовинами та лайфхаками.</p></div>

  <div class="card">
    <h3>Що включає наша розсилка:</h3>
    <ul>
      <li>Свіжі екологічні новини світу та України.</li>
      <li>Поради “Еко за 1 хвилину”.</li>
      <li>Щотижневий zero‑waste челендж.</li>
      <li>Екопродукти тижня та огляди товарів.</li>
      <li>Інструменти для економії ресурсів.</li>
    </ul>
    <p>Ніякого спаму — лише найкорисніше 💚</p>
  </div>

  <div class="card">
    <h3>Підписатися:</h3>
    <input id="email" placeholder="Ваш email" style="padding:10px; width:80%; border-radius:10px; border:none; margin-bottom:10px;"><br>
    <button onclick="subscribeUser()">Підписатися</button>
    <p id="subMessage" style="margin-top:10px;"></p>
  </div>
</div>
<script>
function subscribeUser(){
  const email = document.getElementById('email').value;
  if(email.includes('@')){
    localStorage.setItem('subscriber', email);
    document.getElementById('subMessage').innerText = "Дякуємо! Ви підписані 💚";
  } else {
    document.getElementById('subMessage').innerText = "Введіть коректний email!";
  }
}
</script>
</div>

<script>
function openPage(id){
  document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo({ top:0, behavior:'smooth' });
}
function toggleTheme(){ document.body.classList.toggle('dark'); }
</script>

<!-- ДОДАНО ВЕЛИКИЙ ІНТЕРАКТИВНИЙ БЛОК -->
<script>
// Анімація появи карток при скролі
const observer = new IntersectionObserver(entries => {
 entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('show'); } });
},{threshold:0.2});

document.querySelectorAll('.card').forEach(card=>observer.observe(card));

// ІНТЕРАКТИВ: Порада дня
const tips=[
 'Використовуйте багаторазову пляшку — це економить до 300 пляшок на рік!',
 'Не купуйте овочі в пакеті — беріть власну торбинку.',
 'Замініть вологі серветки на багаторазову тканинну.',
 'Купуйте товари без упаковки — підтримуйте магазини на вагу.',
 'Комpostуйте органічні відходи — це зменшує сміття до 40%.',
 'Очищайте пластик перед переробкою — це підвищує шанс його переробки.',
 'Користуйтеся громадським транспортом або велосипедом — мінус CO₂!',
 'Не беріть чек у магазині, якщо він не потрібен — це хімічний папір.',
 'Краще ремонтувати, ніж купувати нове — апсайклінг рулить!',
 'Купуйте локальні продукти — менше транспорту, менше викидів.'
];
function showTip(){
 const random = tips[Math.floor(Math.random()*tips.length)];
 document.getElementById('dailyTip').innerText = random;
}

// Модальне вікно
function openModal(){ document.getElementById('modal').style.display='flex'; }
function closeModal(){ document.getElementById('modal').style.display='none'; }

</script>

<style>
.show{opacity:1!important; transform:translateY(0)!important;}
.card{opacity:0; transform:translateY(50px); transition:0.7s ease;}
.modal{
 display:none; position:fixed; inset:0; background:rgba(0,0,0,0.6);
 justify-content:center; align-items:center; z-index:2000;
}
.modal-content{
 background:var(--card); backdrop-filter:var(--glass);
 padding:30px; border-radius:15px; max-width:500px; text-align:center;
}
.link-box{
 background:var(--card); padding:15px; border-radius:12px;
 margin:15px 0; border:1px solid rgba(255,255,255,0.15);
}
</style>

<div id="extraContent" class="section">
 <div class="card">
   <h2>Порада дня</h2>
   <p id="dailyTip">Натисніть кнопку, щоб отримати пораду</p>
   <button onclick="showTip()">Отримати пораду</button>
 </div>

 <div class="card">
   <h2>Корисні міжнародні екосайти</h2>
   <div class="link-box"><a href="https://www.zerowastehome.com" target="_blank">Zero Waste Home</a> — блог Беа Джонсон.</div>
   <div class="link-box"><a href="https://www.plasticpollutioncoalition.org" target="_blank">Plastic Pollution Coalition</a> — боротьба з пластиком.</div>
   <div class="link-box"><a href="https://www.earthday.org" target="_blank">EarthDay</a> — глобальні екоініціативи.</div>
   <div class="link-box"><a href="https://www.greenpeace.org" target="_blank">Greenpeace</a> — захист природи.</div>
 </div>

 <div class="card">
   <h2>Розрахуйте ваш екологічний слід</h2>
   <p>Натисніть кнопку, щоб приблизно оцінити свій рівень впливу на природу.</p>
   <button onclick="openModal()">Порахувати</button>
 </div>
</div>

<div id="modal" class="modal">
 <div class="modal-content">
   <h3>Екологічний слід</h3>
   <p>Чи користуєтесь одноразовими пакетами?</p>
   <button onclick="closeModal()">Закрити</button>
 </div>
</div>

<!-- Additional interactive blocks: animated stars, scroll-to-top, article actions, more links -->
<style>
/* Starfield canvas */
#starfield{position:fixed;inset:0;z-index:0;pointer-events:none}
/* Floating action */
.fab{position:fixed;right:20px;bottom:20px;background:var(--accent);color:#012;padding:12px 14px;border-radius:999px;font-weight:800;box-shadow:0 10px 30px rgba(0,0,0,0.12);cursor:pointer}
.fab:hover{transform:translateY(-4px)}
/* article actions */
.article-actions{display:flex;gap:8px;margin-top:10px}
.action-btn{padding:8px 12px;border-radius:10px;border:1px solid rgba(0,0,0,0.06);background:transparent;cursor:pointer}
.action-btn.liked{background:linear-gradient(90deg,var(--accent),var(--accent));color:#052}
/* scroll to top */
#toTop{position:fixed;right:20px;bottom:90px;padding:10px;border-radius:10px;background:rgba(0,0,0,0.06);cursor:pointer}
/* subtle hover glow */
.btn-glow{box-shadow:0 6px 20px rgba(47,169,107,0.15)}
/* saved list */
#savedList{position:fixed;left:20px;bottom:20px;max-width:300px;background:var(--card);backdrop-filter:var(--glass);padding:12px;border-radius:12px;border:1px solid rgba(255,255,255,0.12)}
#savedList h4{margin:0 0 8px 0}
</style>

<canvas id="starfield"></canvas>
<button class="fab btn-glow" title="Отримати пораду" onclick="showTip();">Порада</button>
<button id="toTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">Наверх</button>
<div id="savedList" style="display:none"><h4>Збережені статті</h4><ul id="savedUl" style="margin:0;padding-left:18px"></ul></div>

<script>
// Starfield animation
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');
let stars = [];
function resize(){canvas.width=innerWidth; canvas.height=innerHeight;}
window.addEventListener('resize',resize); resize();
function initStars(){stars=[]; const count=Math.floor((canvas.width*canvas.height)/8000); for(let i=0;i<count;i++){stars.push({x:Math.random()*canvas.width,y:Math.random()*canvas.height,z:Math.random()*1,p:Math.random()*1.5+0.2});}} initStars();
function draw(){ctx.clearRect(0,0,canvas.width,canvas.height); for(const s of stars){const size=s.p*1.6; ctx.beginPath(); ctx.fillStyle=`rgba(255,255,255,${s.p})`; ctx.arc(s.x,s.y,size,0,Math.PI*2); ctx.fill(); s.x+= (s.z*0.6); s.y+= (s.z*0.2); if(s.x>canvas.width) s.x=0; if(s.y>canvas.height) s.y=0;} requestAnimationFrame(draw);} draw();

// Article like/save actions
function likeArticle(id, btn){ btn.classList.toggle('liked'); }
function saveArticle(id, title){ let arr=JSON.parse(localStorage.getItem('zh_saved')||'[]'); if(!arr.find(x=>x.id===id)){ arr.push({id,title}); localStorage.setItem('zh_saved',JSON.stringify(arr)); renderSaved(); }}
function renderSaved(){ const arr=JSON.parse(localStorage.getItem('zh_saved')||'[]'); const ul=document.getElementById('savedUl'); ul.innerHTML=''; if(arr.length){ document.getElementById('savedList').style.display='block'; arr.forEach(a=>{const li=document.createElement('li'); li.textContent=a.title; ul.appendChild(li); }); } else document.getElementById('savedList').style.display='none'; }
renderSaved();

// Enhance existing article cards: add actions and external links
function enhanceArticles(){ document.querySelectorAll('.card').forEach((c,idx)=>{
  if(c.dataset.enhanced) return; c.dataset.enhanced = '1';
  const actions = document.createElement('div'); actions.className='article-actions';
  const like = document.createElement('button'); like.className='action-btn'; like.textContent='❤ Лайк'; like.onclick = ()=>likeArticle(idx, like);
  const save = document.createElement('button'); save.className='action-btn'; save.textContent='💾 Зберегти'; save.onclick = ()=> saveArticle(idx, c.querySelector('h3')?c.querySelector('h3').innerText:'Стаття');
  const ext = document.createElement('a'); ext.className='action-btn'; ext.href='https://www.zerowastehome.com'; ext.target='_blank'; ext.textContent='🔗 Ресурс';
  actions.appendChild(like); actions.appendChild(save); actions.appendChild(ext);
  c.appendChild(actions);
}); }
enhanceArticles();

// Smooth reveal for subcards
document.querySelectorAll('.subcard').forEach((s,i)=>{ s.style.transition = 'transform 0.5s ease, opacity 0.5s ease'; s.style.transform='translateY(10px)'; s.style.opacity='0'; setTimeout(()=>{ s.style.transform='translateY(0)'; s.style.opacity='1'; }, 100 + i*120); });

// add external resource links in resources section
(function addResourceLinks(){ const resLinks = [
  {title:'Zero Waste Home',url:'https://www.zerowastehome.com'},
  {title:'RecycleMap',url:'https://recyclemap.org'},
  {title:'Too Good To Go',url:'https://toogoodtogo.com'},
  {title:'Olio',url:'https://olioex.com'}
];
  const container = document.querySelector('#resources .card');
  if(!container) return; const box = document.createElement('div'); box.className='link-box'; box.innerHTML = '<strong>Зовнішні корисні посилання:</strong>';
  resLinks.forEach(r=>{ const d=document.createElement('div'); d.style.marginTop='8px'; d.innerHTML = `<a href="${r.url}" target="_blank">${r.title}</a>`; box.appendChild(d); });
  container.appendChild(box);
})();

// Add more mock interactive content: mini quiz
(function addQuiz(){ const qcard = document.createElement('div'); qcard.className='card'; qcard.innerHTML = `<h3>Міні‑вікторина: скільки ви знаєте про сортування?</h3><p>Який матеріал не можна класти в контейнер для паперу?</p><div style="margin-top:10px"><button class='action-btn' onclick="alert('Правильно! Папір з пластиком або вологий папір не можна.')">Олівець</button> <button class='action-btn' onclick="alert('Ні — папір можна, але обгорнуті снідки краще прибрати.')">Пластиковий стаканчик</button></div>`;
  const articlesSection = document.getElementById('articles'); if(articlesSection) articlesSection.appendChild(qcard);
})();

// Auto-open extraContent after a short delay to showcase features
setTimeout(()=>{ openPage('extraContent'); setTimeout(()=>{ openPage('home'); },2500); },1200);

</script>

</body>
</html>
