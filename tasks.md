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
  * *Status:* `🟢 Concluído`

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


