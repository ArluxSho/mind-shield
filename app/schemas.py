from typing import Literal

from pydantic import BaseModel, Field


class StudentData(BaseModel):

    gender: Literal["Male", "Female"]

    age: int = Field(..., ge=18, le=35)

    academic_pressure: int = Field(..., ge=1, le=5)

    study_satisfaction: int = Field(..., ge=1, le=5)

    sleep_duration: Literal[
        "Less than 5 hours",
        "5-6 hours",
        "7-8 hours",
        "More than 8 hours"
    ]

    dietary_habits: Literal[
        "Healthy",
        "Moderate",
        "Unhealthy"
    ]

    suicidal_thoughts: Literal[
        "Yes",
        "No"
    ]

    study_hours: int = Field(..., ge=0, le=12)

    financial_stress: int = Field(..., ge=1, le=5)

    family_history: Literal[
        "Yes",
        "No"
    ]