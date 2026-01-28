from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# ====== SOZLAMALAR ======
BOT_TOKEN = "PASTE_YOUR_NEW_TOKEN_HERE" 8231083442:AAGnrjhYS2z9b9zb9veZpcxMoZWVnmYrKGc
PREMIUM_CHANNEL = "https://t.me/+pGhN_CYDofNmMGEy"
ADMIN_ID = 7488316739
PREMIUM_PRICE = "250 000 so‘m"
REF_DAYS = 45

# ====== /start ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args

    text = f"""
👋 Salom {user.first_name}!

🤖 *SmartUz AI Premium Bot*

💎 Premium narxi: *{PREMIUM_PRICE}*
🎁 3 ta referal = *{REF_DAYS} kun* BEPUL premium

👇 Tanlang:
"""

    keyboard = [
        [InlineKeyboardButton("💎 Premium olish", callback_data="premium")],
        [InlineKeyboardButton("🎁 Referal orqali", callback_data="referal")],
        [InlineKeyboardButton("🔒 Premium kanal", url=PREMIUM_CHANNEL)]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# ====== PREMIUM ======
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = f"""
💎 *Premium obuna*

💰 Narx: *{PREMIUM_PRICE}*

💳 To‘lov usullari:
• Click
• Manual (screenshot yuborish)

📩 To‘lovdan so‘ng admin bilan bog‘laning.
"""

    await query.edit_message_text(text, parse_mode="Markdown")

# ====== REFERAL ======
async def referal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    bot_username = context.bot.username
    user_id = query.from_user.id

    ref_link = f"https://t.me/{bot_username}?start={user_id}"

    text = f"""
🎁 *Referal tizimi*

👥 3 ta odam chaqiring
⏳ {REF_DAYS} kun BEPUL premium

🔗 Sizning referal linkingiz:
{ref_link}
"""

    await query.edit_message_text(text, parse_mode="Markdown")

# ====== CALLBACK ======
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.data == "premium":
        await premium(update, context)
    elif query.data == "referal":
        await referal(update, context)

# ====== MAIN ======
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("✅ SmartUz AI Bot ishga tushdi")
    app.run_polling()

if __name__ == "__main__":
    main()
