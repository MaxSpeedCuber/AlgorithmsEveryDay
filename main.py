import logging
from aiogram.types import ContentType
import config
from db import Database
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, f"Привет! Я - <a href='https://t.me/maxspeedcuber'>MaxSpeedCuber</a>, и я создал этого бота, для того, чтобы Вы смогли учить алгоритмы в спокойном темпе(по 5-6 в день). В ближайшее время будут CLL алгоритмы.Воспользуйтесь командой /maintenance, если Вы захотите поддержать <a href='https://t.me/maxspeedcuber'>создателя</a> этого бота.", parse_mode='html')
@dp.message_handler(commands=['rassilochkaotbota'])
async def rassilka(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5030790426:
            text = message.text[19:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, "Успешная рассылка")
hundred = types.LabeledPrice(label="Поддержать MaxSpeedCuber 100 рублей", amount=10000)
two = types.LabeledPrice(label="Поддержать MaxSpeedCuber 200 рублей", amount=20000)
five = types.LabeledPrice(label="Поддержать MaxSpeedCuber 500 рублей", amount=50000)
thousand = types.LabeledPrice(label="Поддержать MaxSpeedCuber 1000 рублей", amount=100000)
twothousand = types.LabeledPrice(label="Поддержать MaxSpeedCuber 2000 рублей", amount=200000)
@dp.message_handler(commands=['maintenance'])
async def maintenance(message: types.Message):
    await bot.send_message(message.chat.id, f"\n/buy1 - поддержать мой канал 100 рублей"
                         f"\n/buy2 - поддержать мой канал 200 рублей"
                         f"\n/buy5 - поддержать мой канал 500 рублей"
                         f"\n/buy10 - поддержать мой канал 1000 рублей"
                         f"\n/buy20 - поддержать мой канал 2000 рублей")


@dp.message_handler(commands=['buy1'])
async def buy1(message: types.Message):
    if config.payment.split(":")[1] == 'TEST':
        await bot.send_message(message.chat.id, "Поддержка канала MaxSpeedCuber")
    await bot.send_invoice(message.chat.id,
                           title="Поддержать меня 100 рублей",
                           description="Спасибо, дорогой друг! Я очень рад, что тебя радует мой контент, и ты захотел его поддержать. Спасибо тебе огромное!!!",
                           provider_token=config.payment,
                           currency="rub",
                           photo_url="https://ruwix.com/pics/rubiks-cube-patterns/twisty-puzzles/iloveyou-pattern-7.png",
                           photo_width=300,
                           photo_height=300,
                           photo_size=300,
                           is_flexible=False,
                           prices=[hundred],
                           start_parameter="one-time-payment",
                           payload="test-invoice-payload")


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_chekout_query(pre_chekout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_chekout_q.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT: ")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id, f"""Спасибо тебе огромное!! Платёж прошёл успешно, ты поддержал меня {message.successful_payment.total_amount // 100} рублями! Ты самый лучший! Я буду стараться делать самый лучший контент для тебя!\n\n\n\nТак же ты вступаешь в <b><a href="https://t.me/+2hy-xNV0YCdlNDky">чат со мной лично</a></b>""", parse_mode="html")










@dp.message_handler(commands=['buy2'])
async def buy2(message: types.Message):
    if config.payment.split(":")[1] == 'TEST':
        await bot.send_message(message.chat.id, "Поддержка канала MaxSpeedCuber")
    await bot.send_invoice(message.chat.id,
                           title="Поддержать меня 200 рублей",
                           description="Спасибо, дорогой друг! Я очень рад, что тебя радует мой контент, и ты захотел его поддержать. Спасибо тебе огромное!!!",
                           provider_token=config.payment,
                           currency="rub",
                           photo_url="https://ruwix.com/pics/rubiks-cube-patterns/twisty-puzzles/iloveyou-pattern-7.png",
                           photo_width=300,
                           photo_height=300,
                           photo_size=300,
                           is_flexible=False,
                           prices=[two],
                           start_parameter="one-time-payment",
                           payload="test-invoice-payload")




@dp.pre_checkout_query_handler(lambda query: True)
async def pre_chekout_query(pre_chekout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_chekout_q.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT: ")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id, f"""Спасибо тебе огромное!! Платёж прошёл успешно, ты поддержал меня {message.successful_payment.total_amount // 100} рублями! Ты самый лучший! Я буду стараться делать самый лучший контент для тебя!\n\n\n\nТак же ты вступаешь в <b><a href="https://t.me/+2hy-xNV0YCdlNDky">чат со мной лично</a></b>""", parse_mode="html")



@dp.message_handler(commands=['buy5'])
async def buy3(message: types.Message):
    if config.payment.split(":")[1] == 'TEST':
        await bot.send_message(message.chat.id, "Поддержка канала MaxSpeedCuber")
    await bot.send_invoice(message.chat.id,
                           title="Поддержать меня 500 рублей",
                           description="Спасибо, дорогой друг! Я очень рад, что тебя радует мой контент, и ты захотел его поддержать. Спасибо тебе огромное!!!",
                           provider_token=config.payment,
                           currency="rub",
                           photo_url="https://ruwix.com/pics/rubiks-cube-patterns/twisty-puzzles/iloveyou-pattern-7.png",
                           photo_width=300,
                           photo_height=300,
                           photo_size=300,
                           is_flexible=False,
                           prices=[five],
                           start_parameter="one-time-payment",
                           payload="test-invoice-payload")



@dp.pre_checkout_query_handler(lambda query: True)
async def pre_chekout_query(pre_chekout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_chekout_q.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT: ")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id, f"""Спасибо тебе огромное!! Платёж прошёл успешно, ты поддержал меня {message.successful_payment.total_amount // 100} рублями! Ты самый лучший! Я буду стараться делать самый лучший контент для тебя!\n\n\n\nТак же ты вступаешь в <b><a href="https://t.me/+2hy-xNV0YCdlNDky">чат со мной лично</a></b>""", parse_mode="html")


@dp.message_handler(commands=['buy10'])
async def buy10(message: types.Message):
    if config.payment.split(":")[1] == 'TEST':
        await bot.send_message(message.chat.id, "Поддержка канала MaxSpeedCuber")
    await bot.send_invoice(message.chat.id,
                           title="Поддержать меня 1000 рублей",
                           description="Спасибо, дорогой друг! Я очень рад, что тебя радует мой контент, и ты захотел его поддержать. Спасибо тебе огромное!!!",
                           provider_token=config.payment,
                           currency="rub",
                           photo_url="https://ruwix.com/pics/rubiks-cube-patterns/twisty-puzzles/iloveyou-pattern-7.png",
                           photo_width=300,
                           photo_height=300,
                           photo_size=300,
                           is_flexible=False,
                           prices=[thousand],
                           start_parameter="one-time-payment",
                           payload="test-invoice-payload")



@dp.pre_checkout_query_handler(lambda query: True)
async def pre_chekout_query(pre_chekout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_chekout_q.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT: ")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id, f"""Спасибо тебе огромное!! Платёж прошёл успешно, ты поддержал меня {message.successful_payment.total_amount // 100} рублей! Ты самый лучший! Я буду стараться делать самый лучший контент для тебя!\n\n\n\nТак же ты вступаешь в <b><a href="https://t.me/+2hy-xNV0YCdlNDky">чат со мной лично</a></b>""", parse_mode="html")




@dp.message_handler(commands=['buy20'])
async def buy20(message: types.Message):
    if config.payment.split(":")[1] == 'TEST':
        await bot.send_message(message.chat.id, "Поддержка канала MaxSpeedCuber")
    await bot.send_invoice(message.chat.id,
                           title="Поддержать меня 2000 рублей",
                           description="Спасибо, дорогой друг! Я очень рад, что тебя радует мой контент, и ты захотел его поддержать. Спасибо тебе огромное!!!",
                           provider_token=config.payment,
                           currency="rub",
                           photo_url="https://ruwix.com/pics/rubiks-cube-patterns/twisty-puzzles/iloveyou-pattern-7.png",
                           photo_width=300,
                           photo_height=300,
                           photo_size=300,
                           is_flexible=False,
                           prices=[twothousand],
                           start_parameter="one-time-payment",
                           payload="test-invoice-payload")







@dp.pre_checkout_query_handler(lambda query: True)
async def pre_chekout_query(pre_chekout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_chekout_q.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT: ")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    await bot.send_message(message.chat.id, f"""Спасибо тебе огромное!! Платёж прошёл успешно, ты поддержал меня {message.successful_payment.total_amount // 100} рублей! Ты самый лучший! Я буду стараться делать самый лучший контент для тебя!\n\n\n\nТак же ты вступаешь в <b><a href="https://t.me/+2hy-xNV0YCdlNDky">чат со мной лично</a></b>""", parse_mode="html")
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)