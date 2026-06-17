# 🎬 Seenuz Bot

O'zbekiston uchun premium Telegram bot — to'lov tizimi, referral, obuna boshqaruvi.

---

## 📋 Imkoniyatlar

| Funksiya | Tavsif |
|---|---|
| 💎 Obuna tizimi | 1/3/6/12 oylik rejalar |
| 💳 Payme | Payme Subscribe integratsiya |
| 🔵 Click | Click Merchant API |
| 🟠 Uzum Bank | Uzum to'lov tizimi |
| 👥 Referral | Taklif tizimi va bonuslar |
| 💰 Balans | Bonus balans va pul chiqarish |
| 📢 Kanal obunasi | Majburiy kanal tekshiruvi |
| ⚙️ Admin panel | Statistika, broadcast, foydalanuvchi boshqaruvi |

---

## 🗄️ Ma'lumotlar bazasi jadvallari

```
users               — Foydalanuvchilar
subscription_plans  — Obuna rejalari
subscriptions       — Faol obunalar
payments            — To'lovlar tarixi
referral_bonuses    — Referral bonuslar
withdrawals         — Pul chiqarish so'rovlari
notifications       — Xabarlar
```

---

## 🚀 O'rnatish

### 1. Talablar

- Docker & Docker Compose
- Telegram Bot Token ([@BotFather](https://t.me/BotFather))
- Payme/Click/Uzum merchant akkauntlari

### 2. Sozlash

```bash
git clone https://github.com/yourrepo/seenuz-bot.git
cd seenuz-bot
cp .env.example .env
nano .env    # sozlamalarni kiriting
```

### 3. Ishga tushirish

```bash
docker compose up -d
```

Loglarni kuzatish:
```bash
docker compose logs -f bot
```

### 4. To'xtatish

```bash
docker compose down
```

---

## ⚙️ .env sozlamalari

| Kalit | Tavsif |
|---|---|
| `BOT_TOKEN` | BotFather dan olingan token |
| `ADMIN_IDS` | Admin Telegram ID lari (JSON array) |
| `DATABASE_URL` | PostgreSQL ulanish URL |
| `REDIS_URL` | Redis ulanish URL |
| `PAYME_MERCHANT_ID` | Payme merchant ID |
| `PAYME_SECRET_KEY` | Payme secret key |
| `PAYME_IS_TEST` | `true` test rejim, `false` production |
| `CLICK_SERVICE_ID` | Click service ID |
| `CLICK_MERCHANT_ID` | Click merchant ID |
| `REQUIRED_CHANNEL_ID` | Majburiy kanal ID (manfiy son) |
| `REFERRAL_BONUS_INVITER` | Taklif qiluvchiga bonus (so'm) |
| `REFERRAL_BONUS_INVITED` | Taklif qilinganga bonus (so'm) |

---

## 🤖 Bot buyruqlari

| Buyruq | Tavsif |
|---|---|
| `/start` | Boshlanish, ro'yxatdan o'tish |
| `/profile` | Profil va obuna holati |
| `/subscribe` | Obuna rejalarini ko'rish |
| `/balance` | Balans va pul chiqarish |
| `/referral` | Referral havolam |
| `/support` | Qo'llab-quvvatlash |
| `/admin` | Admin panel (faqat adminlar) |

---

## 📁 Loyiha tuzilmasi

```
seenuz-bot/
├── main.py                    # Asosiy kirish nuqtasi
├── config.py                  # Sozlamalar (Pydantic)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
│
├── database/
│   ├── models.py              # SQLAlchemy modellari
│   └── repo.py                # Repository layer (CRUD)
│
├── handlers/
│   ├── start.py               # /start, asosiy menyu
│   ├── subscription.py        # Obuna va to'lov
│   ├── profile.py             # Profil va tarix
│   ├── referral.py            # Referral va balans
│   └── support.py             # Qo'llab-quvvatlash
│
├── keyboards/
│   └── keyboards.py           # Barcha klaviaturalar
│
├── services/
│   ├── payment.py             # Payme/Click/Uzum
│   └── redis_service.py       # Redis cache
│
├── middlewares/
│   └── middlewares.py         # DB, User, Spam, Ban
│
├── admin/
│   └── admin.py               # Admin panel
│
└── logs/                      # Log fayllar
```

---

## 💳 To'lov tizimi arxitekturasi

```
Foydalanuvchi → Reja tanlaydi → Provider tanlaydi
                                      ↓
                             To'lov URL generatsiya
                                      ↓
                             Foydalanuvchi to'laydi
                                      ↓
                          "Tekshirish" tugmasini bosadi
                                      ↓
                        Provider API'dan status so'raladi
                                      ↓
                    Tasdiqlansa → Obuna yaratiladi ✅
```

---

## 👥 Referral tizimi

```
A taklif qiladi B ni
        ↓
B /start?ref_CODE bosadi
        ↓
B ro'yxatdan o'tadi
        ↓
A balansiga +5,000 so'm
B balansiga +2,000 so'm
        ↓
Minimal 50,000 so'm to'plansa
        ↓
Karta raqamiga pul chiqarish
```

---

## 🔧 Development

Local ishga tushirish (Docker'siz):

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# .env ni tahrirlang, local DB/Redis URL lari bilan

python main.py
```

---

## 📊 Monitoring

```bash
# Bot loglari
docker compose logs -f bot

# DB ulangan holda
docker compose --profile dev up -d    # Adminer 8080 portda

# Redis monitoring
docker exec -it seenuz_redis redis-cli monitor
```

---

## 📄 Litsenziya

MIT License — erkin foydalanish mumkin.
