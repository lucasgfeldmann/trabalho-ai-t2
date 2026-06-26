# CaliForge - Assistente Inteligente de Calistenia

Este repositório contém o projeto de Inteligência Artificial da G2 para a disciplina de IA 2. O objetivo é desenvolver um assistente inteligente focado na prática de calistenia, utilizando as metodologias de **Spec-Driven Development (SDD)** e **Harness Engineering**.

---

## 📂 Estrutura do Projeto

* [prompts.jsonl](file:///home/lucas/github/trabalho-ai-t2/prompts.jsonl): Banco de dados em formato JSON Lines que registra todos os prompts enviados pelo usuário com metadados detalhados para auditoria e replicação.
* [context.jsonl](file:///home/lucas/github/trabalho-ai-t2/context.jsonl): Histórico estruturado de passos, decisões tomadas e estado atual do projeto para alinhamento rápido de contexto entre chats.
* [.agents/AGENTS.md](file:///home/lucas/github/trabalho-ai-t2/.agents/AGENTS.md): Regras de contexto para o agente de IA neste workspace.
* [idea-organize/](file:///home/lucas/github/trabalho-ai-t2/idea-organize/):
  * [README.md](file:///home/lucas/github/trabalho-ai-t2/idea-organize/README.md): Protocolo de especificação onipresente que define critérios de qualidade e o fluxo inicial.
  * [lifecycle.md](file:///home/lucas/github/trabalho-ai-t2/idea-organize/lifecycle.md): Definição das etapas de desenvolvimento da especificação e fluxo de validação em loop.
  * [active_spec.md](file:///home/lucas/github/trabalho-ai-t2/idea-organize/active_spec.md): Especificação ativa em desenvolvimento (Etapa 3 Concluída pelo Usuário).

---

## 🚀 Como Iterar no Projeto

1. **Alinhamento de Contexto:** A IA lê [context.jsonl](file:///home/lucas/github/trabalho-ai-t2/context.jsonl) e [.agents/AGENTS.md](file:///home/lucas/github/trabalho-ai-t2/.agents/AGENTS.md) para sincronizar o progresso.
2. **Seguir o Protocolo:** Toda ideia nova deve seguir os pilares definidos no [README.md das especificações](file:///home/lucas/github/trabalho-ai-t2/idea-organize/README.md).
3. **Rever a Especificação Ativa:** Acesse [active_spec.md](file:///home/lucas/github/trabalho-ai-t2/idea-organize/active_spec.md) para analisar o status atual e os checklists.
4. **Ciclo de Validação:** Discuta refinamentos com a IA. Quando uma etapa estiver 100% acordada, atualizamos o checklist e avançamos para a próxima etapa em [lifecycle.md](file:///home/lucas/github/trabalho-ai-t2/idea-organize/lifecycle.md).
5. **Evolução Contínua:** Proponha melhorias ao ciclo de vida no arquivo de melhorias local e registre novos direcionamentos para futuras especificações.
