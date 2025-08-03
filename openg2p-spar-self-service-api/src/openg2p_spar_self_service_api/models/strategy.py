from enum import Enum

from openg2p_fastapi_common.models import BaseORMModelWithTimes
from sqlalchemy import Enum as SaEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class StrategyType(Enum):
    ID = "ID"
    FA = "FA"


class Strategy(BaseORMModelWithTimes):
    __tablename__ = "strategy"

    description: Mapped[str] = mapped_column(String)
    strategy_type: Mapped[StrategyType] = mapped_column(SaEnum(StrategyType))
    deconstruct_strategy: Mapped[str] = mapped_column(String)
    construct_strategy: Mapped[str] = mapped_column(String)

    level_values = relationship("DfspLevelValue", back_populates="strategy")
