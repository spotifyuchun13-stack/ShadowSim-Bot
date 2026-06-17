from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Telegram
    BOT_TOKEN: str
    BOT_USERNAME: str = "Uzbek_seenuz_bot"

    # Admin
    ADMIN_IDS: List[int] = []
    ADMIN_PASSWORD: str = "admin123"

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@db:5432/seenuz_bot"
    REDIS_URL: str = "redis://redis:6379/0"

    # Payment - Payme
    PAYME_MERCHANT_ID: str = ""
    PAYME_SECRET_KEY: str = ""
    PAYME_TEST_SECRET_KEY: str = ""
    PAYME_IS_TEST: bool = True

    # Payment - Click
    CLICK_SERVICE_ID: str = ""
    CLICK_MERCHANT_ID: str = ""
    CLICK_SECRET_KEY: str = ""
    CLICK_MERCHANT_USER_ID: str = ""

    # Payment - Uzum
    UZUM_MERCHANT_ID: str = ""
    UZUM_SECRET_KEY: str = ""

    # Prices
    SUBSCRIPTION_1_MONTH_PRICE: int = 15000   # UZS (tiyin)
    SUBSCRIPTION_3_MONTH_PRICE: int = 35000
    SUBSCRIPTION_6_MONTH_PRICE: int = 60000
    SUBSCRIPTION_12_MONTH_PRICE: int = 100000

    # Referral
    REFERRAL_BONUS_INVITER: int = 5000    # UZS
    REFERRAL_BONUS_INVITED: int = 2000    # UZS
    REFERRAL_MIN_WITHDRAW: int = 50000    # UZS

    # Channel (majburiy obuna)
    REQUIRED_CHANNEL_ID: int = -1001234567890
    REQUIRED_CHANNEL_USERNAME: str = "@seenuz_channel"

    # App
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    WEBHOOK_URL: str = ""
    WEBHOOK_PATH: str = "/webhook"
    WEB_SERVER_HOST: str = "0.0.0.0"
    WEB_SERVER_PORT: int = 8080

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
