from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from for_lemana_count import count_diam  # Импортируем нашу функцию


TOKEN = '7771023581:AAFMu7180GflNAIoT4zyr3ApPRHoKEqCLSM'


STATE_DIAMETER, STATE_VITKI, STATE_WIDTH = range(3)

user_data = {}

def start (update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_data[user_id] = {}
    
    
    update.message.reply_text(
        'Привет! Я от Трошкина ;). Могу посчитать погонные и квадратные метры. \n'
        'Введи диаметр рулона (в метрах): '
    )
    return STATE_DIAMETER

def get_diameter(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        diameter = float(update.message.text)
        user_data[user_id]['diameter'] = diameter
        
        update.message.reply_text('Теперь введи количество витков: ')
        return STATE_VITKI
    except ValueError:
        update.message.reply_text('Пожалуйста, введите число: ')
        return STATE_DIAMETER
    
    
def get_vitki(update:Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        vitki = float(update.message.text)
        user_data[user_id]['vitki'] = vitki
        
        update.message.reply_text('Теперь введи ширину (в метрах): ')
        return STATE_WIDTH
    except ValueError:
        update.message.reply_text('Пожалуйста, введи число: ')
        return STATE_VITKI
    
def get_width(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        width = float(update.message.text)
        user_data[user_id]['width'] = width

        # Получаем данные
        diameter = user_data[user_id]['diameter']
        vitki = user_data[user_id]['vitki']

        # Вычисляем
        pogony, kv_metri = count_diam(diameter, vitki, width)

        # Отправляем результат
        update.message.reply_text(
            f"📏 Результат:\n"
            f"Погонные метры: {pogony:.2f}\n"
            f"Квадратные метры: {kv_metri:.2f}\n\n"
            f"Для нового расчёта введите /start"
        )

        return -1  # Завершаем диалог
    except ValueError:
        update.message.reply_text("Пожалуйста, введите число (например: 0.5):")
        return STATE_WIDTH  
    

def error(update: Update, context: CallbackContext):
    update.message.reply_text("Произошла ошибка. Попробуйте снова /start")

# Главная функция
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Диалог
    conv_handler = MessageHandler(Filters.text & ~Filters.command, 
        [
            get_diameter,
            get_vitki,
            get_width
        ]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)

    print("Бот запущен...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()