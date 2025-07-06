from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    ConversationHandler
)
from for_lemana_count import count_diam
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Состояния диалога
DIAMETER, VITKI, WIDTH = range(3)

class MaterialCalculatorBot:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.dp = self.updater.dispatcher
        self.user_data = {}
        
        self._setup_handlers()
    
    def _setup_handlers(self):
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', self.start)],
            states={
                DIAMETER: [MessageHandler(filters.Filters.text & ~filters.Filters.command, self.get_diameter)],
                VITKI: [MessageHandler(filters.Filters.text & ~filters.Filters.command, self.get_vitki)],
                WIDTH: [MessageHandler(filters.Filters.text & ~filters.Filters.command, self.get_width)]
            },
            fallbacks=[CommandHandler('cancel', self.cancel)],
            allow_reentry=True
        )
        
        self.dp.add_handler(conv_handler)
        self.dp.add_error_handler(self.error_handler)
    
    def start(self, update: Update, context: CallbackContext) -> int:
        user_id = update.message.from_user.id
        self.user_data[user_id] = {}
        update.message.reply_text(
            "📏 Калькулятор материалов\n"
            "Введите диаметр рулона (в метрах):"
        )
        return DIAMETER
    
    def get_diameter(self, update: Update, context: CallbackContext) -> int:
        try:
            diameter = float(update.message.text.replace(',', '.'))
            if diameter <= 0:
                update.message.reply_text("❌ Диаметр должен быть > 0")
                return DIAMETER
            
            self.user_data[update.message.from_user.id]['diameter'] = diameter
            update.message.reply_text("Введите количество витков:")
            return VITKI
        except ValueError:
            update.message.reply_text("❌ Введите число (например: 1.5)")
            return DIAMETER
    
    def get_vitki(self, update: Update, context: CallbackContext) -> int:
        try:
            vitki = float(update.message.text.replace(',', '.'))
            if vitki <= 0:
                update.message.reply_text("❌ Количество должно быть > 0")
                return VITKI
            
            self.user_data[update.message.from_user.id]['vitki'] = vitki
            update.message.reply_text("Введите ширину материала (в метрах):")
            return WIDTH
        except ValueError:
            update.message.reply_text("❌ Введите число (например: 10)")
            return VITKI
    
    def get_width(self, update: Update, context: CallbackContext) -> int:
        try:
            width = float(update.message.text.replace(',', '.'))
            if width <= 0:
                update.message.reply_text("❌ Ширина должна быть > 0")
                return WIDTH
            
            user_id = update.message.from_user.id
            data = self.user_data.get(user_id, {})
            if not data:
                update.message.reply_text("❌ Данные не найдены. Начните заново: /start")
                return ConversationHandler.END
                
            pogony, kv_metri = count_diam(data['diameter'], data['vitki'], width)
            
            update.message.reply_text(
                f"✅ Результат:\n"
                f"▪ Погонные метры: {pogony:.2f}\n"
                f"▪ Квадратные метры: {kv_metri:.2f}\n\n"
                f"Новый расчёт: /start"
            )
            return ConversationHandler.END
        except ValueError:
            update.message.reply_text("❌ Введите число (например: 0.5)")
            return WIDTH
        except Exception as e:
            logger.error(f"Error in get_width: {e}")
            update.message.reply_text("❌ Произошла ошибка при расчетах")
            return ConversationHandler.END
    
    def cancel(self, update: Update, context: CallbackContext) -> int:
        update.message.reply_text("❌ Диалог отменён. /start - начать заново")
        return ConversationHandler.END
    
    def error_handler(self, update: object, context: CallbackContext) -> None:
        error = context.error
        logger.error(f"Ошибка: {error}", exc_info=True)
        
        if update and hasattr(update, 'message'):
            update.message.reply_text(
                "⚠️ Техническая ошибка\n"
                "Попробуйте снова: /start\n"
                f"Код ошибки: {type(error).__name__}"
            )
    
    def run(self) -> None:
        self.updater.start_polling()
        self.updater.idle()


# Для запуска бота
if __name__ == '__main__':
    TOKEN = "7771023581:AAFMu7180GflNAIoT4zyr3ApPRHoKEqCLSM"
    bot = MaterialCalculatorBot(TOKEN)
    bot.run()