from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, logger
from database.models import Base


def connect_db() -> AsyncEngine:
    """
    Функция для асинхронного создания пула соединения
    """

    engine = create_async_engine(
        f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        pool_pre_ping=True,
    )
    return engine


async def create_db() -> None:
    """
    Функция для удаления старой и создания новой таблицы БД
    """

    try:
        engine = connect_db()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        await engine.dispose()
        logger.info("Таблица spimex_trading в БД создана!")
    except Exception as ex:
        logger.exception("Ошибка создания БД: " + str(ex), exc_info=True)
