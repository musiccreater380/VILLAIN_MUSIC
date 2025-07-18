from pyrogram.types import InlineKeyboardButton

import config
from VILLAIN_MUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["https://t.me/TheSuportChat"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["7973954776"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_7"], callback_data="gib_source"),
            InlineKeyboardButton(text=_["https://t.me/SexyNayak"], url=config.SUPPORT_CHANNEL),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
    ]
    return buttons
