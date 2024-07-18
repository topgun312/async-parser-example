from parser.data_processing import ProcessingData

import asyncpg

from config import DB_NAME, logger


class AddDataToDataBase:

    async def add_processing_data_to_db(self) -> None:
        """
        Метод класса для загрузки обработанных данных в таблицу "spimex_trading" базы данных
        """

        dataframe_list = ProcessingData().create_dataframe_list()
        conn = await asyncpg.connect(database=f"{DB_NAME}")
        try:
            for df_item in dataframe_list:
                tuples = [tuple(x) for x in df_item.values]
                await conn.copy_records_to_table(
                    "spimex_trading",
                    records=tuples,
                    columns=list(df_item.columns),
                    timeout=10,
                )
            logger.info("Данные в таблицу spimex_trading загружены успешно!")
        except Exception as ex:
            logger.exception("Ошибка добавления данных БД: " + str(ex), exc_info=True)
