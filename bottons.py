from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = [
    [KeyboardButton(text="Login"), KeyboardButton(text="Register")]
]

menu_key = ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True)

BtnGen = [
    [KeyboardButton(text="Male"), KeyboardButton(text="Female")]
]
gen_key = ReplyKeyboardMarkup(keyboard=BtnGen, resize_keyboard=True)
