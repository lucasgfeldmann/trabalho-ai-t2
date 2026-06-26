# Especificação Ativa: CaliForge

Este arquivo contém a especificação de produto e técnica do CaliForge, desenvolvida iterativamente de acordo com o nosso Ciclo de Vida de Especificação.

* **Status Atual:** 🟢 Aprovada para Desenvolvimento (Etapa 3 Concluída pelo Usuário)
* **Última Atualização:** 2026-06-25

---

## 🏁 Etapa 1: Visão Geral e Escopo

### 1. Público-Alvo e Personas
A solução atende a dois perfis principais de praticantes de calistenia, estabelecendo uma relação conversacional onde o perfil de cada um é descoberto de forma gradual ao longo do tempo (sem questionários exaustivos iniciais):
* **Persona A: O Iniciante (Pedro, 24 anos)**
  * **Objetivo:** Começar a treinar usando apenas o peso do corpo, ganhar força básica.
  * **Dificuldade:** Não sabe quais exercícios fazer, não consegue fazer 1 pull-up ainda, treina em casa sem equipamentos (apenas no chão ou usando cadeiras).
  * **Necessidade:** Treinos muito simples, focados em exercícios educativos (flexão de joelho, barra australiana/remada sob a mesa, agachamento livre) e instruções claras de forma.
* **Persona B: O Intermediário (Mariana, 28 anos)**
  * **Objetivo:** Dominar movimentos mais complexos (dips, pull-ups perfeitas, iniciar L-sit) e aumentar a resistência.
  * **Dificuldade:** Platô nos treinos atuais; não sabe como progredir além de apenas adicionar mais repetições de flexões comuns.
  * **Necessidade:** Um guia claro de progressões de exercícios (ex: transição de flexão comum para flexão arqueiro) e controle de volume/intensidade semanal.

### 2. Escopo Funcional (Recursos Chave)
* **RF01 - Geração de Treinos Adaptativos e Conversacionais:** Em vez de sugerir um plano fixo imediato, o sistema coleta o nível físico, histórico e preferências do usuário de forma orgânica durante diálogos cotidianos. Com base nesses dados evolutivos, gera rotinas flexíveis de calistenia.
* **RF02 - Manejo Dinâmico de Dores e Reabilitação:** Se o usuário reportar qualquer desconforto articular (ex: dor no punho), o sistema retira os exercícios agressores, insere variações de menor impacto e exercícios de reabilitação. Conforme o usuário reporta melhoras nos check-ins diários, o sistema reinserirá gradualmente os exercícios padrão.
* **RF03 - Acompanhamento Diário e Insights Educativos:** O sistema acompanha os registros de repetições, metas e progresso diariamente em um formato de diálogo natural, oferecendo dicas sobre execução de movimentos, princípios de calistenia e explicações técnicas.

### 3. Mapeamento de Limitações e Equipamentos
* **Preferências de Equipamento:** 
  A ausência de equipamentos (como barra fixa ou paralelas) é tratada como uma preferência de ambiente. O sistema prioriza treinos sem equipamentos (bodyweight puro). O assistente pergunta de forma natural sobre a disponibilidade de novos equipamentos. Pode sugerir, de maneira sutil e contextualizada ("sem encher o saco do usuário"), exercícios correspondentes com equipamento baseando-se no perfil dele (ex: sugerir barra australiana tradicional se ele conseguir acesso a uma barra).
* **Mapeamento e Recuperação de Dores Articulares:**
  * *Fase de Alerta:* Dor relatada -> Corte imediato de exercícios que tensionem a área afetada. Mapeamento de substitutos (ex: flexão inclinada na parede ou flexão sobre punhos fechados para dores nos punhos).
  * *Fase de Reestabelecimento:* Inclusão de exercícios educativos leves e de mobilidade para restabelecer o movimento de forma progressiva.
  * *Fase de Recuperação:* Validação do estado de dor após alguns dias; se recuperado, o exercício original volta ao plano de forma progressiva.
## 🚦 Checklist de Validação da Etapa 1

- [x] **Item 1:** Personas do usuário bem definidas e validadas.
- [x] **Item 2:** Escopo de recursos (Geração de Treino, Progressão, Acompanhamento) detalhado e sem ambiguidades.
- [x] **Item 3:** Mapeamento de equipamentos e restrições acordado.

---

## 📐 Etapa 2: Requisitos do Projeto / Sistema a ser Desenvolvido

### 1. Requisitos de Movimento, Progresso e Domínio (CaliForge Core Rules)
* **RF01 - Faixas de Repetição Flexíveis:** Cada movimento prescrito deve conter faixas de repetição (ex: 3 séries de 8 a 12 repetições) em vez de números fixos.
* **RF02 - Evolução Colaborativa:** A progressão não ocorre por cálculos mecânicos puros. O sistema analisa o padrão de consistência geral e propõe a evolução no diálogo de check-in, validando os sentimentos (energia, motivação) e co-decidindo o avanço com o usuário.
* **RF03 - Adaptação à Fadiga Subjetiva:** Relatos de exaustão física/mental reduzem o volume ou mantêm o nível atual, priorizando a consistência.
* **RF04 - Equilíbrio Corporal (Push/Pull Ratio):** As sessões devem garantir harmonia anatômica e equilíbrio de volume de esforço semanal entre eixos opostos (Push vs. Pull).
* **RF05 - Ciclo de Vida Temporal de Dores (TTL):** Janela de 7 dias de validade para relatos de dores articulares, decaimento automático de 1 nível após 7 dias de inatividade de relatos, e gatilho de pergunta de reavaliação no check-in a cada 3 treinos concluídos.
* **RF06 - Valores Padrão Seguros (Fallbacks):** Caso informações de biometria, consistência, equipamentos ou dores não sejam coletados no onboarding progressivo, o sistema aplica as regras padrão (nível iniciante, bodyweight solo, sem dor ativa).

### 2. Requisitos de UI/UX e Experiência de Uso (System Interfaces)
* **RF07 - Dashboard Híbrido Reativo (T1):** Exibição do painel do plano do dia/status de exercícios quando ocioso, deslizando suavemente para interface de chat limpa quando o usuário inicia uma interação conversacional.
* **RF08 - Plano do Dia e Entrada Manual (T2):** Exibição de séries/repetições do treino prescrito com inputs onde o usuário pode registrar manualmente as marcas alcançadas.
* **RF09 - Sincronização por Diálogo (Chat Sync):** O assistente interpreta relatos coloquiais no chat (ex: *"hoje fiz 3x10 flexões"*) e preenche automaticamente os inputs de treino no plano do dia.
* **RF10 - Calendário Histórico e Memória Contextual (T3):** Calendário mensal exibindo os dias de treinos concluídos e resumo de notas contextuais do chat daquele dia.

### 🚦 Checklist de Validação da Etapa 2
- [x] **Item 1:** Requisitos de regras funcionais, adaptação à fadiga e sobrecarga progressiva estruturados.
- [x] **Item 2:** Requisitos de interface de usuário (Dashboard híbrido, Chat Sync, Calendário Histórico) consolidados.
- [x] **Item 3:** Requisitos de ciclo de vida de dados (fallbacks de dados vazios e TTL/decaimento de dor) descritos como lógica de sistema.

---

## 🧪 Etapa 3: Critérios de Aceitação

Abaixo estão definidos os critérios de aceitação objetivos (Passa / Não Passa) que validam se o CaliForge cumpre os requisitos de produto especificados:

### 1. Critérios de Segurança e Restrição de Dor (Pain Lockout)
* **[CA-001] Bloqueio contra Dor Aguda:** Se o usuário apresentar estado de dor ativa com intensidade maior ou igual a 3 em uma articulação, exercícios que tensionem essa área devem ser bloqueados (ex: dor no punho >= 3 bloqueia flexões tradicionais e dips nas paralelas).
* **[CA-002] Substituição de Impacto:** Exercícios bloqueados devem ser substituídos por variações de menor impacto ou movimentos educativos leves de mobilidade.

### 2. Critérios de Equilíbrio Corporal e Progressão
* **[CA-003] Equilíbrio Anatômico Fullbody:** Em treinos Fullbody gerados, a relação de volume semanal entre exercícios de Empurrar (Push) e Puxar (Pull) deve ser mantida em proporção equilibrada (Push/Pull ratio entre 0.8 e 1.2).
* **[CA-004] Prevenção de Progressão Acelerada:** O sistema não deve propor evolução no nível de movimento se o usuário registrar consistência semanal menor que 2 treinos concluídos.

### 3. Critérios de Ciclo de Vida e Fallbacks
* **[CA-005] Expiração e Decaimento de Dor:** O nível de dor relatada deve decair linearmente em 1 unidade a cada 7 dias de ausência de novos relatos pelo usuário.
* **[CA-006] Gatilho de Reavaliação Activa:** O assistente deve disparar obrigatoriamente um diálogo de reavaliação de desconforto a cada 3 sessões concluídas.
* **[CA-007] Integridade de Onboarding Conversacional:** Caso dados opcionais (biometria ou equipamentos) não sejam providos, o sistema deve assumir nível iniciante, sem dor e treino com peso corporal puro, sem quebrar o fluxo.

### 🚦 Checklist de Validação da Etapa 3
- [x] **Item 1:** Critérios de aceitação para segurança articular e substituição de impacto definidos.
- [x] **Item 2:** Critérios de proporção de volume muscular e progressão por consistência estabelecidos.
- [x] **Item 3:** Critérios de validade temporal de dados e fallbacks de onboarding integrados.

