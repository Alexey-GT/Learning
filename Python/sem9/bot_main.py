from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
from config import TOKEN
from calc import calc_main
from calc_complex import calc_complex_main
from calc_fraction import calc_fraction_main
from calc_log_reader import log_reader
from fun import cat, joke, yesno

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ много чего умею!\nДля вывода списка комманд введите /help")



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('''Калькулятор: /calculate\nРазвлечения: /fun\nПринятие решений: /yn_ann\nИ самое важное: /best''')

@dp.message_handler(commands=['calculate'])
async def process_calc_command(message: types.Message):
    await message.reply(f'''Есть несколько видов калькуляторов:
      Для простых чисел: /eval <выражение>
      Для комплексных чисел: /complex <a+bj + c-dj>
      Для дробных чисел: /fraction <a/b + c/d>
      Просмотр лога калькулятора: /calc_log''')

@dp.message_handler(commands=['complex'])
async def process_complex_command(message: types.Message, command: Command):
    await message.reply(f"По моим подсчетам {calc_complex_main(command.args)}")

@dp.message_handler(commands=['fraction'])
async def process_fraction_command(message: types.Message, command: Command):
    await message.reply(f"По моим подсчетам {calc_fraction_main(command.args)}")   

@dp.message_handler(commands=['calc_log'])
async def process_calc_log_command(message: types.Message):
    await message.reply(log_reader())  

@dp.message_handler(commands=['eval'])
async def process_eval_command(message: types.Message, command: Command):
    await message.reply(f"По моим подсчетам {calc_main(command.args)}")

@dp.message_handler(commands=['fun'])
async def process_fun_command(message: types.Message):
    await message.reply(f'''Есть шутки: /joke\nЕсть котики: /cat\n''')

@dp.message_handler(commands=['joke'])
async def process_joke_command(message: types.Message):
    await message.reply(joke())  

@dp.message_handler(commands=['cat'])
async def process_cat_command(message: types.Message):
    image = cat()
    await bot.send_photo(message.chat.id, image )

@dp.message_handler(commands=['yn_ann'])
async def process_yn_ann_command(message: types.Message):
    await message.reply(f'''Не знаешь, делать что-то или нет? Задай вопрос! Я скину гифку с ответом: /Yes_No''')

@dp.message_handler(commands=['Yes_No'])
async def process_yesno_command(message: types.Message):
    image = yesno()
    await bot.send_document(message.chat.id, image)

@dp.message_handler(commands=['best'])
async def proces_best_command(message: types.Message):
    video = 'https://youtu.be/dQw4w9WgXcQ'
    await bot.send_message(message.chat.id, video )

if __name__ == '__main__':
    executor.start_polling(dp)