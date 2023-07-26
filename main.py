import logging.config
import os
from aiogram import executor
from data.logging import LOGGING_CONFIG
from bot import dp

# Убедимся, что папка logs существует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Применяем конфигурацию логирования
# logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        from bot import handlers
        logger.info("Starting bot")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logger.exception("Error occurred while starting the bot")
