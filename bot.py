from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler
import random
from datetime import datetime

# Имя девушки
her_name = "Дашуля"

# 40 уникальных тёплых сообщений
daily_phrases = [
    f"{her_name}, ты — самое прекрасное, что случилось со мной 💕",
    f"{her_name}, я каждый день благодарю судьбу за тебя 🌸",
    f"{her_name}, твоя улыбка делает мой мир светлее 😊",
    f"{her_name}, я люблю всё в тебе, каждую мелочь 💖",
    f"{her_name}, даже мысли о тебе делают меня счастливым ✨",
    f"{her_name}, с тобой каждый момент особенный 💌",
    f"{her_name}, ты моё вдохновение и радость 🤍",
    f"{her_name}, я хочу обнимать тебя бесконечно 😍",
    f"{her_name}, твоя доброта и тепло меня завораживают 💖",
    f"{her_name}, я всегда думаю о тебе с улыбкой 😊",
    f"{her_name}, я люблю, когда мы вместе 💕",
    f"{her_name}, твоя поддержка делает меня сильнее 🌸",
    f"{her_name}, ты наполняешь мою жизнь счастьем ✨",
    f"{her_name}, я мечтаю о каждом моменте с тобой 💌",
    f"{her_name}, ты — моя радость и счастье 💖",
    f"{her_name}, я хочу, чтобы каждый день был с тобой 🤍",
    f"{her_name}, твоя красота — не только внешняя, но и внутренняя 😍",
    f"{her_name}, я скучаю по тебе даже когда мы вместе 💕",
    f"{her_name}, ты наполняешь моё сердце любовью 💖",
    f"{her_name}, с тобой каждый день — праздник ✨",
    f"{her_name}, твоя улыбка способна растопить любой лёд 💌",
    f"{her_name}, я хочу дарить тебе счастье каждый день 💕",
    f"{her_name}, мне так приятно думать о тебе 😍",
    f"{her_name}, ты — моя маленькая вселенная 💖",
    f"{her_name}, с тобой мир кажется ярче 🌸",
    f"{her_name}, я люблю слушать твой смех 😊",
    f"{her_name}, хочу, чтобы мы всегда были вместе 💕",
    f"{her_name}, твои глаза — как океан красоты 💖",
    f"{her_name}, каждый момент с тобой бесценен ✨",
    f"{her_name}, ты делаешь моё сердце счастливым 💌",
    f"{her_name}, я обожаю каждый твой взгляд 😍",
    f"{her_name}, с тобой даже обычный день — чудо 💖",
    f"{her_name}, ты наполняешь мою жизнь радостью 🌸",
    f"{her_name}, я люблю всё, что связано с тобой 💕",
    f"{her_name}, твоя нежность согревает меня 💖",
    f"{her_name}, я хочу быть рядом с тобой всегда 🤍",
    f"{her_name}, твоя забота делает меня счастливым 💌",
    f"{her_name}, ты — моя навсегда 💖",
    f"{her_name}, я хочу дарить тебе только счастье 🌸",
    f"{her_name}, твоя энергия вдохновляет меня каждый день ✨",
    f"{her_name}, с тобой я чувствую себя на седьмом небе 💕",
    f"{her_name}, твоя любовь делает меня сильнее 💖"
]

# Специальные даты
special_dates = {
    "08-11": f"{her_name}, сегодня наша годовщина! 💖 Помнишь, как мы познакомились? 😍",
    "02-14": f"{her_name}, с Днём влюблённых! 💌 Люблю тебя безмерно ❤️",
    "05-12": f"{her_name}, с днём рождения! 🎂💖 Пусть мечты сбываются!",
    "01-01": f"{her_name}, с Новым годом! 🎉 Пусть этот год будет нашим самым счастливым! 💕",
    "03-08": f"{her_name}, с 8 марта! 🌸 Люблю тебя, солнышко! 💖",
    "12-31": f"{her_name}, с наступающим Новым годом! 🎆 Пусть он будет волшебным для нас! 💌"
}

# Переменные
chat_id = None
sent_today = set()  # чтобы сообщения не повторялись каждый день

# Команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global chat_id
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Привет, {her_name}! 🤍 Теперь я буду присылать тебе тёплые сообщения и поздравления 💌")

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrase = random.choice(daily_phrases)
    await update.message.reply_text(phrase)

async def morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text=f"Доброе утро, {her_name}! ☀️💖 Пусть день будет красивым!")
async def night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text=f"Спокойной ночи, {her_name} 😴💌 Пусть сладкие сны будут о нас!")

# Автоматические функции
async def send_morning(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text=f"Доброе утро, {her_name}! ☀️💖")

async def send_night(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text=f"Спокойной ночи, {her_name} 😴💌")

async def send_daily_phrase(context: ContextTypes.DEFAULT_TYPE):
    global sent_today
    available = [msg for msg in daily_phrases if msg not in sent_today]
    if not available:
        sent_today = set()
        available = daily_phrases.copy()
    phrase = random.choice(available)
    sent_today.add(phrase)
    await context.bot.send_message(chat_id=chat_id, text=phrase)

async def send_special_date(context: ContextTypes.DEFAULT_TYPE):
    today = datetime.now().strftime("%m-%d")
    if today in special_dates:
        await context.bot.send_message(chat_id=chat_id, text=special_dates[today])

# Токен
TOKEN = "8069645041:AAHQE2k1r9gY4t0foY8gwNP5V3tjdfFHztU"
app = ApplicationBuilder().token(TOKEN).build()

# Добавляем команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("love", love))
app.add_handler(CommandHandler("morning", morning))
app.add_handler(CommandHandler("night", night))

# Планировщик
scheduler = BackgroundScheduler()

# Таймеры
scheduler.add_job(lambda: app.create_task(send_morning(app)), 'cron', hour=6, minute=0)
scheduler.add_job(lambda: app.create_task(send_night(app)), 'cron', hour=23, minute=0)
scheduler.add_job(lambda: app.create_task(send_daily_phrase(app)), 'cron', hour=12, minute=0)
scheduler.add_job(lambda: app.create_task(send_special_date(app)), 'cron', hour=9, minute=0)

scheduler.start()

# Запуск бота
app.run_polling()