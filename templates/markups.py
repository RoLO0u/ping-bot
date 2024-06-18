# -*- coding: utf-8 -*-

import random

from templates.const import CAPTCHA_CAPTIONS

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def captcha_inline() -> InlineKeyboardMarkup:
    random_capts = [(key, CAPTCHA_CAPTIONS[key]) for key in list(CAPTCHA_CAPTIONS.keys())]
    random.shuffle(random_capts)
    random_capts = dict(random_capts)
    listed_markup = [InlineKeyboardButton(text=capt, callback_data=random_capts[capt]) for capt in random_capts]
    listed_markup = [listed_markup[:3], listed_markup[3:]]
    return InlineKeyboardMarkup(inline_keyboard=listed_markup)