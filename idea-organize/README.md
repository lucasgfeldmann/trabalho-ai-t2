# Protocolo de Especificação Onipresente (Spec Engine Protocol)

Este repositório atua como um **Framework de Especificação (Spec Engine)**. O seu objetivo principal é estruturar o processo e o ciclo de vida pelos quais qualquer ideia de produto ou melhoria técnica deve passar antes de ser codificada em projetos futuros.

O diretório `idea-organize/` serve exclusivamente para a modelagem desse framework e documentação de especificações exemplares (como o **CaliForge** em `active_spec.md`). Portanto, **nenhum código de produção será gerado neste repositório**. No futuro, este framework servirá como uma Skill Customizada (`new-idea`) que impedirá os agentes de IA de iniciar qualquer desenvolvimento ou alteração em qualquer projeto sem que haja uma especificação formal previamente aprovada pelo usuário.

---

## 🎯 O que é uma "Boa Especificação"? (Critérios de Qualidade)

Para que uma especificação seja considerada pronta para desenvolvimento, ela deve obrigatoriamente cumprir três pilares:

1. **Testabilidade (Falsificabilidade):** Todo requisito deve ter um critério de aceitação binário (Passa / Não Passa) que possa ser verificado por um script ou pelo usuário de forma inequívoca.
2. **Mapeamento de Casos de Borda (Edge Cases):** A especificação deve descrever o comportamento esperado em cenários de falha, dados inválidos ou comportamentos inesperados do usuário.
3. **Segurança e Restrições (Safety First):** Devem estar explícitas as barreiras de proteção do sistema (ex: na Calistenia, não prescrever exercícios perigosos para quem tem lesões).

---

## 🔁 O Loop de Validação de Especificações

Quando uma ideia nasce, ela passa por um ciclo de vida assistido de especificação da ideia:

```mermaid
graph TD
    A[Usuário: Envia Ideia/Rascunho] --> B[IA: Mapeia Objetivo e Escopo]
    B --> C[IA: Detalha Requisitos do Projeto/Sistema]
    C --> D[IA + Usuário: Estabelece Critérios de Aceitação]
    D --> E[Aprovação e Fim do Ciclo de Especificação]
```

---

## ⚙️ Regras de Execução da IA (Onipresença)

Sempre que uma nova funcionalidade for discutida, a IA deve guiar o processo seguindo estas diretrizes:

* **Código de Produção Zero (Rigor Estrito):** Nenhum código-fonte da aplicação (backend ou frontend) ou interfaces operáveis serão gerados pelas IAs até que todas as etapas de especificação (Etapas 1 a 3) estejam integralmente concluídas, validadas e aprovadas pelo usuário.
* **Não pular etapas:** Nunca comece a propoer implementações ou telas de produção antes que a especificação atinja a aprovação completa.
* **Desafio Ativo:** A IA deve atuar como um validador crítico, propondo pelo menos 2 cenários de falha ou "casos de borda" para cada novo requisito proposto pelo usuário.
* **Registro de Melhorias (Improvements Tracker):** Qualquer ponto de melhoria ou refinamento estrutural no ciclo de vida (lifecycle) deve ser documentado no arquivo [improvements-framework.md](file:///home/lucas/github/trabalho-ai-t2/idea-organize/improvements-framework.md) neste diretório de idea-organize, servindo como instrução local focada em refinar a estrutura do framework. **Este registro de melhorias deve conter apenas aprimoramentos do meta-processo, sendo estritamente proibida a inclusão de regras de negócio de produtos ativos.**
* **Tracker de Perguntas (Questions Tracker):** Toda e qualquer pergunta feita ao usuário durante o ciclo de vida deve ser registrada no arquivo [questions.md](file:///home/lucas/github/trabalho-ai-t2/idea-organize/questions.md). Nenhuma etapa do checklist pode ser concluída e nenhuma dedução/afirmação pode ser assumida até que todas as respectivas perguntas ativas no tracker sejam respondidas pelo usuário.

