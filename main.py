import os
import asyncio
import logging
from form import Form
from dotenv import load_dotenv
from bottons import gen_key, menu_key
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart, Command

load_dotenv()
Channel_id = os.getenv("CHANNEL")
bot = Bot(os.getenv("B_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(f"Welcome! {msg.from_user.full_name}", reply_markup=menu_key)


@dp.message(F.text == "Register")
async def registers(msg: Message, state: FSMContext):
    await state.set_state(Form.name)
    await msg.answer(text="Enter your name:", reply_markup=ReplyKeyboardRemove())


@dp.message(Form.name)
async def name_func(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Form.age)
    await msg.answer(text="Enter your age:")


@dp.message(Form.age)
async def genders(msg: Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await state.set_state(Form.gender)
    await msg.answer("Your gender is:", reply_markup=gen_key)


@dp.message(Form.gender)
async def birthdays(msg: Message, state: FSMContext):
    await state.update_data(gender=msg.text)
    await state.set_state(Form.birthday)
    await msg.answer(text="Enter your birthday:", reply_markup=ReplyKeyboardRemove())


@dp.message(Form.birthday)
async def passwords(msg: Message, state: FSMContext):
    await state.update_data(birthday=msg.text)
    await state.set_state(Form.password)
    await msg.answer("Your password is:")


@dp.message(Form.password)
async def finishes(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    await state.set_state(Form.finish)
    data = await state.get_data()
    await state.clear()
    await message.answer("Register Done ! ✅")
    name = data.get("name", "Unknown")
    age = data.get("age", "Unknown")
    gender = data.get("gender", "Unknown")
    birthday = data.get("birthday", "Unknown")
    password = data.get("password", "Unknown")

    text = f"Your data is now saved !\nName: {name}, \nAge: {age}, \nGender:{gender}, \nBirthday: {birthday}, \nPassword: {password} "

    await message.answer(text)
    await bot.send_message(chat_id=Channel_id, text=text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
