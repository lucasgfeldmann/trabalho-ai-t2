# Especificação Ativa: CaliForge

Este arquivo contém a especificação de produto e técnica do CaliForge, desenvolvida iterativamente de acordo com o nosso Ciclo de Vida de Especificação.

* **Status Atual:** 🟢 Aprovada para Desenvolvimento (Etapa 5 Concluída)
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

### 4. Massa Crítica de Dados (Estado Mínimo Viável)
Para que o gerador de treinos do CaliForge possa rodar sem gerar rotinas inseguras ou incompatíveis, a IA deve obter obrigatoriamente as seguintes quatro categorias de variáveis (Massa Crítica) no fluxo inicial:
1. **Dados de Identificação e Biometria Básica:** Nome, idade, altura e peso (dados essenciais para entender a sobrecarga articular e o biotipo corporal do usuário na calistenia).
2. **Histórico de Saúde e Limitações Físicas:**
   - Mapeamento explícito de presença ou ausência de dores articulares (punho, ombro, cotovelo, joelho, lombar).
   - Mapeamento de problemas de mobilidade, deficiências ou restrições médicas gerais de saúde.
3. **Mapeamento de Nível Físico por Teste Prático Guiado:**
   - Se o usuário souber informar, registra-se os parâmetros de exercícios de calistenia que ele já consegue executar.
   - Se o usuário for iniciante ou não souber informar, a IA prescreve um **Teste Físico Conversacional**: instrui o usuário a realizar um exercício básico (ex: flexões no chão ou agachamentos simples). Com base no feedback de repetições e dificuldade relatado pelo usuário, a IA aumenta ou diminui progressivamente o nível dos movimentos sugeridos até mapear com exatidão a faixa de força inicial.
4. **Disponibilidade de Equipamentos:** Acesso a barras fixas, barras paralelas ou elásticos (se indisponível, assume fallback de peso corporal puro).

---

## 🚦 Checklist de Validação da Etapa 1

- [x] **Item 1:** Personas do usuário bem definidas e validadas.
- [x] **Item 2:** Escopo de recursos (Geração de Treino, Progressão, Acompanhamento) detalhado e sem ambiguidades.
- [x] **Item 3:** Mapeamento de equipamentos e restrições acordado.
- [x] **Item 4:** Massa Crítica de Dados (Estado Mínimo Viável) e fluxo de teste físico dinâmico definidos formalmente.

---

## 📐 Etapa 2: Modelo de Domínio e Progressão

### 1. Categorias de Movimento e Progressão Geral
Cada treino do CaliForge é estruturado em quatro eixos principais de movimento na calistenia:
1. **Empurrar (Push):** Flexão na parede ➔ Flexão inclinada ➔ Flexão de joelhos ➔ Flexão tradicional ➔ Flexão diamante ➔ Flexão arqueiro ➔ Pseudo-planche push-ups ➔ Dips (paralelas).
2. **Puxar (Pull):** Remada sob a mesa/australiana inclinada ➔ Remada australiana horizontal ➔ Barra fixa negativa ➔ Barra fixa supinada (chin-up) ➔ Barra fixa pronada (pull-up) ➔ L-sit pull-up.
3. **Pernas (Legs):** Sentar e levantar da cadeira ➔ Agachamento livre ➔ Agachamento sumô ➔ Agachamento búlgaro ➔ Agachamento pistola (pistol squat) assistido ➔ Pistol squat livre.
4. **Core (Abs/Lombar):** Prancha frontal ➔ Elevação de joelhos deitado ➔ Abdominal remador ➔ Hollow body hold (canoa) ➔ Elevação de joelhos na barra ➔ L-sit hold.

### 2. Regras de Sobrecarga Progressiva e Adaptação
* **Meta de Repetições:** O usuário recebe uma faixa de repetições flexível por exercício (ex: 3 séries de 8 a 12 repetições).
* **Evolução Colaborativa (Sem Números Mágicos Rígidos):** A progressão não ocorre por cálculos mecânicos puros (ex: completar 3x12 ou bater 3 treinos consecutivos). Em vez disso, o sistema analisa o *padrão de consistência* geral (desempenho e regularidade semanal) e, ao identificar prontidão física, a IA **propõe de forma conversacional e colaborativa o avanço**. No diálogo de check-in, a IA valida os sentimentos do usuário (energia, motivação e cansaço) e a decisão de evoluir o nível é compartilhada e baseada nos objetivos e desejos expressos por ele.
* **Regressão e Adaptação a Fadiga Subjetiva:** Se o usuário relatar que o treino foi excessivamente exaustivo ou que seu rendimento caiu devido a cansaço físico/mental, o algoritmo se adapta de forma compreensiva, sugerindo manter o nível ou regredir temporariamente para preservar a consistência da rotina, em vez de penalizar o usuário.
* **Análise de Frequência e Recuperação:** O sistema monitora o histórico de frequência de treinos semanais. A meta principal é a consistência da rotina a longo prazo e a saúde articular. O algoritmo incentiva descansos ativos e regula o volume se detectar sinais cumulativos de fadiga, reforçando o repouso como parte do progresso.

### 3. Filosofia de Equilíbrio Corporal e Preferências (Saúde Primeiro)
* **Equilíbrio Musculoesquelético:** Por padrão, o sistema planeja as sessões garantindo harmonia anatômica. Isso envolve manter uma relação equilibrada de volume semanal entre padrões de movimento opostos (como empurrar vs. puxar) para proteger a integridade dos ombros e a postura.
* **Foco em Saúde Articular:** A seleção de progressões prioriza o fortalecimento passivo e a mobilidade de forma gradual, de acordo com o nível físico estimado.
* **Customização com Salvaguarda:** O usuário pode configurar preferências específicas de foco (ex: *"priorizar pernas"* ou *"priorizar membros superiores"*). No entanto, o algoritmo garante um patamar mínimo de atividade em todos os outros eixos corporais de sustentação para prevenir desbalanços. A IA atua didaticamente no diálogo explicando a importância desse equilíbrio para a saúde a longo prazo.

### 🚦 Checklist de Validação da Etapa 2
- [x] **Item 1:** Mapeamento de exercícios principais (Empurrar, Puxar, Pernas, Core) e suas progressões de nível acordados.
- [x] **Item 2:** Tabela de progressão validada para as personas definidas.
- [x] **Item 3:** Regras de sobrecarga progressiva e regressão adaptativas estabelecidas.

---

## 🖥️ Etapa 3: Especificação de UI/UX e Design System

### 1. Fluxo de Telas (Design Híbrido e Minimalista)
O sistema deve conter o menor número de telas possível, focando em simplicidade e interação centralizada:

* **T1: Tela Principal (Chat + Dashboard Híbrido)**
  * *Estado Inicial/Ocioso:* Quando o usuário acessa o aplicativo e não iniciou a troca de mensagens na sessão, exibe o painel do plano do dia ou o progresso (exercícios concluídos vs. restantes).
  * *Estado Ativo:* Interface de chat limpa e premium para interações naturais do dia com o assistente inteligente de treino.
* **T2: Painel de Plano do Dia (Status & Entrada)**
  * *Exibição de Informações:* Detalhes completos do treino prescrito (séries, repetições, tempos de descanso e notas).
  * *Inserção Manual:* Inputs rápidos onde o usuário pode marcar diretamente os conjuntos (sets) e repetições que concluiu.
  * *Sincronização por Diálogo (Chat Sync):* Caso o usuário digite suas marcas no chat de forma coloquial (ex: *"hoje fiz 3x10 flexões e 2x8 agachamentos"*), a IA interpreta a frase e atualiza automaticamente os inputs correspondentes no Painel de Treino do Dia.
* **T3: Tela de Calendário (Histórico & Memória Contextual)**
  * *Frequência de Treino:* Calendário mensal marcando visualmente os dias de treino ativo concluídos.
  * *Resumo Diário Contextual:* Clicar em um dia exibe o histórico de exercícios realizados e um cartão de resumo com detalhes relevantes capturados do chat (ex: *"Relatou leve dor nos joelhos no agachamento búlgaro, sugerido focar em agachamentos sumô leves."*).

### 2. Elementos Visuais e Micro-interações
* *Interface Minimalista:* Fundo escuro (sleek dark mode) e uso de HSL para status (concluído, pendente, dor).
* *Transições Premium:* Animações suaves entre o chat e o dashboard quando o usuário começa a interagir ou rolar a página.

### 🚦 Checklist de Validação da Etapa 3
- [x] **Item 1:** Fluxo de telas (Chat híbrido, Plano do Dia com sync e Calendário com resumos) detalhado.
- [x] **Item 2:** Tokens de design e layout minimalista (foco no chat e dashboard integrados) definidos.
- [x] **Item 3:** Protocolo de sincronização entre diálogo (chat) e UI (plano de treino) estruturado.

---

## 💾 Etapa 4: Esquemas de Dados e Contratos

Abaixo estão definidos os contratos de dados JSON Schema para a comunicação com a IA e para fins de validação no Harness. Eles são projetados para acomodar o perfil dinâmico de dores, preferências de equipamentos e a estrutura de treino evolutiva de consistência.

### 1. JSON Schema de Entrada (User Profile & State Input)
Este esquema define as informações do usuário enviadas ao modelo para gerar a rotina diária:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CaliForgeUserInput",
  "type": "object",
  "required": ["userId", "name", "age", "height", "weight", "healthConditions"],
  "properties": {
    "userId": { "type": "string" },
    "name": { "type": "string" },
    "age": { "type": "integer", "minimum": 1, "maximum": 120 },
    "height": { "type": "number", "minimum": 0.5, "maximum": 2.5, "description": "Altura em metros (ex: 1.75)" },
    "weight": { "type": "number", "minimum": 10, "maximum": 300, "description": "Peso em kg (ex: 72.5)" },
    "healthConditions": {
      "type": "object",
      "required": ["hasMobilityIssues", "hasHealthRestrictions"],
      "properties": {
        "hasMobilityIssues": { "type": "boolean" },
        "mobilityDetails": { "type": "string", "description": "Detalhes caso existam problemas de mobilidade ou deficiências" },
        "hasHealthRestrictions": { "type": "boolean" },
        "healthRestrictionsDetails": { "type": "string", "description": "Detalhes de restrições de saúde gerais ou médicas" }
      },
      "additionalProperties": false
    },
    "experienceLevel": { "type": "string", "enum": ["beginner", "intermediate", "advanced"] },
    "movementLevels": {
      "type": "object",
      "required": ["push", "pull", "legs", "abs"],
      "properties": {
        "push": { "type": "integer", "minimum": 1, "maximum": 8 },
        "pull": { "type": "integer", "minimum": 1, "maximum": 6 },
        "legs": { "type": "integer", "minimum": 1, "maximum": 6 },
        "abs": { "type": "integer", "minimum": 1, "maximum": 6 }
      }
    },
    "painState": {
      "type": "object",
      "description": "Estado de dor ativa e intensidade relatada pelo usuário por articulação",
      "properties": {
        "wrist": { "type": "integer", "minimum": 0, "maximum": 5 },
        "shoulder": { "type": "integer", "minimum": 0, "maximum": 5 },
        "elbow": { "type": "integer", "minimum": 0, "maximum": 5 },
        "knee": { "type": "integer", "minimum": 0, "maximum": 5 },
        "lowerBack": { "type": "integer", "minimum": 0, "maximum": 5 }
      },
      "additionalProperties": false
    },
    "equipmentAvailability": {
      "type": "object",
      "required": ["hasPullUpBar", "hasParallelBars", "hasResistanceBands"],
      "properties": {
        "hasPullUpBar": { "type": "boolean" },
        "hasParallelBars": { "type": "boolean" },
        "hasResistanceBands": { "type": "boolean" }
      }
    },
    "weeklyConsistency": {
      "type": "object",
      "properties": {
        "completedWorkoutsThisWeek": { "type": "integer", "minimum": 0 },
        "targetWorkoutsPerWeek": { "type": "integer", "minimum": 1, "maximum": 7 }
      }
    }
  }
}
```

### 2. Valores Padrão Seguros (Fallbacks de Dados Incompletos)
Quando dados opcionais do perfil não forem fornecidos no JSON de entrada durante o fluxo de onboarding progressivo, o sistema aplicará os seguintes fallbacks:

| Campo Opcional | Descrição | Valor Padrão Seguro (Fallback) |
| :--- | :--- | :--- |
| `experienceLevel` | Nível geral do usuário | `"beginner"` |
| `movementLevels` | Nível em cada eixo de exercícios | Nível `1` em todos os eixos (`push: 1`, `pull: 1`, `legs: 1`, `abs: 1`) |
| `painState` | Dores localizadas nas articulações | `0` (sem dor ativa) em todas as articulações |
| `equipmentAvailability` | Equipamentos de calistenia | `false` em todos (bodyweight puro no chão) |
| `weeklyConsistency` | Consistência e meta de treinos | `completedWorkoutsThisWeek: 0` e `targetWorkoutsPerWeek: 3` |


### 3. JSON Schema de Saída (Generated Workout Output)
Este esquema define a estrutura estrita de treino gerada e retornada pela IA:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CaliForgeWorkoutOutput",
  "type": "object",
  "required": ["workoutId", "date", "focus", "exercises", "recoveryNotes"],
  "properties": {
    "workoutId": { "type": "string" },
    "date": { "type": "string", "format": "date" },
    "focus": { "type": "string", "enum": ["push", "pull", "legs", "abs", "fullbody"] },
    "exercises": {
      "type": "array",
      "minItems": 2,
      "items": {
        "type": "object",
        "required": ["exerciseName", "category", "level", "sets", "repsRange", "restSeconds", "executionGuide"],
        "properties": {
          "exerciseName": { "type": "string" },
          "category": { "type": "string", "enum": ["push", "pull", "legs", "abs"] },
          "level": { "type": "integer" },
          "sets": { "type": "integer", "minimum": 1, "maximum": 5 },
          "repsRange": {
            "type": "object",
            "required": ["min", "max"],
            "properties": {
              "min": { "type": "integer", "minimum": 1 },
              "max": { "type": "integer", "minimum": 1 }
            }
          },
          "restSeconds": { "type": "integer", "minimum": 30, "maximum": 300 },
          "executionGuide": { "type": "string", "maxLength": 300 }
        }
      }
    },
    "recoveryNotes": {
      "type": "string",
      "description": "Conselhos de descanso baseados em consistência ou alertas articulares caso dores existam",
      "maxLength": 500
    }
  }
}
```

### 4. Ciclo de Vida e Decaimento de Dados Temporais (Dores Articulares)
Para garantir que as restrições físicas reflitam a recuperação biológica real do usuário, o estado de dores articulares (`painState`) segue regras rígidas de expiração e decaimento temporal:
1. **Janela de Validade (TTL - Time to Live) do Relato:** Qualquer relato de dor articular (intensidade entre 1 e 5) é considerado ativo por uma janela padrão de **7 dias** a partir do timestamp do último check-in onde a dor foi mencionada.
2. **Regra de Decaimento por Tempo (Inatividade):** Se o usuário ficar **7 dias corridos de calendário sem registrar novos relatos** da articulação afetada, o sistema aplica um decaimento linear automático: a intensidade da dor é reduzida em **1 nível** a cada 7 dias (ex: de intensidade 4 para 3). Ao atingir 0, o bloqueio articular é removido.
3. **Gatilho de Reavaliação no Check-in (Conversa Ativa):** A cada **3 sessões de treino concluídas** sob o regime de dor em uma articulação, a IA deve disparar uma pergunta de reavaliação no chat de check-in (ex: *"Como está o seu punho hoje?"*). O feedback subjetivo do usuário atualiza imediatamente a intensidade da dor no banco de dados (redefinindo o valor ou zerando-o se recuperado), reiniciando o ciclo de expiração.

### 🚦 Checklist de Validação da Etapa 4
- [x] **Item 1:** Esquema JSON de entrada validado para suportar restrições articulares e preferências do usuário.
- [x] **Item 2:** Esquema JSON de saída estruturado com faixas de repetições flexíveis e campos específicos para mensagens de reabilitação.
- [x] **Item 3:** Contrato verificado contra todos os cenários das personas (Iniciante sem equipamentos vs. Intermediário).
- [x] **Item 4:** Mapeamento e documentação de valores padrões seguros (fallbacks) para todos os parâmetros de dados opcionais ou incompletos.
- [x] **Item 5:** Definição do ciclo de vida, expiração e regras de decaimento para variáveis mutáveis ou dependentes do tempo (dados temporais).

---

## 🧪 Etapa 5: Critérios de Avaliação e Dataset do Harness

Abaixo são definidos os cenários do dataset de teste do Harness e os critérios de validação automatizada de qualidade de treinos (assertions) para o CaliForge.

### 1. Dataset de Cenários de Teste (Harness Evaluation Cases)
O dataset de avaliação é estruturado com base nas seguintes personas e estados de usuário:

* **Caso de Teste 01 (Iniciante + Dor Aguda + Sem Equipamentos):**
  * *Entrada:* Nível iniciante em todos os eixos, dor no punho = 4, dor na lombar = 0, sem equipamentos.
  * *Expectativa:* NENHUM exercício que apoie peso sobre os punhos (ex: sem flexões). Substitutos como flexões na parede com punhos cerrados ou foco total em pernas/core e remada leve sob a mesa (se preferência de puxar).
* **Caso de Teste 02 (Intermediário + Equipamentos Completos + Alta Performance):**
  * *Entrada:* Nível push = 5, pull = 4, legs = 3, abs = 3, dores = 0, tem barra e paralelas.
  * *Expectativa:* Prescrever barra fixa (pronada/supinada), dips (paralelas) e exercícios de core mais avançados.
* **Caso de Teste 03 (Reabilitação Articular Múltipla + Sem Equipamentos):**
  * *Entrada:* Nível intermediário, dor no ombro = 2, dor na lombar = 1, sem equipamentos.
  * *Expectativa:* Exercícios de empurrar adaptados para menor impacto (ex: flexão inclinada elevada), inclusão explícita de exercícios educativos de mobilidade de ombro (reabilitação) e exclusão de prancha isométrica longa (tensão lombar).
* **Caso de Teste 04 (Baixa Consistência + Treino Regenerativo):**
  * *Entrada:* Nível intermediário, consistência semanal = 1 treino concluído de 4 planejados.
  * *Expectativa:* IA não deve progredir nível de exercícios. O treino deve ter volume reduzido (menos séries ou repetições) e foco em reestabelecimento e consistência.
* **Caso de Teste 05 (Avançado + Foco em Pernas):**
  * *Entrada:* Nível legs = 5, dor = 0, objetivo específico de priorizar pernas.
  * *Expectativa:* Prescrever pistol squats e variações intensas de pernas, mas com a salvaguarda de manter pelo menos 1 exercício de empurrar, puxar e core de manutenção.

### 2. Lógica de Asserção e Critérios de Aceitação (Assertions)
O Harness irá testar os JSONs gerados programaticamente usando as seguintes verificações lógicas:

```python
# Verificação de Segurança (Pain Lockout)
for exercise in workout.exercises:
    if user.painState.get("wrist", 0) >= 3 and exercise.category == "push":
        assert exercise.exerciseName not in ["flexao_tradicional", "dips"], "Falha: Exercício estressa articulação com dor aguda."

# Verificação de Equilíbrio Anatômico (Push/Pull Ratio)
push_count = sum(1 for e in workout.exercises if e.category == "push")
pull_count = sum(1 for e in workout.exercises if e.category == "pull")
if workout.focus == "fullbody":
    ratio = push_count / max(1, pull_count)
    assert 0.8 <= ratio <= 1.2, f"Falha: Treino fullbody desbalanceado (Push/Pull ratio: {ratio})"

# Verificação de Não-Progressão por Consistência
if user.weeklyConsistency.completedWorkoutsThisWeek < 2:
    for exercise in workout.exercises:
        previous_level = user.movementLevels[exercise.category]
        assert exercise.level <= previous_level, "Falha: Progrediu nível de exercício mesmo com baixa consistência semanal."
```

### 🚦 Checklist de Validação da Etapa 5
- [x] **Item 1:** Dataset de testes cobrindo todas as personas críticas e variações de equipamentos.
- [x] **Item 2:** Asserções de segurança articulares codificadas de forma binária.
- [x] **Item 3:** Validações de consistência e equilíbrio integradas ao harness de teste.

