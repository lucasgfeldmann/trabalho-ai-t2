# Registro de Melhorias do Spec Engine (improvements-framework)

Este arquivo atua como um mecanismo de **Auto-Learning (Aprendizado por Reforço)** para o refinamento contínuo do [lifecycle.md](file:///home/lucas/github/trabalho-ai-t2/specs/lifecycle.md). 

A lógica operacional funciona como um loop de feedback:
1. Durante a idealização e validação das especificações, a IA identifica de forma empírica as limitações, gargalos de contexto ou ambiguidades do processo.
2. Esses pontos são registrados aqui como feedbacks (recompensas/penalidades do loop).
3. Periodicamente, o usuário e a IA revisam este log para consolidar as melhorias no [lifecycle.md](file:///home/lucas/github/trabalho-ai-t2/specs/lifecycle.md), delimitando passos extremamente regrados, limites e papéis claros a serem desempenhados dentro do diretório `specs/`.

---

## 📈 Melhorias Mapeadas no Lifecycle

### 1. Refinamento de Etapas e Portões de Passagem (Lifecycle Phase Gates)
* **[IMP-001] Validação Automatizada de Checklist (Fase de Transição):**
  * *Descrição:* Estabelecer uma regra no lifecycle em que o avanço de uma etapa para a outra (ex: Etapa 2 para Etapa 3) exija a validação formal de um interpretador de regras antes de liberar o checklist, evitando que o agente tome a iniciativa de avançar etapas baseado em respostas vagas do usuário.
  * *Impacto:* Rigor metodológico estrito nas passagens de fase.
  * *Status:* 🟡 Em discussão.

### 2. Engenharia de Contexto nas Fases Iniciais (Lifecycle Context Management)
* **[IMP-002] Densidade de Informação e Limite de Casos de Borda (Etapas 1 e 2):**
  * *Descrição:* Definir um limite recomendado de "casos de borda" ativos mapeados por funcionalidade (ex: máximo de 3 a 5 mais críticos) para evitar que o rascunho inicial em `active_spec.md` acumule dados excessivos que estourem a janela de contexto de IAs subsequentes.
  * *Impacto:* Redução do consumo de tokens e foco nos problemas de maior valor.
  * *Status:* 🟡 Em discussão.

### 3. Protocolo de Coleta Conversacional de Dados (Onboarding Loop)
* **[IMP-003] Fluxo de Coleta Gradual de Atributos (Etapa 1/2):**
  * *Descrição:* Formalizar na estrutura da Etapa 1 o comportamento conversacional da IA para coletar preferências do usuário de forma fragmentada no diálogo diário (onboarding contínuo), em vez de exigir preenchimento de formulários inteiros. Definir como o checklist da Etapa 1 valida que o perfil foi "suficientemente mapeado" para permitir a geração de treinos.
  * *Impacto:* Melhora drástica na UX e simplificação do escopo inicial de domínio.
  * *Status:* 🟡 Em discussão.

### 4. Flexibilidade de Contratos Dinâmicos (Etapa 4/5 - Contratos de Dados)
* **[IMP-004] Esquemas de Preferências Mutáveis no Domínio:**
  * *Descrição:* Ajustar o modelo de dados da Etapa 4 para que os contratos JSON Schema suportem "preferências dinâmicas/temporárias" (como histórico de dor ativa do usuário que expira após X dias), garantindo que o domínio do algoritmo reflita a natureza adaptativa da fisiologia humana no lifecycle.
  * *Impacto:* Adaptação do contrato de dados à reabilitação e consistência do usuário.
  * *Status:* 🟡 Em discussão.

---

## ⚙️ Instruções Locais para o Agente de Specs
Sempre que você estiver refinando as especificações ou o ciclo de vida neste diretório `specs/`:
1. **Consulte este arquivo** para verificar se há alguma melhoria pendente que afete o domínio que você está modelando.
2. **Registre novos pontos de melhoria estrutural** no lifecycle seguindo o padrão de identificação `[IMP-XXX]`.
3. **Mantenha o foco puramente na modelagem do processo de especificação** e do ciclo de vida, evitando anotações sobre código de produção ou infraestruturas globais do repositório.
