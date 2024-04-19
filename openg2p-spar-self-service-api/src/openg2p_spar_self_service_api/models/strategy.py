from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum

from openg2p_fastapi_common.models import BaseORMModelWithTimes


class Strategy(BaseORMModelWithTimes):
    __tablename__ = "strategy"

    description = Column(String)
    strategy_type = Column(
        String,
        nullable=False,
        default=Enum(
            "StrategyType", {"DECONSTRUCT": "DECONSTRUCT", "CONSTRUCT": "CONSTRUCT"}
        ),
    )
    deconstruct_strategy = Column(String)
    construct_strategy = Column(String)

    level_values = relationship("DfspLevelValue", back_populates="strategy")
