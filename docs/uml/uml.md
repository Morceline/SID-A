1) Diagrama de Caso de Uso
O Diagrama de Caso de Uso apresenta a visão externa do sistema, mostrando quais atores interagem com a solução e quais funcionalidades cada um pode acessar. Ele está diretamente ligado aos requisitos funcionais, porque traduz as necessidades do varejista, do cliente final, do barqueiro e do administrador em serviços concretos do sistema, como acompanhar encomendas, consultar status, visualizar histórico, receber alertas e gerenciar viagens. No contexto do projeto, esse diagrama é importante porque delimita claramente a fronteira do sistema e evidencia que a solução foi pensada para diferentes perfis de usuário, respeitando inclusive as restrições de acesso.
Ligação direta com os requisitos
- RF04: painel de monitoramento interativo
- RF05: cálculo de ETA
- RF06: sistema de alertas
- RNF03: controle de acesso e privacidade




2) Diagrama de Classes
O Diagrama de Classes representa a estrutura estática do sistema, ou seja, as entidades que armazenam as informações e os relacionamentos entre elas. Ele está ligado ao projeto porque organiza o núcleo dos dados necessários para o monitoramento logístico, como embarcação, viagem, encomenda, posição, usuário e alerta. Em relação aos requisitos, esse diagrama sustenta a rastreabilidade das cargas, o armazenamento do histórico geográfico e a aplicação das regras de negócio, como a obrigatoriedade de associar uma viagem a uma embarcação e a necessidade de manter registros de posição ordenados no tempo.
Ligação direta com os requisitos
- RN01: uma encomenda vinculada a apenas uma viagem ativa
- RN02: toda viagem associada a uma embarcação
- RN03: múltiplas posições ordenadas por timestamp
- RF02: georreferenciamento automático
- RF04: visualização de histórico e última posição




3) Diagrama de Atividades
O Diagrama de Atividades mostra o fluxo operacional do sistema, especialmente a lógica de coleta, armazenamento local, sincronização e geração de alertas. Ele está diretamente relacionado ao problema do projeto, porque representa o funcionamento do sistema em um ambiente com conectividade intermitente, como ocorre na Amazônia. Em termos de requisitos, esse diagrama evidencia o comportamento offline-first da solução, a sincronização assíncrona e o processamento de eventos logísticos, mostrando que o sistema continua funcionando mesmo sem acesso contínuo à internet.
Ligação direta com os requisitos
- RF01: registro de eventos logísticos
- RF02: associação de GPS e horário aos eventos
- RF03: sincronização assíncrona
- RF06: geração de alertas
- RNF01: tolerância a desconexões
- RNF02: persistência e resiliência




4) Diagrama de Sequência
O Diagrama de Sequência detalha a troca cronológica de mensagens entre os componentes do sistema durante o fluxo principal de operação. Ele é importante para o projeto porque mostra, de forma temporal, como os dados saem do dispositivo embarcado, passam pelo armazenamento local, são sincronizados com o backend, persistidos no banco de dados e depois disponibilizados ao usuário. Sua ligação com os requisitos está principalmente na integridade da sincronização, na validação dos dados e na atualização das informações apresentadas na interface.
Ligação direta com os requisitos
- RF03: transmissão automática após reconexão
- RF04: consulta das informações pela interface
- RN04: prioridade de armazenamento local
- RN05: dados não podem ser descartados antes da confirmação




5) Diagrama de Arquitetura / Componentes
O Diagrama de Arquitetura representa a organização estrutural da solução em blocos funcionais, mostrando como os componentes se conectam para sustentar o sistema como um todo. Ele está diretamente ligado ao projeto porque evidencia as decisões técnicas adotadas para o contexto amazônico, especialmente o uso de armazenamento local, comunicação assíncrona e sincronização tolerante a atrasos. Em relação aos requisitos, esse diagrama mostra como a solução foi estruturada para garantir operação offline, processamento dos dados, persistência central e visualização web para os usuários.
Ligação direta com os requisitos
- RF03: sincronização assíncrona
- RF04: frontend de monitoramento
- RF06: processamento de alertas
- RNF01: operação robusta sem conectividade contínua
- RNF04: interface leve em PWA
- RNF06: arquitetura modular e escalável