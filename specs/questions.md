# Tracker de Perguntas do Spec Engine (questions.md)

Este arquivo serve para rastrear e gerenciar **toda e qualquer pergunta** feita ao usuário durante o processo de idealização e refinamento das especificações. 

### ⚙️ Regras do Tracker:
1. **Registro Obrigatório:** Toda pergunta formulada para obter direcionamento do usuário deve ser listada aqui com um identificador `[Q-XXX]` e checkbox `[ ]`.
2. **Proibição de Deduções:** A IA não pode marcar checklists de etapas como concluídos, nem deduzir/afirmar respostas caso o usuário não tenha respondido explicitamente à pergunta correspondente no chat.
3. **Casos de Uso:** O avanço das etapas no `lifecycle.md` está estritamente bloqueado pelas perguntas pendentes daquela etapa.

---

## 🚦 Perguntas Ativas

*Nenhuma pergunta ativa no momento. Todas as etapas do ciclo de especificação foram validadas pelo usuário!*

---

## 📜 Histórico de Perguntas Respondidas

* **[Q-009] Estratégia de Cobertura de Cenários no Dataset do Harness:**
  * *Pergunta:* O dataset do Harness deve cobrir quais cenários específicos de usuários? Proponho testar 5 perfis básicos em active_spec.md: (1) Iniciante sem equipamentos com dor aguda no punho (nível 4); (2) Intermediário focado em Push/Pull com barra e paralelas; (3) Reabilitação de ombro (nível 2) e lombar (nível 1); (4) Usuário com consistência semanal baixa (volume reduzido); (5) Avançado com foco em pernas (pistol squat). Está de acordo com essa cobertura?
  * *Resposta/Decisão:* Aprovado pelo usuário para cobrir os 5 cenários propostos no dataset de testes do Harness.
  * *Status:* `[x] Respondida`

* **[Q-010] Critérios de Aceitação Binários (Asserções de Teste do Harness):**
  * *Pergunta:* Concorda com as seguintes regras de validação programática (Passa/Não Passa)? (1) Dor articular > 2 bloqueia exercícios agressores; (2) Proporção Push vs. Pull em treinos Fullbody entre 0.8 e 1.2; (3) Baixa consistência semanal impede propostas de progressão de nível. Está aprovado?
  * *Resposta/Decisão:* Aprovado pelo usuário para as 3 regras de asserção lógica binárias do Harness de teste.
  * *Status:* `[x] Respondida`

* **[Q-007] Formato do Mapeamento de Dores Articulares no Schema de Entrada:**
  * *Pergunta:* Para as restrições articulares no JSON Schema de entrada, prefere um formato simples contendo apenas a lista de articulações afetadas (ex: `["wrist", "shoulder"]`) ou um mapeamento estruturado com nível de intensidade/dor de 1 a 5 (ex: `{"wrist": 3, "shoulder": 1}`)?
  * *Resposta/Decisão:* O usuário escolheu a Opção 2 (Mapeamento com Intensidade de 1 a 5) por ser mais rico para aplicar regras de reabilitação.
  * *Status:* `[x] Respondida`

* **[Q-008] Variações e Alternativas no Schema de Treino (Saída):**
  * *Pergunta:* A estrutura de treino gerada pela IA (saída) deve conter alternativas pré-computadas para cada exercício (ex: caso um equipamento esteja ocupado ou o usuário prefira mudar na hora do treino) ou prefere que a saída seja linear e qualquer troca seja processada dinamicamente via chat?
  * *Resposta/Decisão:* O usuário prefere que a estrutura de saída do treino seja linear, e que qualquer alteração seja negociada e ajustada de forma dinâmica através do chat.
  * *Status:* `[x] Respondida`

* **[Q-001] Regras de Sobrecarga Progressiva e Adaptação:**
  * *Pergunta:* A lógica adaptativa proposta para o algoritmo (Evoluir de exercício se fizer o topo da faixa de repetições nas 3 séries; Regredir de exercício por segurança se ficar abaixo do limiar de 5 repetições em alguma série devido à fadiga) está aprovada por você?
  * *Resposta/Decisão:* Rejeitada parcialmente. O usuário direcionou que a evolução do treino deve exigir consolidação ao longo do tempo (evitando saltos por picos de performance diários) e o algoritmo deve analisar a frequência semanal e dar foco em repouso e recuperação física, sem forçar alta performance diária constante.
  * *Status:* `[x] Respondida` (Mapeado em active_spec.md e gerada pergunta Q-005).

* **[Q-005] Lógica de Consolidação e Recuperação Adaptativa:**
  * *Pergunta:* A nova lógica contendo consolidação de meta (manter o desempenho máximo por 3 treinos consecutivos antes de avançar) e análise de frequência semanal (recomendações de descanso e controle de volume regulados pela consistência semanal) está aprovada?
  * *Resposta/Decisão:* Rejeitada pelo usuário. Ele indicou que o aplicativo deve focar no engajamento e adesão a longo prazo, evitando "números mágicos" estáticos como contadores de 3 treinos consecutivos. A evolução deve ser adaptável baseada na análise de padrões do usuário e no feedback de sentimento (como ele se sente no treino) de forma personalizada e de acordo com seus desejos.
  * *Status:* `[x] Respondida` (Mapeado em active_spec.md e gerada pergunta Q-006).

* **[Q-006] Evolução Colaborativa Sem Números Mágicos:**
  * *Pergunta:* A nova proposta onde a progressão e evolução de carga são baseadas na análise geral de consistência e sugeridas dialogicamente pela IA (negociando com o sentimento, energia e desejo de avanço do usuário no check-in diário, em vez de aplicar um número fixo automático de 3 dias/treinos) está aprovada?
  * *Resposta/Decisão:* Aprovada pelo usuário. A progressão ocorre por meio da análise geral de padrões de consistência, sentimentos, energia e adesão ao longo do tempo, em vez de limites mecânicos fixos.
  * *Status:* `[x] Respondida`

* **[Q-002] Layout Dinâmico e Transição do Dashboard Híbrido (T1):**
  * *Pergunta:* O fluxo híbrido em que a tela principal mostra o dashboard de treino do dia quando ociosa, e desliza de forma fluida para o chat quando o usuário interage, está de acordo com a sua visão de simplicidade?
  * *Resposta/Decisão:* Aprovado pelo usuário no fluxo híbrido.
  * *Status:* `[x] Respondida`

* **[Q-003] Sincronização Automática por Diálogo (Chat Sync - T2):**
  * *Pergunta:* Está aprovado o recurso onde a IA escuta relatos coloquiais no chat (ex: *"fiz 3x10 flexões diamante"*) e marca automaticamente os inputs de séries/repetições na UI do plano de treino?
  * *Resposta/Decisão:* Aprovado pelo usuário o preenchimento automático.
  * *Status:* `[x] Respondida`

* **[Q-004] Design System e Paleta HSL:**
  * *Pergunta:* Concorda com a proposta de visual minimalista escuro (Sleek Dark Mode) utilizando tons cinzas-chumbo HSL e cores discretas para status (verde para concluído, amarelo para reabilitação, coral para dor ativa)?
  * *Resposta/Decisão:* Aprovado pelo usuário para a paleta HSL e o dark mode.
  * *Status:* `[x] Respondida`
