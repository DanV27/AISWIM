from typing import List, Optional, Literal
from pydantic import BaseModel, Field

SwimLevel = Literal["beginner", "intermediate", "advanced"]
FocusType = Literal["speed", "technique", "endurance"]
Stroke = Literal["freestyle", "backstroke", "breaststroke", "butterfly", "choice"]

class GenerateRequest(BaseModel):
    level: SwimLevel
    total_yards: int = Field(..., ge=100, le=5000)
    focus: FocusType
    stroke: Optional[Stroke] = "freestyle"
    equipment: List[str] = Field(default_factory=list)

class Block(BaseModel):
    type: Literal["warmup", "main", "cooldown"]
    yards: int
    details: List[str]

class GenerateResponse(BaseModel):
    total_yards: int
    level: SwimLevel
    focus: FocusType
    stroke: Stroke
    blocks: List[Block]
