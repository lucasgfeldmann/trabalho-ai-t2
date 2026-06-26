# Rastreador de Tarefas do Projeto (tasks.md)

Este arquivo é um mecanismo de governança de processo global da workspace. Ele serve para dividir tópicos amplos ou debates multifatoriais em pequenos blocos de tarefas (micro-atividades) para iterarmos sequencialmente, garantindo assertividade e evitando que a IA se perca ou ignore tópicos.

---

## ⚙️ Regras do Rastreador de Tarefas:
1. **Regra de Divisão Atômica:** Qualquer debate amplo, complexo ou com múltiplas perguntas em aberto deve obrigatoriamente ser quebrado em micro-tarefas neste arquivo com o formato `[TSK-XXX]`.
2. **Iteração Sequencial:** A IA e o usuário devem focar em resolver **uma única tarefa ativa por vez**. As demais permanecem listadas de forma inerte.
3. **Registro de Conclusões:** Ao finalizar um bloco, a IA deve marcar a tarefa correspondente como concluída (`[x]`) e registrar a decisão extraída no histórico de conclusões.

---

## 🚦 Quadro de Tarefas Ativas

### 📈 Debate do improvements-framework.md (Melhorias no Ciclo de Vida)
* **[x] [TSK-001] Discussão do IMP-001 (Validação de checklists):**
  * *Descrição:* Debater e decidir sobre a incorporação da regra de transição de fase rígida no `lifecycle.md` com base na conformidade do questions tracker.
  * *Status:* `🟢 Concluído`

* **[x] [TSK-002] Discussão do IMP-002 (Densidade de Casos de Borda):**
  * *Descrição:* Debater e decidir sobre limitar o mapeamento a no máximo 3 casos de borda de segurança ativos nas especificações para otimizar tokens.
  * *Status:* `🟢 Concluído`

* **[x] [TSK-003] Discussão do IMP-003 (UX de Onboarding Gradual):**
  * *Descrição:* Debater e decidir sobre a diretriz de coleta de atributos de forma conversacional e fragmentada no primeiro onboarding.
  * *Status:* `🟢 Concluído`

* **[x] [TSK-004] Discussão do IMP-004 (Contratos de Dados Dinâmicos):**
  * *Descrição:* Debater e decidir sobre a exigência de histórico temporal e metadados de dor nos schemas de entrada/saída para reabilitação articular.
  * *Status:* 🟢 Concluído

### 🔍 Revisão e Ajuste do active_spec.md (CaliForge)
* **[x] [TSK-005] Ajuste da Etapa 1 (Massa Crítica de Dados):**
  * *Descrição:* Definir formalmente a Massa Crítica de Dados obrigatória na Etapa 1 para o onboarding conversacional do CaliForge e atualizar o checklist.
  * *Status:* 🟢 Concluído

* **[x] [TSK-006] Ajuste da Etapa 4 (Fallbacks de Dados Incompletos):**
  * *Descrição:* Documentar os valores padrões seguros (fallbacks) e ajustar os esquemas JSON de entrada/saída na Etapa 4 para aceitar dados parciais.
  * *Status:* 🟢 Concluído

* **[x] [TSK-007] Ajuste da Etapa 4 (Ciclo de Vida de Dados Temporais):**
  * *Descrição:* Mapear a validade temporal (TTL) e regras de decaimento de dores no esquema e contratos da Etapa 4.
  * *Status:* 🟢 Concluído

### 📐 Correção Metodológica do Ciclo de Vida (Generalização do lifecycle.md)
* **[x] [TSK-008] Generalização do lifecycle.md (Remoção de Poluição de Negócio):**
  * *Descrição:* Remover todas as referências diretas de entrada de dados específicos do CaliForge e termos específicos de calistenia dos checklists e objetivos das etapas no lifecycle.md, tornando-o um meta-framework puramente conceitual.
  * *Status:* 🟢 Concluído

* **[x] [TSK-009] Remoção da Etapa 4 Técnica (Exclusão de JSON Schemas):**
  * *Descrição:* Remover a Etapa 4 de Contratos Técnicos (JSON Schemas) do ciclo de vida, integrando os requisitos de dados mínimos obrigatórios na Etapa 1 e a validade de dados temporais e fallbacks na Etapa 2 de domínio.
  * *Status:* 🟢 Concluído

* **[x] [TSK-010] Simplificação da Etapa 1 (Focar apenas em Objetivos e Escopo de Produto):**
  * *Descrição:* Remover a menção e a obrigatoriedade da 'Massa Crítica de Dados' da Etapa 1 do lifecycle.md e active_spec.md, focando a primeira etapa puramente na visão geral, personas e escopo de funcionalidades.
  * *Status:* 🟢 Concluído

* **[x] [TSK-011] Remoção da Etapa 4 de Harness (Validação e Testes Técnicos):**
  * *Descrição:* Remover por completo a Etapa 4 de Critérios de Avaliação e Dataset do Harness dos arquivos lifecycle.md, README.md e active_spec.md, deixando o Spec Engine composto por 3 etapas puramente funcionais de ideação de produto (Escopo, Domínio e UI/UX).
  * *Status:* 🟢 Concluído

* **[x] [TSK-012] Redesenho Metodológico do Ciclo de Vida (Novas 3 Etapas):**
  * *Descrição:* Redefinir as etapas do lifecycle.md, README.md e active_spec.md para: Etapa 1. Objetivo e Escopo, Etapa 2. Requisitos do Sistema, e Etapa 3. Critérios de Aceitação.
  * *Status:* 🟢 Concluído

* **[x] [TSK-013] Auditoria Completa do Diretório idea-organize/:**
  * *Descrição:* Revisar todos os arquivos da pasta idea-organize/ (active_spec.md, future-specs.md, improvements-framework.md, lifecycle.md, questions.md) para garantir que estão focados puramente na montagem e estruturação do projeto em nível de ideia/conceito e não de desenvolvimento técnico de software.
  * *Status:* 🟢 Concluído

* **[x] [TSK-014] Renomeação do Diretório specs para idea-organize:**
  * *Descrição:* Renomear fisicamente a pasta specs/ para idea-organize/ e substituir de forma abrangente todas as referências textuais e links markdown a "specs/" por "idea-organize/" em todos os arquivos da workspace.
  * *Status:* 🟢 Concluído

* **[x] [TSK-015] Renomeação da Skill new-spec para new-idea:**
  * *Descrição:* Renomear fisicamente a pasta de skills .agents/skills/new-spec/ para .agents/skills/new-idea/, atualizar o name YAML no SKILL.md e substituir todas as referências a "new-spec" na workspace por "new-idea".
  * *Status:* 🟢 Concluído

---

## 📜 Histórico de Tarefas Concluídas

* **[TSK-001] Discussão do IMP-001 (Validação de checklists):**
  * *Decisão:* Consolidada a regra de portão de validação no `lifecycle.md` exigindo consentimento verbal do usuário, checklist questions tracker zerado e registro em `context.jsonl` antes que qualquer IA possa alterar caixas de checklists.*

* **[TSK-002] Discussão do IMP-002 (Densidade de Casos de Borda):**
  * *Decisão:* Adicionado o Protocolo de Gestão de Densidade de Contexto no `lifecycle.md`. Ele estabelece a triagem ativa de ideias secundárias (armazenadas em `idea-organize/future-specs.md`) e a modularização de subsistemas extensos em arquivos satélites (`idea-organize/modules/`) para manter o arquivo de especificação ativo com no máximo 3 casos de borda por arquivo, contendo token bloat.

* **[TSK-003] Discussão do IMP-003 (UX de Onboarding Gradual):**
  * *Decisão:* Adicionada a exigência metodológica no `lifecycle.md` para especificações de produtos dinâmicos/incrementais. Exige-se a definição formal da Massa Crítica de Dados (Etapa 1) e o mapeamento dos Fallbacks de Segurança (valores padrão) para todos os dados opcionais/vazios nos esquemas (Etapa 4), blindando a integração de dados e a IA.

* **[TSK-004] Discussão do IMP-004 (Contratos de Dados Dinâmicos):**
  * *Decisão:* Incluída a regra obrigatória na Etapa 4 de `lifecycle.md` exigindo a modelagem do Ciclo de Vida do Dado para quaisquer parâmetros de dados temporais ou dinamicamente mutáveis, definindo janelas de validade (TTL) e regras de decaimento/exclusão.

* **[TSK-005] Ajuste da Etapa 1 (Massa Crítica de Dados):**
  * *Decisão:* Adicionada a definição formal de Massa Crítica de Dados (Identificação, Biometria, Equipamentos, Saúde/Dores/Mobilidade e Nível Físico por Teste Prático Guiado) na Etapa 1 de `active_spec.md`, alinhada com as exigências de onboarding conversacional gradual.

* **[TSK-006] Ajuste da Etapa 4 (Fallbacks de Dados Incompletos):**
  * *Decisão:* Ajustado o JSON Schema de entrada (`CaliForgeUserInput`) em `active_spec.md` para exigir apenas a biometria/saúde obrigatória e adicionada uma tabela detalhada com valores padrão seguros (fallbacks) para todos os dados opcionais ausentes no onboarding.

* **[TSK-007] Ajuste da Etapa 4 (Ciclo de Vida de Dados Temporais):**
  * *Decisão:* Adicionado o detalhamento do Ciclo de Vida e Decaimento de Dores Articulares na Etapa 4 de `active_spec.md`. Ele estabelece validade padrão de 7 dias (TTL), decaimento de 1 nível de dor a cada 7 dias de inatividade de relatos e gatilho de reavaliação no chat a cada 3 sessões de treino concluídas.

* **[TSK-008] Generalização do lifecycle.md (Remoção de Poluição de Negócio):**
  * *Decisão:* Removidas todas as menções diretas a calistenia, exercícios, equipamentos e termos específicos do CaliForge das etapas do lifecycle.md. O ciclo de vida agora é agnóstico, descrevendo de forma abstrata personas, restrições gerais de domínio, modelo de dados estruturado (entradas/saídas), massa crítica de dados, fallbacks, dados temporais e dataset de asserções do Harness.

* **[TSK-009] Remoção da Etapa 4 Técnica (Exclusão de JSON Schemas):**
  * *Decisão:* Removida completamente a Etapa 4 técnica de Contratos e Esquemas JSON de Entrada/Saída do `lifecycle.md` e do `README.md` das especificações. O ciclo de vida agora foi simplificado para 4 etapas principais, integrando a "Massa Crítica de Dados" na Etapa 1 (Escopo) e as diretrizes de "Valores Padrão (Fallbacks)" e "Regras de Dados Temporais (TTL/Decaimento)" na Etapa 2 (Modelo de Domínio). Na especificação ativa `active_spec.md` do CaliForge, os JSON Schemas técnicos foram removidos e as seções de fallbacks e regras temporais de dores foram movidas e fundidas com a Etapa 2 de domínio.

* **[TSK-010] Simplificação da Etapa 1 (Focar apenas em Objetivos e Escopo de Produto):**
  * *Decisão:* Removida a exigência de especificar a 'Massa Crítica de Dados' e fluxos de dados de entrada mínimos da Etapa 1 de `lifecycle.md` e `active_spec.md`. O objetivo da Etapa 1 foi redefinido para focar puramente em alinhar e documentar a visão do produto, público-alvo, personas e escopo de recursos chave (funcionalidades), eliminando barreiras técnicas e de modelagem de dados precoce na ideação inicial.

* **[TSK-011] Remoção da Etapa 4 de Harness (Validação e Testes Técnicos):**
  * *Decisão:* Removidos completamente todos os requisitos e a etapa de Harness (Critérios de Avaliação e Dataset de Testes) do `lifecycle.md`, `README.md` e `active_spec.md`. O ciclo de vida do Spec Engine agora é puramente conceitual e focado na ideação de ideias em 3 etapas consecutivas: 1. Visão Geral e Escopo (Objetivos, Personas e Recursos), 2. Modelo de Domínio e Regras de Negócio (Entidades, Estados e Temporalidade Funcional de Dados) e 3. UI/UX e Design System (Navegação, Tokens HSL e Animações), eliminando qualquer acoplamento técnico de testes programáticos do repositório.

* **[TSK-012] Redesenho Metodológico do Ciclo de Vida (Novas 3 Etapas):**
  * *Decisão:* Reformuladas e consolidadas as 3 etapas de idealização do Spec Engine no `lifecycle.md` e `README.md` para focar em engenharia de requisitos: 1. Objetivo e Escopo do Projeto (Goal & Scope), 2. Requisitos do Projeto / Sistema a ser Desenvolvido (System Requirements) e 3. Critérios de Aceitação (Acceptance Criteria). Na especificação ativa `active_spec.md` do CaliForge, as antigas seções de domínio, fallbacks, TTL e UI/UX foram estruturadas como requisitos do sistema (Etapa 2), e as asserções de testes lógicas do Harness foram convertidas em critérios de aceitação binários (Etapa 3), eliminando acoplamento técnico anterior e simplificando o repositório.

* **[TSK-013] Auditoria Completa do Diretório idea-organize/:**
  * *Decisão:* Auditados e ajustados cirurgicamente todos os arquivos do diretório idea-organize/ (lifecycle.md, active_spec.md, improvements-framework.md, questions.md). Removemos quaisquer termos e referências residuais a fases de desenvolvimento técnico, tais como JSON Schemas, contratos de dados, datasets e Harness de testes. Os documentos agora estão 100% focados na montagem, estruturação e idealização de conceitos funcionais em 3 etapas de Requisitos de Engenharia.

* **[TSK-014] Renomeação do Diretório specs para idea-organize:**
  * *Decisão:* Renomeado fisicamente o diretório de especificações specs/ para idea-organize/, e atualizadas com sucesso todas as referências em README.md, AGENTS.md, SKILL.md, e nos arquivos internos de processos (lifecycle.md, improvements-framework.md, etc.) para refletir a nova nomenclatura voltada a organização de ideias.

* **[TSK-015] Renomeação da Skill new-spec para new-idea:**
  * *Decisão:* Renomeada fisicamente a pasta da skill customizada para `.agents/skills/new-idea`, alterado o nome para `new-idea` no frontmatter YAML do `SKILL.md` e atualizadas com sucesso todas as referências residuais no `README.md` do diretório `idea-organize/` para manter a consistência do ecossistema.





