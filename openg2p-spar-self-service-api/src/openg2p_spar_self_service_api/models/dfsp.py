from typing import Optional, List
from sqlalchemy import ForeignKey, Integer, String, select, Column
from sqlalchemy.orm import relationship, Mapped
from openg2p_fastapi_common.models import BaseORMModelWithTimes
from sqlalchemy.ext.asyncio import async_sessionmaker
from openg2p_fastapi_common.context import dbengine

from .strategy import Strategy


class DfspLevel(BaseORMModelWithTimes):
    __tablename__ = "dfsp_levels"

    name: Mapped[str] = Column(String)
    code: Mapped[str] = Column(String(20))
    parent: Mapped[Optional[int]] = Column(
        Integer, ForeignKey("dfsp_levels.id"), nullable=True
    )
    validation_regex: Mapped[Optional[str]] = Column(String, nullable=True)

    @classmethod
    async def get_level(cls, **kwargs):
        response = []
        async_session_maker = async_sessionmaker(dbengine.get())
        async with async_session_maker() as session:
            stmt = select(cls)
            for key, value in kwargs.items():
                if value is not None:
                    stmt = stmt.where(getattr(cls, key) == value)

            stmt = stmt.order_by(cls.id.asc())

            result = await session.execute(stmt)

            response = list(result.scalars())
        return response


class DfspLevelValue(BaseORMModelWithTimes):
    __tablename__ = "dfsp_level_values"

    name: Mapped[str] = Column(String)
    code: Mapped[str] = Column(String(20))
    parent: Mapped[Optional[int]] = Column(
        Integer, ForeignKey("dfsp_level_values.id"), nullable=True
    )
    level_id: Mapped[int] = Column(Integer, ForeignKey("dfsp_levels.id"))
    strategy_id: Mapped[Optional[int]] = Column(
        Integer, ForeignKey("strategy.id"), nullable=True
    )

    strategy: Mapped[Optional[Strategy]] = relationship("Strategy")

    @classmethod
    async def get_level_values(cls, **kwargs):
        response = []
        async_session_maker = async_sessionmaker(dbengine.get())
        async with async_session_maker() as session:
            stmt = select(cls)
            for key, value in kwargs.items():
                if value is not None:
                    stmt = stmt.where(getattr(cls, key) == value)

            stmt = stmt.order_by(cls.id.asc())

            result = await session.execute(stmt)

            response = list(result.scalars())
        return response
