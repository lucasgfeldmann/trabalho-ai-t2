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

### 📂 Geração de Documentos de Entrega Pós-Lifecycle
* **[x] [TSK-008] Regras de Portão no Lifecycle e README:**
  * *Descrição:* Adicionar no README.md e lifecycle.md a regra de liberação de arquivos pós-lifecycle. Definir como local de saída o diretório `specs/output/`.
  * *Status:* 🟢 Concluído

* **[x] [TSK-009] Definição dos Modelos/Templates dos 3 Arquivos:**
  * *Descrição:* Desenhar os templates de estrutura para os arquivos projeto.md, requisitos.md e criterios-aceite.md.
  * *Status:* 🟢 Concluído

* **[x] [TSK-010] Geração e Preenchimento dos Entregáveis do CaliForge:**
  * *Descrição:* Criar e popular specs/output/projeto.md, specs/output/requisitos.md e specs/output/criterios-aceite.md para o CaliForge.
  * *Status:* 🟢 Concluído

### 🧪 Desenvolvimento do Harness de Testes (Harness Engineering)
* **[x] [TSK-011] Criação do diretório de testes e arquitetura do Harness:**
  * *Descrição:* Criar a pasta `tests/` na raiz do projeto e estruturar a arquitetura do executor de testes (como os arquivos serão organizados e executados).
  * *Status:* 🟢 Concluído

* **[x] [TSK-012] Implementação do Dataset e Validação de Schemas:**
  * *Descrição:* Criar o dataset JSON (`tests/dataset.json`) contendo os 5 perfis de teste e implementar a validação dos JSON Schemas de entrada e saída.
  * *Status:* 🟢 Concluído

* **[x] [TSK-013] Implementação do Script do Harness (test_harness.py):**
  * *Descrição:* Desenvolver o script de teste (`tests/test_harness.py`) contendo a lógica de validação automatizada e as asserções de qualidade do CaliForge (CA-001 a CA-004).
  * *Status:* 🟢 Concluído

### 💻 Desenvolvimento da Aplicação (CaliForge Core em `/src/`)
* **[x] [TSK-014] Estrutura Inicial e Contratos do `/src/`:**
  * *Descrição:* Configurar o diretório `/src/` com as classes de domínio e mapeamento de tipos básicos baseados nos JSON Schemas.
  * *Status:* 🟢 Concluído

* **[x] [TSK-015] Implementação do Algoritmo de Geração e Reabilitação:**
  * *Descrição:* Desenvolver a lógica real de geração de treinos, regras de sobrecarga progressiva, temporalidade de dores e pain lockout em `/src/`.
  * *Status:* 🟢 Concluído

* **[x] [TSK-016] Acoplamento do Harness ao Código de Produção:**
  * *Descrição:* Substituir o mock do gerador no `tests/test_harness.py` pela chamada das funções reais do `/src/`, validando o produto final contra as asserções.
  * *Status:* 🟢 Concluído

### 🐳 Infraestrutura de Conteinerização (Docker)
* **[x] [TSK-017] Configuração do Docker da Aplicação e Harness:**
  * *Descrição:* Criar o `Dockerfile` e arquivos de apoio do Docker para executar o CaliForge e rodar a suite de testes de forma isolada em containers.
  * *Status:* 🟢 Concluído

---

## 📜 Histórico de Tarefas Concluídas

* **[TSK-001] Discussão do IMP-001 (Validação de checklists):**
  * *Decisão:* Consolidada a regra de portão de validação no `lifecycle.md` exigindo consentimento verbal do usuário, checklist questions tracker zerado e registro em `context.jsonl` antes que qualquer IA possa alterar caixas de checklists.*

* **[TSK-002] Discussão do IMP-002 (Densidade de Casos de Borda):**
  * *Decisão:* Adicionado o Protocolo de Gestão de Densidade de Contexto no `lifecycle.md`. Ele estabelece a triagem ativa de ideias secundárias (armazenadas em `specs/future-specs.md`) e a modularização de subsistemas extensos em arquivos satélites (`specs/modules/`) para manter o arquivo de especificação ativo com no máximo 3 casos de borda por arquivo, contendo token bloat.

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

* **[TSK-008] Regras de Portão no Lifecycle e README:**
  * *Decisão:* Adicionada a regra de portão em `specs/README.md` e a seção "Entregáveis Finais de Engenharia" em `specs/lifecycle.md`, proibindo a geração de `projeto.md`, `requisitos.md` e `criterios-aceite.md` antes da aprovação final (Etapa 5) e definindo a subpasta `specs/output/` como destino oficial.

* **[TSK-009] Definição dos Modelos/Templates dos 3 Arquivos:**
  * *Decisão:* Aprovados e desenhados os templates em Markdown estruturado para `projeto.md` (visão, problema, metas e escopo), `requisitos.md` (RFs e RNFs detalhados) e `criterios-aceite.md` (casos de teste em JSON e asserções binárias do Harness).

* **[TSK-010] Geração e Preenchimento dos Entregáveis do CaliForge:**
  * *Decisão:* Criados e preenchidos os arquivos de entrega pós-lifecycle para o CaliForge sob o diretório `specs/output/`: `projeto.md` (Visão geral, objetivos, restrições e personas), `requisitos.md` (Requisitos funcionais, regras de negócio e não-funcionais) e `criterios-aceite.md` (Dataset de teste de 5 cenários com JSON e as 5 asserções lógicas para o Harness).

* **[TSK-011] Criação do diretório de testes e arquitetura do Harness:**
  * *Decisão:* Criado o diretório `tests/` na raiz e adotada a arquitetura modular e desacoplada (Opção 1): schemas separados em subpasta, dados no formato JSON (`tests/dataset.json`) e lógica de testes encapsulada in `tests/test_harness.py`.

* **[TSK-012] Implementação do Dataset e Validação de Schemas:**
  * *Decisão:* Criados e validados os arquivos JSON Schemas (`tests/schemas/CaliForgeUserInput.json` e `tests/schemas/CaliForgeWorkoutOutput.json`) e o dataset com os 5 casos de teste completos no arquivo `tests/dataset.json`.

* **[TSK-013] Implementação do Script do Harness (test_harness.py):**
  * *Decisão:* Desenvolvido o script `tests/test_harness.py` contendo a validação de JSON Schemas (com fallback resiliente sem bibliotecas externas) e a checagem das 4 asserções de segurança/consistência. Testes executados com sucesso e obtido status final 5/5 Verde ("TUDO VERDE").

* **[TSK-017] Configuração do Docker da Aplicação e Harness:**
  * *Decisão:* Criada a infraestrutura Docker (`Dockerfile`, `.dockerignore`, `requirements.txt`). Imagem `califorge-harness` compilada e executada com sucesso. A validação estrita via `jsonschema` (instalada via Docker) rodou com sucesso na avaliação dos 5 casos (5/5 verde), homologando a portabilidade do Harness.

* **[TSK-014] Estrutura Inicial e Contratos do `/src/`:**
  * *Decisão:* Criado o pacote `src/` com `__init__.py` e `src/models.py`. Implementadas classes com `dataclasses` para modelar os inputs e outputs do CaliForge, incluindo métodos estáticos `from_dict` que aplicam os fallbacks seguros descritos na Etapa 4 da especificação em caso de dados de entrada incompletos.

* **[TSK-015] Implementação do Algoritmo de Geração e Reabilitação:**
  * *Decisão:* Criado o arquivo `src/generator.py` contendo a função `generate_workout`. Ela faz o parsing da entrada com os fallbacks, resolve o foco muscular (reabilitando se dor no punho >= 3), aplica restrições de progressão de nível baseadas em consistência (< 2 treinos), garante que o volume de sustentação de empurrar/puxar no fullbody seja equilibrado e filtra equipamentos.

* **[TSK-016] Acoplamento do Harness ao Código de Produção:**
  * *Decisão:* Modificado o script de testes `tests/test_harness.py` para injetar o caminho do diretório raiz no `sys.path` e importar a função real `generate_workout` de `src.generator`. Executados os testes via Docker que resultaram em homologação total (5/5 verde), atestando a integridade física e sintática do motor de prescrições.












