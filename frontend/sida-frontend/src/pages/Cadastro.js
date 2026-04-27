import React, { useState } from 'react';
import api from '../services/api';

function Cadastro() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");

  const handleCadastro = async () => {
    try {
      const response = await api.post('/auth/register', {
  nome,
  email,
  senha
});
      alert(response.data.msg || response.data.erro);
    } catch (error) {
      console.error("Erro ao cadastrar", error);
    }
  };

  return (
    <div>
      <h2>Cadastro</h2>
      <input type="text" placeholder="Nome" onChange={e => setNome(e.target.value)} />
      <input type="email" placeholder="Email" onChange={e => setEmail(e.target.value)} />
      <input type="password" placeholder="Senha" onChange={e => setSenha(e.target.value)} />
      <button onClick={handleCadastro}>Cadastrar</button>
    </div>
  );
}

export default Cadastro;