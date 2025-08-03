from openg2p_fastapi_auth.models.orm.login_provider import LoginProvider as BaseLoginProvider
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .strategy import Strategy


class LoginProvider(BaseLoginProvider):
    strategy_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("strategy.id"))
    strategy: Mapped[Strategy | None] = relationship("Strategy")
