import asyncio
import time

from parser.parse_data import ParseDataFromSite

from config import logger
from database.add_data import AddDataToDataBase
from database.db import create_db


async def main():
    """
    Основная функция для вызова работы всего скрипта
    """
    parse = ParseDataFromSite()
    add_data_class = AddDataToDataBase()
    await create_db()
    await parse.get_page_count()
    await add_data_class.add_processing_data_to_db()


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    finish_time = time.time()
    work_time = round(finish_time - start_time, 1)
    logger.info(f"Операция выполнена успешно. Время работы: {work_time} секунд")
