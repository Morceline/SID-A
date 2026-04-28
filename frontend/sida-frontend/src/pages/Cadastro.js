import React, { useState } from 'react';
import api from '../services/api';

function Cadastro() {
  const [form, setForm] = useState({
    nome: "",
    email: "",
    senha: "",
    confirmar: ""
  });

  const [erro, setErro] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Função de validação local (antes de gastar internet enviando ao back)
  function validar() {
    if (!form.nome || !form.email || !form.senha) return "Preencha todos os campos";
    if (form.senha.length < 6) return "Senha muito curta (mín. 6 caracteres)";
    if (form.senha !== form.confirmar) return "Senhas não coincidem";
    return null;
  }

  const handleCadastro = async () => {
    const erroValidacao = validar();
    if (erroValidacao) {
      setErro(erroValidacao);
      return;
    }

    setLoading(true);
    setErro("");

    try {
      // Chama o endpoint de cadastro do backend
      await api.post("/auth/register", {
        nome: form.nome,
        email: form.email,
        senha: form.senha
      });

      alert("Conta criada com sucesso! Agora faça login.");
      // Redirecionar para login aqui 
    } catch (e) {
      // Pega a mensagem de erro que vem do Backend 
      const msgErro = e.response?.data?.detail || e.response?.data?.erro || "Erro ao cadastrar";
      setErro(msgErro);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Cadastro de Usuário</h2>
      {erro && <p style={{ color: 'red', fontWeight: 'bold' }}>{erro}</p>}
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', width: '250px' }}>
        <input name="nome" placeholder="Nome Completo" onChange={handleChange} />
        <input name="email" type="email" placeholder="E-mail" onChange={handleChange} />
        <input name="senha" type="password" placeholder="Senha" onChange={handleChange} />
        <input name="confirmar" type="password" placeholder="Confirmar Senha" onChange={handleChange} />
        
        <button onClick={handleCadastro} disabled={loading}>
          {loading ? "Processando..." : "Cadastrar"}
        </button>
      </div>
    </div>
  );
}

export default Cadastro;