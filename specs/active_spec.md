# Especificação Ativa: CaliForge

Este arquivo contém a especificação de produto e técnica do CaliForge, desenvolvida iterativamente de acordo com o nosso Ciclo de Vida de Especificação.

* **Status Atual:** 🟢 Etapa 1: Visão Geral e Escopo (Rascunho Inicial)
* **Última Atualização:** 2026-06-23

---

## 🏁 Etapa 1: Visão Geral e Escopo

### 1. Público-Alvo e Personas
A solução atende a dois perfis principais de praticantes de calistenia:
* **Persona A: O Iniciante (Pedro, 24 anos)**
  * **Objetivo:** Começar a treinar usando apenas o peso do corpo, ganhar força básica.
  * **Dificuldade:** Não sabe quais exercícios fazer, não consegue fazer 1 pull-up ainda, treina em casa sem equipamentos (apenas no chão ou usando cadeiras).
  * **Necessidade:** Treinos muito simples, focados em exercícios educativos (flexão de joelho, barra australiana/remada sob a mesa, agachamento livre) e instruções claras de forma.
* **Persona B: O Intermediário (Mariana, 28 anos)**
  * **Objetivo:** Dominar movimentos mais complexos (dips, pull-ups perfeitas, iniciar L-sit) e aumentar a resistência.
  * **Dificuldade:** Platô nos treinos atuais; não sabe como progredir além de apenas adicionar mais repetições de flexões comuns.
  * **Necessidade:** Um guia claro de progressões de exercícios (ex: transição de flexão comum para flexão arqueiro) e controle de volume/intensidade semanal.

### 2. Escopo Funcional (Recursos Chave)
* **RF01 - Geração de Treinos Adaptativos:** O usuário informa seu nível de força atual por categoria de movimento (Empurrar, Puxar, Pernas, Core), seus equipamentos disponíveis (nenhum, barra, paralela) e recebe uma rotina de treino personalizada com séries e repetições sugeridas.
* **RF02 - Guia de Progressão Dinâmico:** Para cada exercício, se o usuário relatar que atingiu a meta de repetições (ex: 3 séries de 12 flexões limpas), o sistema deve apresentar o próximo exercício da cadeia evolutiva (ex: flexão declinada ou flexão diamante) e explicar como executá-lo.
* **RF03 - Registro e Acompanhamento de Treino:** Permitir ao usuário registrar as repetições realizadas em cada treino e visualizar sua curva de evolução de força ao longo do tempo.

### 3. Mapeamento de Limitações e Equipamentos
* **Níveis de Equipamento:**
  1. *Bodyweight Puro:* Apenas chão e superfícies domésticas comuns (cadeiras/sofás).
  2. *Básico:* Acesso a uma barra fixa (porta ou parque).
  3. *Completo:* Acesso a barras paralelas, argolas olímpicas, elásticos de resistência.
* **Restrições Comuns:** Problemas de articulação (punho, ombro, joelho) devem ser informados para adaptar/substituir exercícios agressivos (ex: trocar flexão tradicional por flexão sobre os punhos fechados se houver dor nos punhos).

---

## 🚦 Checklist de Validação da Etapa 1

- [ ] **Item 1:** Personas do usuário bem definidas e validadas.
- [ ] **Item 2:** Escopo de recursos (Geração de Treino, Progressão, Acompanhamento) detalhado e sem ambiguidades.
- [ ] **Item 3:** Mapeamento de equipamentos e restrições acordado.
