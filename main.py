import logging

import checkWord

from transliterate import to_cyrillic, to_latin

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5124349048:AAH8VganUO34dzNaLKrdvHABvbmABTx4BtU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\nBotga xush kelibsiz!"
                        "\nBu botda siz so'zlar imlosini ko'rishingiz mumkin.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z jo'nating!")


@dp.message_handler()
async def imloLugat(message: types.Message):
    words = message.text.split()
    if len(words) == 1:
        word = message.text
        answers = checkWord.checkWord(word.lower())
        if answers.get('available'):
            output = '✅' + word.capitalize()
        else:
            output = f"❌ {word.capitalize()}\n"
            for text in answers.get('matches'):
                output += f"✅ {text.capitalize()}\n"
        await message.answer(output)

    else:
        for word in words:
            answers = checkWord.checkWord(word.lower())
            if answers.get('available'):
                output = '✅ ' + word.capitalize()
            else:
                output = f"❌ {word.capitalize()}\n"
                for text in answers.get('matches'):
                    output += f"✅ {text}\n"
            await message.answer(output)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
