import React, { useState } from 'react';
import api from '../services/api';

function Login() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");

  const handleLogin = async () => {
    try {
      const response = await api.post('/auth/login', null, {
        params: { email, senha }
      });
      if (response.data.id) {
        alert(`Bem-vindo, ${response.data.nome}!`);
        // Aqui depois vamos salvar no contexto e redirecionar
      } else {
        alert(response.data.erro);
      }
    } catch (error) {
      console.error("Erro no login", error);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)} />
      <input type="password" placeholder="Senha" onChange={e => setSenha(e.target.value)} />
      <button onClick={handleLogin}>Entrar</button>
    </div>
  );
}

export default Login;