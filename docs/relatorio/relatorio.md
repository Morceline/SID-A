**Tópicos:**

CONTEXTO + PROBLEMA
O sistema é na Amazônia

A logística na Amazônia é um sistema multimodal desafiador, fortemente dependente do modal fluvial (responsável por cerca de 65% do transporte na região) e aéreo, exigindo adaptação às condições geográficas e climáticas extremas. A integração de balsas, portos fluviais, aeroportos e o uso de tecnologia são fundamentais para o escoamento da Zona Franca de Manaus e o abastecimento de áreas remotas.
 
O transporte fluvial é essencial em regiões como a Amazônia, onde rodovias são escassas. Muitas comunidades e empresas dependem desse meio para envio de mercadorias. No entanto, grande parte dessas operações ocorre de forma manual ou informal, sem sistemas digitais de rastreamento.

Hoje existem sistemas de rastreamento baseados em conexão contínua (internet móvel, celular).
Mas esses sistemas não funcionam bem em regiões remotas.

Logo, existe uma lacuna:
Soluções adaptadas para conectividade intermitente.

Uso de Tecnologias de Rastreamento
Empresas modernas utilizam GPS, telemetria, sensores IoT e integração com ERPs para garantir controle de ponta a ponta.

- Sistemas Tolerantes a Atrasos e Desconexões (DTNs) são arquiteturas de rede projetadas para operar em ambientes com interrupções frequentes, altas taxas de erro ou longos atrasos (latência), como comunicações espaciais, redes de sensores remotos, áreas rurais e cenários de desastre. Utilizam "store-and-forward" (armazenar e encaminhar) para garantir a entrega.
As Redes Tolerantes a Atrasos e Desconexões (DTNs) são uma arquitetura de rede projetada para operar em ambientes "desafiadores", onde a conectividade intermitente, atrasos extremos e altas taxas de erro tornam os protocolos tradicionais (como o TCP/IP) ineficazes. 
Diferente da Internet convencional, que exige um caminho fim-a-fim ativo para a transmissão, as DTNs utilizam uma abordagem de "armazena-e-encaminha" (store-and-forward).
- Arquitetura "Store-and-Forward": Ao contrário da Internet tradicional (TCP/IP), os nós DTN armazenam os dados (bundles) persistentemente quando não há um caminho de ponta a ponta disponível, encaminhando-os apenas quando uma conexão se estabelece.
- Conectividade Intermitente: Os nós da rede podem nunca estar todos conectados ao mesmo tempo.
Longos Atrasos: Podem variar de minutos a dias (comum em comunicações espaciais).
Protocolo Bundle (BP): Funciona como uma camada de "sobreposição" (overlay) acima das camadas de transporte, agrupando dados em blocos (bundles) que são movidos entre nós conforme as oportunidades de contato surgem.
Transferência de Custódia: Um nó pode assumir a responsabilidade (custódia) de uma mensagem, garantindo seu armazenamento persistente até que consiga passá-la para o próximo salto seguro. 

**Exemplos de Aplicação**
	1. Redes Interplanetárias (IPN): Comunicação entre a Terra e sondas ou rovers em Marte, onde o atraso pela velocidade da luz impede o uso de TCP.
	2. Redes de Sensores em Áreas Rurais ou Remotas: Uso de "mulas de dados" (como barcos ou veículos) que coletam informações fisicamente de um ponto e as descarregam em outro.
	3. Comunicações Militares ou de Emergência: Cenários de desastre onde a infraestrutura de rede fixa foi destruída.
    4. Redes Submarinas: Onde a propagação de sinal acústico é lenta e sujeita a muitas interrupções. 

- Alta incerteza na previsão de chegada de cargas em rotas fluviais amazônicas, causada pela ausência de rastreamento estruturado e pela conectividade intermitente, impactando confiança comercial, planejamento logístico e acesso a bens essenciais.
- democratização do rastreamento logístico em ambientes de baixa digitalização.

- Alta incerteza logística no transporte fluvial amazônico para pequenos operadores e varejistas, causada pela baixa digitalização, conectividade intermitente e ausência de soluções acessíveis de rastreamento.

bases públicas:

- Agência Nacional de Águas (nível dos rios)
- AIS marítimo público
- rotas logísticas publicadas
- estudos acadêmicos

Por que o mercado precisa disso?
Hoje, o rastreamento é focado no casco (segurança da embarcação) e não na encomenda.
Para o pequeno varejista ou para quem faz compras online no interior, o status é um "buraco negro" de 10 dias.

- Quem transporta?
Barqueiro ou o próprio varegista
- O que é transportado?
Mercadorias de varejistas e pequenas empresas
- Qual a dificuldade real hoje?
O alto custo do rastreamento satelital de sinal de celular nos rios isolam pequenos produtores e ribeirinhos.
- Onde entra o risco de roubo?
sem o monitoramento das rotas feitas pelas embarcações e sem a previsão da chegada predefinida não se sabe se a carga foi roubada, se teve desvio de rota ou atraso e nem onde pode ter vestígios.

**Problema central**
O técnico:
- conectividade intermitente
- falta de infraestrutura
- baixo custo necessário.
 
O organizacional:
- processos manuais
- falta de padronização
- baixa fiscalização.

A imprevisibilidade continuaria existindo por:
- sazonalidade dos rios
- processos manuais
- baixa digitalização
- falta de padronização de dados
- ausência de histórico.

O fluxo do cenário atual acaba sendo:
Conectividade intermitente → falta de atualização → baixa confiança → impacto econômico.

Quem sofre?
- Pequeno varejista: perde vendas.
- Consumidor: não sabe quando o produto chega.
- Transportador: sofre desconfiança.
- Região: menor digitalização.

O que acontece quando uma encomenda “desaparece” no sistema atual?
O cliente começa a ter dúvidas e incertezas sobre o produto e o vendedor perde credibilidade.
O problema é incerteza informacional.

**OBJETIVO**  - define o que o sistema FAZ
- O objetivo inicial é validar a viabilidade da arquitetura assíncrona para reduzir lacunas informacionais.

O que o sistema realmente precisa guardar?

- embarcação
- viagem
- encomenda
- histórico de localização
- eventos (chegada em porto, atraso etc.)


MVP mínimo:

- Um script simula o barco.
- Ele perde conexão.
- Guarda dados.
- Recupera conexão.
- Envia histórico.
- API reconstrói trajetória.
- Usuário vê histórico completo.

 O MVP precisa provar:

• um pequeno transportador consegue rastrear
• o cliente consegue visualizar
• funciona offline
• sincroniza depois

Existem três níveis de maturidade:

- Nível 1 (MVP): dados simulados.
- Nível 2: dados históricos públicos.
- Nível 3: integração com sensores reais.

esse tipo de dado é relacional ou não?
Se uma encomenda pertence a uma viagem, e a viagem pertence a uma embarcação: relacional. Então faz sentido PostgreSQL.
Esse é o tipo de raciocínio que empresas como Uber usam para decisões de arquitetura geográfica.

Vamos usar dados simulados baseados em trajetórias reais e variáveis públicas como nível de rios.
- simulação + validação com fontes reais.

não é o local, é o trajeto. Mesmo perto de cidades há trechos sem sinal.

Problema já definido → falta de monitoramento acessível.
Então a solução precisa atacar acessibilidade, baixo custo e conectividade instável.


Solução

- Desenvolver e avaliar um protótipo de monitoramento assíncrono baseado em armazenamento local e sincronização posterior, visando reduzir lacunas de rastreamento em ambientes de conectividade intermitente.

- Uma API leve que consome poucos dados é perfeita para a infraestrutura instável do Norte.
O hardware é barato (ESP32) e a necessidade é alta. O sucesso depende da sua capacidade de gerir dados offline e de uma interface simples para o usuário.

- "Enquanto sistemas comerciais focam em áreas urbanas densamente conectadas, este projeto propõe uma arquitetura para Zonas de Silêncio Digital, comuns na Região Norte, utilizando sincronização assíncrona para garantir a previsibilidade logística."

- Armazenamento Offline (Datalogging)
A maior parte da viagem não tem sinal GPRS/4G. Se o seu ESP32 tentar enviar dados e falhar, a coordenada se perde.
- Visualização:
 bibliotecas como Leaflet ou Google Maps API para mostrar o mapa com a bússola e os pontos.

- Apenas mostrar um ponto no mapa é pouco. O diferencial da API seria o cálculo de ETA (Estimated Time of Arrival) considerando:
Velocidade da Correnteza: Subir o rio é mais lento que descer.
Sazonalidade: Na seca, o barco faz rotas mais longas para evitar bancos de areia.
Se sua API cruzar a coordenada do ESP32 com dados de nível do rio (da ANA - Agência Nacional de Águas), sua previsibilidade será melhor que a de grandes transportadoras.

- Privacidade: Níveis de Acesso. O varejista só vê a embarcação que contém a carga dele (vinculada pelo ID do pedido).

Soluções inviáveis para o foco, mas encontradas:
- 
 Baixo Custo: 
 Em vez de pagar mensalidade de satélite, o barco usa a rede LoRa gratuita.

  Armazenamento Local:
 Quando o barco entra em "zona cega" (sem nenhuma antena LoRa ou Wi-Fi por perto), o hardware salva as coordenadas em um cartão SD ou na memória interna (isso se chama Data Logging).

 O Envio: 
 Assim que o barco passa por uma comunidade ribeirinha ou porto que tenha um Gateway LoRa (antena receptora), o dispositivo "descarrega" todo o histórico de uma vez para a sua API.

 ESP32 (com LoRa integrado): Como o Heltec WiFi LoRa 32 ou o TTGO LoRa. Ele já tem Wi-Fi, Bluetooth e o rádio LoRa em uma placa só.

 Tratamento de Dados: A API recebe as coordenadas brutas e as "plota" no mapa.



Soluções futuras: 
- Tratamento de Dados: A API recebe as coordenadas brutas e as "plota" no mapa.

IA de Predição: um modelo de Regressão ou Redes Neurais Simples para comparar o tempo de viagem histórico entre o Ponto A e o Ponto B, considerando a correnteza do rio (sazonalidade) para dar o Tempo Estimado de Chegada (ETA).

Alertas de Segurança: Se a IA detectar que o barco parou em um local não programado por muito tempo ou saiu da rota usual, o sistema dispara um alerta de "Possível Sinistro/Roubo".

Com hardware na prática(farei coonceitual):

Independência de Infraestrutura: O sistema funciona "ponto a ponto". O barqueiro só precisa do hardware (que você montou) e de um ponto de internet qualquer no destino.
PÚBLICO
- pequenos operadores que não têm acesso às tecnologias atuais.

O que medir?
- tempo de atraso na atualização
- número de eventos registrados
- continuidade da trajetória
- redução de “buracos” de rastreamento.

1. Entidades do sistema 
• embarcação
• encomenda
• trajeto
• posição
• usuário

- quem usa
Varegista, cliente final e ha a p[ossibilidade do barqueiro fica opcional para ele. ]
- pra quê
varegista:
Visualiza suas cargas, ve onde foi a ultima atualizacao e tem,po estimado, ve todos os eventos e alertas de desvio ou possivel roubo e se necessario troca de embarcação.
Cliente final: ve informacoes somente da propria encomenda.
Barqueiro: caso queira acessar pode ver cada mercadoria vinculada a cada varegista e cliente final talvez, ve a rota calculada que sera feita, olha o histolrico de cargas concluidas e futuras, pode ver a atua que ta responsavel e incluir detalhamento.
- em qual cenário
Regiões com conectividades intermitentes com comunidades com baixo acesso a digitalização.

Fontes
Foi separado em 3 tópicos a busca por artigos academicos:
 Tecnologia de Conectividade

 Contexto Regional

 Redes Tolerantes a Atrasos

 Mais precisamente:
 - Contexto e Logística na Amazônia
 - Tecnologias Atuais e Limitações
 - Redes Tolerantes a Atrasos e Soluções
 - Público Afetado e Impacto Social

**Critério de avaliação: clareza, delimitação do escopo e coerência com a solução proposta**

**Informações:**

 Descrição clara do problema a ser resolvido
- A logística fluvial na Amazônia é responsável pela maior parte do transporte de mercadorias, sendo essencial para o abastecimento de comunidades e atividades comerciais. Entretanto, a gestão dessas operações ainda apresenta baixa digitalização e forte dependência de processos manuais. Como consequência, existe limitada visibilidade sobre a localização e o progresso das cargas ao longo da cadeia logística. 

Essa limitação é agravada pela conectividade intermitente, que impede a atualização contínua de sistemas de rastreamento baseados em comunicação em tempo real. Dessa forma, clientes, varejistas e transportadores enfrentam incerteza quanto à previsão de entrega, dificultando planejamento, reposição de estoque e tomada de decisão. 

Embora tecnologias emergentes de conectividade por satélite, como as oferecidas pela Starlink, tenham ampliado o acesso à internet em regiões remotas, sua adoção ainda é limitada entre pequenos operadores devido a custos e complexidade operacional. Consequentemente, existe uma lacuna tecnológica para soluções de monitoramento adaptadas a ambientes de conectividade intermitente e baixo custo. 

Esse tipo de problema também é discutido em cadeias logísticas de grande escala, como as exploradas por empresas de comércio eletrônico, a exemplo da Amazon, nas quais a previsibilidade e a transparência são fatores críticos de confiança. 

- Definição do Problema

O transporte fluvial é um dos principais meios de distribuição de mercadorias em regiões ribeirinhas do Brasil, especialmente em áreas afastadas de grandes centros urbanos. Pequenos varejistas dependem de embarcações de pequeno porte para transportar produtos como alimentos perecíveis, encomendas e insumos comerciais.

Entretanto, esse tipo de logística apresenta limitações significativas relacionadas à falta de visibilidade sobre o deslocamento das embarcações. Em muitos casos, a comunicação entre transportador e varejista ocorre apenas por meio de mensagens ou ligações telefônicas, sem qualquer registro confiável do percurso realizado.

Essa ausência de monitoramento gera problemas como atrasos imprevisíveis, dificuldades no planejamento de estoque e riscos de perda ou desvio de mercadorias. Além disso, regiões ribeirinhas frequentemente apresentam conectividade limitada à internet, o que dificulta o uso de sistemas tradicionais de rastreamento logístico que dependem de conexão contínua.

Diante desse cenário, surge a necessidade de soluções tecnológicas acessíveis que permitam monitorar o deslocamento de embarcações mesmo em ambientes com conectividade intermitente, oferecendo maior previsibilidade e segurança para pequenos varejistas.

- Proposta de Solução

Este projeto propõe o desenvolvimento de um sistema de monitoramento logístico voltado para pequenas embarcações utilizadas no transporte fluvial de mercadorias.

A solução consiste em um dispositivo de rastreamento baseado em microcontrolador que coleta periodicamente coordenadas GPS durante o trajeto da embarcação. Em situações em que não há conexão com a internet, os dados são armazenados localmente no dispositivo.

Quando o sistema detecta disponibilidade de rede, os dados coletados são enviados automaticamente para uma API responsável por armazenar e processar o histórico de rotas.

Essas informações são disponibilizadas em uma interface web que permite ao varejista visualizar o trajeto percorrido pela embarcação e obter uma estimativa de chegada baseada na análise do histórico de deslocamento.

A arquitetura proposta foi projetada para operar de forma eficiente em ambientes de conectividade limitada, permitindo sincronização posterior dos dados e garantindo que o sistema continue registrando informações mesmo durante períodos offline.

• Contextualização (domínio de aplicação)
Na Amazônia e em regiões como Belém, o transporte fluvial é essencial para: 

 – logística 
 – comércio 
 – distribuição 
 – pequenos empreendedores 

Mas muitas dessas operações: 

 – não têm rastreamento 
 – dependem de contato manual 
 – têm baixa visibilidade 
 – enfrentam riscos de atraso e perda 

Isso gera: 

 – ineficiência 
 – falta de confiança 
 – dificuldade de planejamento 
 – risco de fraude ou roubo 

O problema não é falta de tecnologia. 
O problema é falta de soluções acessíveis e adaptadas à realidade local. 

• Público-alvo (stakeholders)

• Justificativa da relevância do problema
Hoje, grandes empresas usam sistemas caros de rastreamento com satélite, sensores e infraestrutura. Exemplos incluem soluções de empresas como Garmin e Iridium Communications. Essas tecnologias são caras, complexas e fora da realidade de pequenos operadores fluviais. `
 A tecnologia existe, mas não chega aos pequenos. 

custo, acessibilidade e adaptação ao contexto. 

A opção por uma arquitetura Web-First e hardware dedicado na embarcação visa mitigar riscos operacionais comuns na região, como o roubo de dispositivos móveis e a baixa autonomia de bateria. Além disso, a segregação de dados por nível de privilégio é uma medida crítica de segurança para prevenir o monitoramento indevido de rotas por agentes externos, garantindo a integridade da carga e dos operadores.

Fontes
Foi separado em 3 tópicos a busca por artigos academicos:
 Tecnologia de Conectividade

 Contexto Regional

 Redes Tolerantes a Atrasos

 Mais precisamente:
 - Contexto e Logística na Amazônia
 - Tecnologias Atuais e Limitações
 - Redes Tolerantes a Atrasos e Soluções
 - Público Afetado e Impacto Social

**Fontes:** 
"Apesar da alta competitividade do frete hidroviário na Amazônia, custando apenas $8,00 por tonelada (MIRANDA; SILVA, 2023), a falta de digitalização e a baixa capilaridade logística impedem que pequenos operadores usufruam plenamente dessa eficiência."

"Considerando que um único comboio hidroviário substitui mais de 1.600 caminhões (MIRANDA; SILVA, 2023), o monitoramento digital torna-se indispensável para gerir essa escala de carga e garantir que o modal hidroviário cumpra seu papel na redução da emissão de carbono conforme o Acordo de Paris."

"A eficiência do monitoramento na Amazônia é condicionada pela sazonalidade hidrológica, onde o período de vazante exige adaptações estratégicas para evitar o desabastecimento (PEREIRA et al., 2025). O sistema proposto visa mitigar essa 'exclusão logística' ao fornecer dados de previsibilidade mesmo em vias desprovidas de infraestrutura formal de hidrovia."

"A logística na região não enfrenta apenas distâncias, mas uma oscilação vertical de até 6 metros entre cheia e vazante (PORTO DE MANAUS, 2025). O SID-A justifica-se ao permitir que o monitoramento assíncrono registre como essa sazonalidade afeta o tempo de viagem (ETA), auxiliando na resiliência das comunidades frente a eventos extremos como a cheia histórica de 2021 (PEREIRA et al., 2025)."

"Diferente das cadeias logísticas tradicionais, o modal amazônico é sensível à velocidade da correnteza e à falta de dados históricos (COSTA; PIRES, 2021). O SID-A propõe mitigar essa incerteza informacional através de uma arquitetura que integra o monitoramento de posição às variáveis sazonais, permitindo a transição de uma postura reativa para uma logística preditiva e resiliente (PEREIRA et al., 2025)."

"O SID-A adota uma abordagem estruturada de monitoramento contínuo para evitar que riscos operacionais se transformem em crises logísticas (VASCONCELOS; BRITO, 2021). Através da análise de eventos detectados pelo hardware, o sistema prioriza alertas baseados na severidade e probabilidade, seguindo as diretrizes de ferramentas como o FMEA aplicadas ao contexto de IP4s amazônicas (PEREIRA et al., 2025)."

"Como evidenciado pelo estudo de caso em Santa Isabel do Rio Negro, a logística fluvial amazônica opera sob um risco constante de isolamento geográfico e interrupção da navegabilidade (PEREIRA et al., 2025). O SID-A atua precisamente na mitigação desses riscos, fornecendo a visibilidade informacional necessária para que operadores e comunidades se adaptem à severa sazonalidade dos rios amazônicos."

"A logística na Amazônia não é apenas uma questão de movimentação de carga, mas um instrumento de dignidade social para populações isoladas (CAVALCANTE et al., 2019). O SID-A busca honrar essa tradição de 'arte de organizar' ao propor uma coordenação integrada e tecnológica que reduza a distância entre produção e consumo em áreas de difícil acesso."

"O transporte hidroviário na Amazônia não é apenas um modal de baixo custo, mas um setor em expansão que movimentou mais de 23 milhões de toneladas em 2021 (GUITARRA, 2024). Segundo a teoria da logística integrada, a eficiência desse fluxo depende da circulação bidirecional de informações entre o ponto de origem e o consumidor final (NOBRE, 2023), lacuna que o SID-A visa preencher."

"A Amazônia concentra 80% das vias navegáveis exploradas do país, com mais de 16 mil quilômetros de extensão (MATOS, 2017). Contudo, a eficiência dessa vasta malha é limitada pela sinuosidade e pelo comportamento da vazante (COSTA; PADULA, 2009), evidenciando a necessidade de sistemas de monitoramento que auxiliem na navegação em trechos desprovidos de sinalização física."

"A seca histórica de 2023, a pior em 121 anos (ESPINOZA et al., 2024), evidenciou a fragilidade do abastecimento na Amazônia, resultando em gastos emergenciais superiores a R$ 140 milhões em dragagens (BRASIL, 2023). O SID-A justifica-se como uma ferramenta de resiliência, permitindo monitorar o fluxo de mercadorias essenciais mesmo quando o calado reduzido força a descentralização do transporte para embarcações menores."

"Apesar da projeção de investimentos do Novo PAC até 2026 (CASA CIVIL, 2024), a infraestrutura brasileira sofreu uma queda de 16,42% em relação ao PIB nas últimas duas décadas (OLIVEIRA, 2024). Nesse cenário de escassez, figuras como o 'Regatão' continuam sendo os principais elos de abastecimento em igarapés remotos (NETO; NOGUEIRA, 2019), tornando urgente a criação de soluções tecnológicas de baixo custo que tragam segurança a esses operadores."

"O SID-A não visa apenas a eficiência logística, mas também a governança ambiental (ESG), uma vez que o descarte inadequado de efluentes e resíduos nas margens dos rios é um problema crônico do modal (MELO; MELO, 2023). Ao digitalizar o monitoramento, o sistema abre espaço para futuras integrações que fiscalizem e orientem práticas sustentáveis em trajetos de longa distância (ANTAQ, 2024)."

"O SID-A atua no centro do paradoxo logístico amazônico: ao mesmo tempo que o modal fluvial é o mais econômico, ele é o mais vulnerável à insegurança e à falta de dados (MELO; MELO, 2023). Integrar o monitoramento assíncrono à agenda ESG do MPor (2024-2027) não é apenas uma inovação técnica, mas uma necessidade para garantir que a abundância natural dos rios se transforme em eficiência e segurança para o transportador e para o cidadão."

"Como proposto por Taveira e Alves Neto (2025), o futuro da logística amazônica depende da integração de sistemas de rastreamento que permitam o ajuste operacional frente às crises climáticas. O SID-A materializa essa visão ao oferecer uma arquitetura resiliente que transforma o monitoramento de dados em uma ferramenta de planejamento estratégico para o transporte em águas rasas."

"A escolha da tecnologia LoRa fundamenta-se na sua resiliência em zonas de silêncio digital, permitindo a criação de redes privadas sem dependência de operadoras (MILESI, 2025). O SID-A utiliza a modulação Chirp Spread Spectrum (CSS) com ajuste dinâmico de Spreading Factor para garantir que as coordenadas de rastreamento sejam preservadas mesmo em condições de baixa relação sinal-ruído típicas do modal fluvial."

"Embora a transformação digital promova a sustentabilidade e a precisão na tomada de decisão (REINARTZ et al., 2019), sua implementação em pequenos operadores logísticos enfrenta barreiras como elevados custos iniciais e resistência cultural (GURUMURTHY; BHARTHUR, 2019). O SID-A propõe mitigar essas desigualdades tecnológicas (MELO, 2024) através de uma solução de baixo custo e interface intuitiva, focada na inclusão digital."

"A arquitetura do SID-A baseia-se no modelo SMACIT (SEBASTIAN et al., 2017), integrando IoT e Mobile para superar a inércia tecnológica em pequenos operadores. Ao adotar uma cultura orientada por dados (KLEIN; TODESCO, 2020), o sistema não apenas rastreia cargas, mas promove o alinhamento estratégico e a competitividade de PMEs no modal hidroviário (ULAS, 2019)."