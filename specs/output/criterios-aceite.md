# Critérios de Aceitação e Plano de Teste: CaliForge

Este documento define os critérios de aceitação, testes manuais e asserções lógicas automatizadas que o algoritmo do CaliForge deve atender para homologação.

---

## 🧪 Casos de Teste do Dataset (Cenários Reais)

Estes cenários representam perfis típicos do dataset de avaliação do Harness:

### [CT-001] Iniciante + Dor Aguda + Sem Equipamentos
* **Perfil do Usuário (Entrada):**
  ```json
  {
    "userId": "usr_001",
    "name": "Pedro",
    "age": 24,
    "height": 1.75,
    "weight": 70.0,
    "healthConditions": {
      "hasMobilityIssues": false,
      "hasHealthRestrictions": false
    },
    "experienceLevel": "beginner",
    "movementLevels": {
      "push": 1,
      "pull": 1,
      "legs": 1,
      "abs": 1
    },
    "painState": {
      "wrist": 4,
      "shoulder": 0,
      "elbow": 0,
      "knee": 0,
      "lowerBack": 0
    },
    "equipmentAvailability": {
      "hasPullUpBar": false,
      "hasParallelBars": false,
      "hasResistanceBands": false
    },
    "weeklyConsistency": {
      "completedWorkoutsThisWeek": 0,
      "targetWorkoutsPerWeek": 3
    }
  }
  ```
* **Comportamento Esperado (Saída):**
  - O treino gerado não deve conter exercícios de empurrar que apoiem o peso do corpo sobre os punhos (como flexões no chão).
  - Deve conter substitutos seguros de baixo impacto (ex: flexões na parede com punhos fechados) ou focar a sessão em pernas e core.
  - Se prescrever exercícios de puxar, deve sugerir remada inclinada leve sob a mesa (bodyweight puro adaptado).

### [CT-002] Intermediário + Equipamentos Completos + Alta Performance
* **Perfil do Usuário (Entrada):**
  ```json
  {
    "userId": "usr_002",
    "name": "Mariana",
    "age": 28,
    "height": 1.65,
    "weight": 58.0,
    "healthConditions": {
      "hasMobilityIssues": false,
      "hasHealthRestrictions": false
    },
    "experienceLevel": "intermediate",
    "movementLevels": {
      "push": 5,
      "pull": 4,
      "legs": 3,
      "abs": 3
    },
    "painState": {
      "wrist": 0,
      "shoulder": 0,
      "elbow": 0,
      "knee": 0,
      "lowerBack": 0
    },
    "equipmentAvailability": {
      "hasPullUpBar": true,
      "hasParallelBars": true,
      "hasResistanceBands": true
    },
    "weeklyConsistency": {
      "completedWorkoutsThisWeek": 3,
      "targetWorkoutsPerWeek": 4
    }
  }
  ```
* **Comportamento Esperado (Saída):**
  - Deve incluir movimentos estruturados suspensos como barra fixa (pull-up/chin-up) e paralelas (dips).
  - Os exercícios de core e pernas devem estar alinhados com o nível intermediário (ex: hollow body holds, dips nas paralelas, barra fixa pronada).

### [CT-003] Reabilitação Articular Múltipla + Sem Equipamentos
* **Perfil do Usuário (Entrada):**
  ```json
  {
    "userId": "usr_003",
    "name": "Carlos",
    "age": 35,
    "height": 1.80,
    "weight": 85.0,
    "healthConditions": {
      "hasMobilityIssues": true,
      "mobilityDetails": "Falta de mobilidade de ombros",
      "hasHealthRestrictions": false
    },
    "experienceLevel": "intermediate",
    "movementLevels": {
      "push": 3,
      "pull": 3,
      "legs": 3,
      "abs": 3
    },
    "painState": {
      "wrist": 0,
      "shoulder": 2,
      "elbow": 0,
      "knee": 0,
      "lowerBack": 1
    },
    "equipmentAvailability": {
      "hasPullUpBar": false,
      "hasParallelBars": false,
      "hasResistanceBands": false
    },
    "weeklyConsistency": {
      "completedWorkoutsThisWeek": 2,
      "targetWorkoutsPerWeek": 3
    }
  }
  ```
* **Comportamento Esperado (Saída):**
  - Os exercícios de empurrar devem ter impacto reduzido nas articulações do ombro (ex: flexão inclinada elevada em mesa).
  - Devem ser incorporados no plano de treino exercícios de mobilidade de ombro leves para fins de reabilitação ativa.
  - Exercícios que gerem alta tensão lombar estática longa (ex: pranchas isométricas com duração > 60s) devem ser cortados ou adaptados para menor tempo/intensidade devido ao relato de dor na lombar.

### [CT-004] Baixa Consistência + Treino Regenerativo
* **Perfil do Usuário (Entrada):**
  ```json
  {
    "userId": "usr_004",
    "name": "Ana",
    "age": 30,
    "height": 1.70,
    "weight": 65.0,
    "healthConditions": {
      "hasMobilityIssues": false,
      "hasHealthRestrictions": false
    },
    "experienceLevel": "intermediate",
    "movementLevels": {
      "push": 4,
      "pull": 3,
      "legs": 3,
      "abs": 3
    },
    "painState": {
      "wrist": 0,
      "shoulder": 0,
      "elbow": 0,
      "knee": 0,
      "lowerBack": 0
    },
    "equipmentAvailability": {
      "hasPullUpBar": true,
      "hasParallelBars": false,
      "hasResistanceBands": false
    },
    "weeklyConsistency": {
      "completedWorkoutsThisWeek": 1,
      "targetWorkoutsPerWeek": 4
    }
  }
  ```
* **Comportamento Esperado (Saída):**
  - Nenhum exercício deve exceder o nível de movimento atual do usuário (sem progressões).
  - O volume de séries ou faixas de repetições prescrito deve ser moderado/regenerativo para incentivar a readaptação e consistência da rotina, sem causar fadiga sistêmica severa.

### [CT-005] Avançado + Foco em Pernas
* **Perfil do Usuário (Entrada):**
  ```json
  {
    "userId": "usr_005",
    "name": "Bruno",
    "age": 27,
    "height": 1.78,
    "weight": 76.0,
    "healthConditions": {
      "hasMobilityIssues": false,
      "hasHealthRestrictions": false
    },
    "experienceLevel": "advanced",
    "movementLevels": {
      "push": 6,
      "pull": 5,
      "legs": 5,
      "abs": 4
    },
    "painState": {
      "wrist": 0,
      "shoulder": 0,
      "elbow": 0,
      "knee": 0,
      "lowerBack": 0
    },
    "equipmentAvailability": {
      "hasPullUpBar": true,
      "hasParallelBars": true,
      "hasResistanceBands": true
    },
    "weeklyConsistency": {
      "completedWorkoutsThisWeek": 4,
      "targetWorkoutsPerWeek": 5
    }
  }
  ```
* **Comportamento Esperado (Saída):**
  - O treino gerado deve conter exercícios avançados de perna (ex: Pistol Squats livres).
  - **Salvaguarda de Equilíbrio Ativa:** O plano de treino deve incluir pelo menos 1 exercício de empurrar, 1 de puxar e 1 de core em nível de manutenção para evitar o desbalanço postural induzido pelo foco exclusivo.

---

## 🚦 Critérios de Aceitação Lógicos (Assertions)

Estas asserções binárias devem ser validadas programaticamente durante a rodada do Harness de teste ou manualmente:

### [CA-001] Bloqueio de Segurança por Dor (Pain Lockout)
* **Descrição da Regra:** Exercícios que apoiem peso corporal direto ou causem estresse severo em articulações com dor aguda (intensidade >= 3 no perfil) são proibidos.
* **Asserção Lógica:**
  ```python
  for exercise in workout.exercises:
      if user.painState.get("wrist", 0) >= 3 and exercise.category == "push":
          assert exercise.exerciseName not in ["flexao_tradicional", "dips", "flexao_diamante"], "Erro: Prescreveu flexões/dips comuns para punho com dor aguda"
      if user.painState.get("knee", 0) >= 3 and exercise.category == "legs":
          assert exercise.exerciseName not in ["agachamento_pistola", "agachamento_bulgaro"], "Erro: Prescreveu agachamento unilateral para joelho com dor aguda"
  ```
* **Forma de Teste:** [x] Automatizado (Harness) | [ ] Manual

### [CA-002] Equilíbrio Anatômico de Grupos Opostos (Push/Pull Ratio)
* **Descrição da Regra:** Sessões prescritas com foco de treino de corpo inteiro ("fullbody") devem manter uma proporção anatômica equilibrada de volume e exercícios entre as categorias de empurrar (push) e puxar (pull).
* **Asserção Lógica:**
  ```python
  if workout.focus == "fullbody":
      push_count = sum(1 for e in workout.exercises if e.category == "push")
      pull_count = sum(1 for e in workout.exercises if e.category == "pull")
      ratio = push_count / max(1, pull_count)
      assert 0.8 <= ratio <= 1.2, f"Erro: Treino fullbody desequilibrado push/pull (ratio: {ratio})"
  ```
* **Forma de Teste:** [x] Automatizado (Harness) | [ ] Manual

### [CA-003] Bloqueio de Sobrecarga por Inconstância Semanal
* **Descrição da Regra:** O algoritmo de treino é proibido de sugerir progressões de nível para exercícios caso o usuário não tenha completado a frequência mínima segura de consistência de treinos na semana (< 2 treinos realizados).
* **Asserção Lógica:**
  ```python
  if user.weeklyConsistency.completedWorkoutsThisWeek < 2:
      for exercise in workout.exercises:
          current_level = user.movementLevels.get(exercise.category, 1)
          assert exercise.level <= current_level, f"Erro: Progrediu nível do exercício {exercise.exerciseName} sob baixa consistência"
  ```
* **Forma de Teste:** [x] Automatizado (Harness) | [ ] Manual

### [CA-004] Validação de Equipamentos Obrigatórios
* **Descrição da Regra:** Exercícios que exijam equipamentos suspensos (ex: barras fixas ou paralelas) não devem ser sugeridos se o usuário não declarar sua disponibilidade no perfil.
* **Asserção Lógica:**
  ```python
  for exercise in workout.exercises:
      if exercise.category == "pull" and exercise.exerciseName in ["barra_fixa", "pull_up", "chin_up", "l_sit_pull_up"]:
          assert user.equipmentAvailability.hasPullUpBar, "Erro: Prescreveu barra fixa sem equipamento disponível no perfil"
      if exercise.category == "push" and exercise.exerciseName == "dips":
          assert user.equipmentAvailability.hasParallelBars, "Erro: Prescreveu paralela (dips) sem equipamento disponível no perfil"
  ```
* **Forma de Teste:** [x] Automatizado (Harness) | [ ] Manual

### [CA-005] Sincronização por Diálogo (Chat Sync Parser)
* **Descrição da Regra:** Entradas coloquiais informando séries e repetições no chat de diálogo diário devem atualizar corretamente e de forma síncrona o Plano do Dia no dashboard.
* **Asserção Lógica:**
  - Frase de Entrada: *"hoje fiz 3 séries de 10 flexões"*
  - Mapeamento de Saída: `exerciseName: "flexao_tradicional", sets_completed: 3, reps_completed: 10`
* **Forma de Teste:** [ ] Automatizado (Harness) | [x] Manual (Teste de Interface de Usuário)
