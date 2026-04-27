import React from 'react';
import Mapa from '../components/Mapa';
import ListaEventos from '../components/ListaEventos';
import PainelInfo from '../components/PainelInfo';

function Dashboard() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Dashboard do Sistema</h1>
      <div style={{ display: 'flex', gap: '20px' }}>
        <div style={{ flex: 2 }}>
          <Mapa />
        </div>
        <div style={{ flex: 1 }}>
          <PainelInfo />
          <ListaEventos />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;