import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from config import settings
from database.models import create_tables
from database.repo import PlanRepo
from database.models import AsyncSessionLocal
from services.redis_service import redis_service
from middlewares import (
    DatabaseMiddleware, UserMiddleware,
    AntiSpamMiddleware, BanCheckMiddleware,
)
from handlers import (
    start_router, subscription_router,
    profile_router, referral_router, support_router,
)
from admin.admin import router as admin_router

logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/bot.log"),
    ],
)
logger = logging.getLogger(__name__)


async def on_startup(bot: Bot):
    logger.info("Bot starting up...")

    # Connect Redis
    await redis_service.connect()
    logger.info("Redis connected")

    # Create DB tables
    await create_tables()
    logger.info("Database tables created/verified")

    # Seed default plans
    async with AsyncSessionLocal() as db:
        plan_repo = PlanRepo(db)
        await plan_repo.seed_default_plans()
    logger.info("Default plans seeded")

    # Set bot commands
    from aiogram.types import BotCommand
    await bot.set_my_commands([
        BotCommand(command="start", description="Boshlanish"),
        BotCommand(command="profile", description="Mening profilim"),
        BotCommand(command="subscribe", description="Obuna olish"),
        BotCommand(command="balance", description="Balansim"),
        BotCommand(command="referral", description="Referral havolam"),
        BotCommand(command="support", description="Qo'llab-quvvatlash"),
        BotCommand(command="help", description="Yordam"),
    ])

    me = await bot.get_me()
    logger.info(f"Bot started: @{me.username}")


async def on_shutdown(bot: Bot):
    logger.info("Bot shutting down...")
    await redis_service.disconnect()
    logger.info("Redis disconnected")


async def main():
    import os
    os.makedirs("logs", exist_ok=True)

    # Initialize Redis-backed FSM storage
    storage = RedisStorage.from_url(settings.REDIS_URL)

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher(storage=storage)

    # Register startup/shutdown
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Register middlewares (order matters)
    dp.update.middleware(DatabaseMiddleware())
    dp.update.middleware(UserMiddleware())
    dp.update.middleware(AntiSpamMiddleware())
    dp.update.middleware(BanCheckMiddleware())

    # Include routers
    dp.include_router(start_router)
    dp.include_router(subscription_router)
    dp.include_router(profile_router)
    dp.include_router(referral_router)
    dp.include_router(support_router)
    dp.include_router(admin_router)

    logger.info("Starting polling...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
