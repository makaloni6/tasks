import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:3000/api/login/', { username, password });
      onLogin(response.data); // ログイン成功時にユーザー情報を親コンポーネントに渡す
    } catch (err) {
      console.error('Login failed', err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  );
}

// // ダッシュボードコンポーネント（ログイン後の画面）
// function Dashboard({ user, onLogout }) {
//   return (
//     <div>
//       <h1>Welcome, {user.username}!</h1>
//       <button onClick={onLogout}>Logout</button>
//       {/* ここにダッシュボードの内容を追加 */}
//     </div>
//   );
// }

// // メインのAppコンポーネント
// function App() {
//   const [user, setUser] = useState(null);

//   const handleLogin = (userData) => {
//     setUser(userData);
//   };

//   const handleLogout = () => {
//     setUser(null);
//   };

//   return (
//     <div className="App">
//       {user ? (
//         <Dashboard user={user} onLogout={handleLogout} />
//       ) : (
//         <Login onLogin={handleLogin} />
//       )}
//     </div>
//   );
// }

// export default App;

// import logo from './logo.svg';
// import './App.css';
// import React from 'react';
// import LoginForm from './components/LoginForm';

function App() {
  const [user, setUser] = useState(null);
  const handleLogin = (userData) => {
        setUser(userData);
      };
  return (
      <div>
          <Login onLogin={handleLogin} />
      </div>
  );
}

export default App;