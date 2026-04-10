**Regras de Negócio:**

- RN01 -- Unicidade de Viagem: 
Uma encomenda deve estar vinculada a apenas uma viagem ativa por vez para evitar duplicidade de rastreamento.
- RN02 -- Hierarquia de Dados: 
Toda viagem deve estar obrigatoriamente associada a uma embarcação previamente cadastrada no sistema.
- RN03 -- Temporalidade Geográfica:
Uma embarcação pode possuir múltiplas posições ao longo do tempo, mas cada registro deve ser único e ordenado por timestamp.
- RN04 -- Prioridade de Armazenamento: 
O sistema deve priorizar o armazenamento local (offline) em detrimento de tentativas contínuas de conexão em áreas de baixa densidade de sinal, visando economia de energia.
- RN05 -- Integridade de Sincronização: 
Dados coletados no dispositivo embarcado jamais podem ser descartados antes da confirmação de recebimento (ACK) enviada pelo servidor central após a reconexão.

**Requisitos Funcionais**

    - RF01 -- Registro de Eventos Logísticos:
        O sistema deve permitir o registro manual ou automático de eventos como início da viagem, paradas intermediárias e entrega final.
     - RF02 -- Georreferenciamento Automático:
        Associar coordenadas de GPS e horários precisos a cada evento registrado ou mudança de estado da carga.
     - RF03 -- Sincronização Assíncrona:
        O dispositivo deve transmitir automaticamente os dados acumulados para o servidor assim que uma conexão de rede for restabelecida.
     - RF04 -- Painel de Monitoramento Interativo:
        Disponibilizar uma interface geográfica para visualização do histórico de rotas e última posição conhecida das embarcações.
     - RF05 -- Cálculo de Estimativa de Chegada (ETA):
        Estimar o tempo de chegada com base na velocidade média registrada em viagens anteriores e na distância restante do percurso.
     - RF06 -- Sistema de Alertas:
        Identificar e notificar automaticamente comportamentos anômalos, como desvios de rota injustificados ou paradas excessivamente prolongadas.

  **Requisitos Não Funcionais**

  - Desempenho, Disponibilidade e Segurança

    - RNF01 -- Tolerância a Desconexões:
     O sistema deve operar de forma robusta sob o paradigma de Redes Tolerantes a Atrasos (DTN), garantindo o funcionamento offline.
    - RNF02 -- Persistência e Resiliência:
     Garantir a integridade dos dados no hardware embarcado mesmo em cenários de falha de energia ou reinicialização inesperada do sistema.
    - RNF03 -- Segurança e Privacidade:
     Implementar controle de acesso granular para garantir que varejistas e clientes visualizem apenas os dados pertinentes às suas respectivas cargas.


- Usabilidade, Escalabilidade e Custo

    - RNF04 -- Interface Leve (PWA):
     A interface deve ser desenvolvida como um Progressive Web App para garantir compatibilidade multiplataforma e baixo consumo de recursos.
    - RNF05 -- Soberania Tecnológica:
     Utilizar exclusivamente tecnologias open-source para reduzir barreiras financeiras e facilitar a evolução colaborativa do projeto.
    - RNF06 -- Escalabilidade de Análise:
     A arquitetura deve possuir estrutura modular que permita a futura integração de modelos de aprendizado de máquina para análises preditivas.
