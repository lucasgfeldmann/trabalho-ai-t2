# Especificação de Requisitos: CaliForge

Este documento contém todos os requisitos funcionais e não-funcionais validados pela especificação de produto e técnica do CaliForge.

---

## ⚙️ Requisitos Funcionais (RFs)

Requisitos que descrevem as funcionalidades ativas do sistema:

### [RF-001] Geração de Treinos Adaptativos e Conversacionais
* **Descrição:** O sistema gera rotinas de calistenia flexíveis e personalizadas de acordo com o nível físico, histórico e preferências do usuário, coletando os dados de forma progressiva e conversacional em diálogos diários.
* **Entradas Exigidas:** Dados do perfil do usuário em formato JSON (`CaliForgeUserInput`) contendo:
  - Identificação básica (userId, nome, idade, altura, peso).
  - Histórico de saúde (restrições médicas, problemas de mobilidade).
  - Nível de força nos eixos de calistenia (`movementLevels`: push, pull, legs, abs).
  - Disponibilidade de equipamentos (`equipmentAvailability`).
  - Consistência semanal (`weeklyConsistency`).
* **Saídas Esperadas:** Objeto JSON estruturado de treino (`CaliForgeWorkoutOutput`) contendo:
  - Identificação do treino (workoutId, data, foco anatômico).
  - Lista de exercícios (`exercises` contendo nome, categoria, nível, séries, faixa de repetições, tempo de descanso e guia de execução).
  - Notas de recuperação e avisos de segurança (`recoveryNotes`).
* **Regras de Negócio Associadas:**
  - **Massa Crítica Obrigatória:** A geração de treino exige um conjunto mínimo de dados coletado no primeiro uso (Biometria, Presença/Ausência de dores articulares e restrições médicas, equipamentos disponíveis e teste físico inicial).
  - **Teste Físico Conversacional:** Se o usuário não souber seu nível físico, a IA o instrui a realizar um exercício básico pelo chat. O nível de força inicial é determinado dinamicamente com base nas repetições e dificuldade relatadas.
  - **Evolução Colaborativa:** A progressão de nível de um exercício não é linear nem puramente matemática. O algoritmo analisa o padrão de consistência semanal e a prontidão física do usuário, propondo conversacionalmente o avanço. A decisão de subir de nível é compartilhada e confirmada no diálogo de check-in (validando energia, motivação e cansaço).
  - **Adaptação a Fadiga Subjetiva:** Se o usuário relatar cansaço ou rendimento abaixo do normal no diálogo de check-in, o sistema sugere manter o nível ou regredir temporariamente para preservar a consistência.
  - **Salvaguarda Muscular Mínima:** Customizações de treino pelo usuário respeitam um volume semanal mínimo nos eixos anatômicos de sustentação opostos para evitar desbalanços (equilíbrio Push/Pull).
  - **Fallbacks de Dados Incompletos:** Na ausência de dados de entrada opcionais durante o onboarding progressivo, o sistema aplica fallbacks seguros:
    * `experienceLevel` -> `"beginner"`
    * `movementLevels` -> Nível `1` em todos os eixos (`push: 1`, `pull: 1`, `legs: 1`, `abs: 1`)
    * `painState` -> `0` (sem dor ativa em todas as articulações)
    * `equipmentAvailability` -> `false` em todos (bodyweight puro)
    * `weeklyConsistency` -> `completedWorkoutsThisWeek: 0` e `targetWorkoutsPerWeek: 3`

### [RF-002] Manejo Dinâmico de Dores e Reabilitação
* **Descrição:** Se o usuário relatar desconforto ou dores nas articulações, o sistema bloqueia exercícios agressores, altera as progressões para menor impacto e inclui exercícios educativos de mobilidade/reabilitação, gerenciando o estado de dor de forma temporal.
* **Entradas Exigidas:** Mapeamento de dor articular (`painState` com intensidade de 1 a 5 nas articulações do punho, ombro, cotovelo, joelho e lombar).
* **Saídas Esperadas:** Prescrição adaptada sem os exercícios causadores de estresse na articulação afetada, inclusão de variações de menor impacto e conselhos específicos de reabilitação no campo `recoveryNotes`.
* **Regras de Negócio Associadas:**
  - **Pain Lockout (Bloqueio de Dor Aguda):** Se o relato de dor em uma articulação for maior ou igual a `3` (intensidade aguda), o sistema bloqueia sumariamente qualquer exercício correspondente à categoria agressora (ex: dor no punho >= 3 bloqueia flexões comuns e dips na paralela). Substitutos como flexões inclinadas elevadas na parede ou flexões sobre os punhos fechados são sugeridos.
  - **Exercícios de Reabilitação:** Em caso de dores, o treino incorpora exercícios específicos de reestabelecimento de mobilidade articular de baixo impacto.
  - **Ciclo de Vida e Decaimento de Dores (TTL e Decaimento):**
    * **TTL do Relato:** Qualquer intensidade de dor relatada (1 a 5) tem validade de **7 dias** a partir do último check-in onde foi mencionada.
    * **Decaimento por Inatividade:** Se o usuário ficar **7 dias corridos sem novos relatos** daquela articulação, a intensidade da dor é reduzida em **1 nível** automaticamente a cada 7 dias de silêncio, até atingir 0 e remover o bloqueio.
    * **Gatilho de Reavaliação:** A cada **3 sessões de treino concluídas** sob regime de dor articular, a IA dispara uma pergunta de reavaliação no chat de check-in diário. O feedback subjetivo do usuário atualiza imediatamente o banco de dados.

### [RF-003] Sincronização Conversacional de Treino (Chat Sync)
* **Descrição:** O interpretador de chat em linguagem natural atualiza de forma síncrona o Painel do Plano de Treino a partir de mensagens coloquiais enviadas pelo usuário.
* **Entradas Exigidas:** Frases coloquiais no chat registrando desempenho (ex: *"hoje fiz 3x10 flexões e 2x12 agachamentos"*).
* **Saídas Esperadas:** Inputs de séries e repetições correspondentes preenchidos e marcados automaticamente como concluídos no dashboard reativo do usuário.
* **Regras de Negócio Associadas:**
  - A IA processa o texto, mapeia a correspondência do exercício com a lista do dia e atualiza o estado da série no banco de dados. Se houver discrepâncias de nome (ex: *"flexões normais"* em vez de *"flexão tradicional"*), o interpretador utiliza mapeamento flexível de sinônimos.

---

## 📐 Requisitos Não-Funcionais (RNFs)

Requisitos que descrevem atributos de qualidade, desempenho ou restrições técnicas:

### [RNF-001] Design Visual Híbrido e Minimalista (UX/UI)
* **Descrição:** A interface deve seguir um layout minimalista e integrado de três telas principais (T1: Chat híbrido com Dashboard Ocioso, T2: Painel de Treino Diário com inputs/sync e T3: Calendário Mensal com memória contextual diária).
* **Métrica de Validação:**
  - Interface baseada inteiramente em **Sleek Dark Mode** (Fundo Escuro) com tokens HSL.
  - Paleta HSL de status rigorosa: Verde para exercícios concluídos, Amarelo para reabilitação/mobilidade e Coral para dores articulares relatadas.
  - Transições fluidas (micro-animações suaves) entre o painel de chat e o dashboard.

### [RNF-002] Segurança e Conformidade Física de Prescrição (Segurança)
* **Descrição:** O algoritmo de treino deve ser robusto e seguro contra prescrições incorretas que aumentem o risco de lesão corporal (como propor exercícios para articulações inflamadas ou progredir a carga de usuários inconstantes).
* **Métrica de Validação:**
  - Execução automatizada de testes no Harness Engineering.
  - **100% de sucesso nas asserções binárias:** Segurança de dor (Pain Lockout), Equilíbrio Push/Pull (ratio entre 0.8 e 1.2 no fullbody) e Bloqueio de progressão por baixa consistência (< 2 treinos concluídos na semana).
  - Cobertura total nos 5 casos de teste críticos descritos na especificação.

### [RNF-003] Desempenho e Latência Conversacional (Desempenho)
* **Descrição:** O assistente inteligente e o interpretador de chat devem processar os relatos e gerar respostas de forma rápida, evitando quebras na fluidez da experiência conversacional.
* **Métrica de Validação:**
  - Tempo de resposta (Time to First Token) inferior a **3 segundos** para comandos de chat de sincronização de treino (Chat Sync).
  - Tempo de geração completo do treino adaptativo diário inferior a **5 segundos** sob condições estáveis de rede.
