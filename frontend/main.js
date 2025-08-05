const apiUrl = 'http://localhost:8000';
let token = null;

async function registerUser(event) {
  event.preventDefault();
  const username = document.getElementById('reg-username').value;
  const email = document.getElementById('reg-email').value;
  const password = document.getElementById('reg-password').value;
  const res = await fetch(`${apiUrl}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password })
  });
  const msg = document.getElementById('register-msg');
  if (res.ok) {
    msg.textContent = 'Usuario registrado';
    event.target.reset();
  } else {
    const data = await res.json();
    msg.textContent = data.detail || 'Error en registro';
  }
}

async function loginUser(event) {
  event.preventDefault();
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;
  const res = await fetch(`${apiUrl}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  const msg = document.getElementById('login-msg');
  if (res.ok) {
    const data = await res.json();
    token = data.access_token;
    msg.textContent = 'Login correcto';
    document.getElementById('courses').style.display = 'block';
    loadCourses();
  } else {
    const data = await res.json();
    msg.textContent = data.detail || 'Error en login';
  }
}

async function createCourse(event) {
  event.preventDefault();
  const title = document.getElementById('course-title').value;
  const description = document.getElementById('course-desc').value;
  const level = document.getElementById('course-level').value;
  const res = await fetch(`${apiUrl}/courses/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {})
    },
    body: JSON.stringify({ title, description, level })
  });
  if (res.ok) {
    event.target.reset();
    loadCourses();
  }
}

async function loadCourses() {
  const res = await fetch(`${apiUrl}/courses/`);
  if (!res.ok) return;
  const courses = await res.json();
  const list = document.getElementById('course-list');
  list.innerHTML = '';
  courses.forEach(c => {
    const li = document.createElement('li');
    li.textContent = `${c.title} (${c.level || 'sin nivel'})`;
    list.appendChild(li);
  });
}

document.getElementById('register-form').addEventListener('submit', registerUser);
document.getElementById('login-form').addEventListener('submit', loginUser);
document.getElementById('course-form').addEventListener('submit', createCourse);
