# -*- coding: utf-8 -*-

"""
CaliForge Data Models (models.py)
---------------------------------
Representação e validação de estruturas de dados de entrada e saída.
Implementa o tratamento de fallbacks seguros de acordo com a especificação de produto (Etapa 4).
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class HealthConditions:
    hasMobilityIssues: bool
    hasHealthRestrictions: bool
    mobilityDetails: Optional[str] = None
    healthRestrictionsDetails: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'HealthConditions':
        return cls(
            hasMobilityIssues=data.get("hasMobilityIssues", False),
            hasHealthRestrictions=data.get("hasHealthRestrictions", False),
            mobilityDetails=data.get("mobilityDetails"),
            healthRestrictionsDetails=data.get("healthRestrictionsDetails")
        )

@dataclass
class MovementLevels:
    push: int = 1
    pull: int = 1
    legs: int = 1
    abs: int = 1

    @classmethod
    def from_dict(cls, data: Optional[dict]) -> 'MovementLevels':
        if not data:
            return cls()
        return cls(
            push=data.get("push", 1),
            pull=data.get("pull", 1),
            legs=data.get("legs", 1),
            abs=data.get("abs", 1)
        )

@dataclass
class PainState:
    wrist: int = 0
    shoulder: int = 0
    elbow: int = 0
    knee: int = 0
    lowerBack: int = 0

    @classmethod
    def from_dict(cls, data: Optional[dict]) -> 'PainState':
        if not data:
            return cls()
        return cls(
            wrist=data.get("wrist", 0),
            shoulder=data.get("shoulder", 0),
            elbow=data.get("elbow", 0),
            knee=data.get("knee", 0),
            lowerBack=data.get("lowerBack", 0)
        )

@dataclass
class EquipmentAvailability:
    hasPullUpBar: bool = False
    hasParallelBars: bool = False
    hasResistanceBands: bool = False

    @classmethod
    def from_dict(cls, data: Optional[dict]) -> 'EquipmentAvailability':
        if not data:
            return cls()
        return cls(
            hasPullUpBar=data.get("hasPullUpBar", False),
            hasParallelBars=data.get("hasParallelBars", False),
            hasResistanceBands=data.get("hasResistanceBands", False)
        )

@dataclass
class WeeklyConsistency:
    completedWorkoutsThisWeek: int = 0
    targetWorkoutsPerWeek: int = 3

    @classmethod
    def from_dict(cls, data: Optional[dict]) -> 'WeeklyConsistency':
        if not data:
            return cls()
        return cls(
            completedWorkoutsThisWeek=data.get("completedWorkoutsThisWeek", 0),
            targetWorkoutsPerWeek=data.get("targetWorkoutsPerWeek", 3)
        )

@dataclass
class CaliForgeUserInput:
    userId: str
    name: str
    age: int
    height: float
    weight: float
    healthConditions: HealthConditions
    experienceLevel: str = "beginner"
    movementLevels: MovementLevels = field(default_factory=MovementLevels)
    painState: PainState = field(default_factory=PainState)
    equipmentAvailability: EquipmentAvailability = field(default_factory=EquipmentAvailability)
    weeklyConsistency: WeeklyConsistency = field(default_factory=WeeklyConsistency)

    @classmethod
    def from_dict(cls, data: dict) -> 'CaliForgeUserInput':
        # Requeridos pelo schema JSON
        userId = data.get("userId")
        name = data.get("name")
        age = data.get("age")
        height = data.get("height")
        weight = data.get("weight")
        
        raw_health = data.get("healthConditions")
        if raw_health is None:
            healthConditions = HealthConditions(hasMobilityIssues=False, hasHealthRestrictions=False)
        else:
            healthConditions = HealthConditions.from_dict(raw_health)

        return cls(
            userId=userId,
            name=name,
            age=age,
            height=height,
            weight=weight,
            healthConditions=healthConditions,
            experienceLevel=data.get("experienceLevel", "beginner"),
            movementLevels=MovementLevels.from_dict(data.get("movementLevels")),
            painState=PainState.from_dict(data.get("painState")),
            equipmentAvailability=EquipmentAvailability.from_dict(data.get("equipmentAvailability")),
            weeklyConsistency=WeeklyConsistency.from_dict(data.get("weeklyConsistency"))
        )

@dataclass
class RepsRange:
    min: int
    max: int

    def to_dict(self) -> dict:
        return {"min": self.min, "max": self.max}

@dataclass
class Exercise:
    exerciseName: str
    category: str  # push, pull, legs, abs
    level: int
    sets: int
    repsRange: RepsRange
    restSeconds: int
    executionGuide: str

    def to_dict(self) -> dict:
        return {
            "exerciseName": self.exerciseName,
            "category": self.category,
            "level": self.level,
            "sets": self.sets,
            "repsRange": self.repsRange.to_dict(),
            "restSeconds": self.restSeconds,
            "executionGuide": self.executionGuide
        }

@dataclass
class CaliForgeWorkoutOutput:
    workoutId: str
    date: str
    focus: str  # push, pull, legs, abs, fullbody
    exercises: List[Exercise]
    recoveryNotes: str

    def to_dict(self) -> dict:
        return {
            "workoutId": self.workoutId,
            "date": self.date,
            "focus": self.focus,
            "exercises": [e.to_dict() for e in self.exercises],
            "recoveryNotes": self.recoveryNotes
        }
