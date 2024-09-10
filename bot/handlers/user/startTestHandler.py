from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from states.testConfig import TestConfigState
from keyboards.inline.testConfigKeyboard import langsButton, levelsButton, countsButton
from loader import dp

LANGUAGES = {
    "UZ": "O'zbek",
    "TR": "Turkcha",
    "EN": "Inglizcha",
}


@dp.callback_query(lambda query: query.data == 'start_test')
async def startTest(query: CallbackQuery, state: FSMContext):
    await query.answer(cache_time=10)
    await state.set_state(TestConfigState.lang)
    await query.message.answer(
        text=f"Qaysi tilda test yechamiz, {query.from_user.full_name}",
        reply_markup=langsButton
    )


@dp.callback_query(TestConfigState.lang, lambda query: query.data.startswith('lang'))
async def langChoice(query: CallbackQuery, state: FSMContext):
    await query.answer(cache_time=10)
    lang_code = query.data.split(':')[1]
    await state.update_data(lang=lang_code)
    await query.message.edit_text("Test darajasini tanlang:", reply_markup=levelsButton)
    await state.set_state(TestConfigState.level)


@dp.callback_query(TestConfigState.level, lambda query: query.data.startswith('level'))
async def levelChoice(query: CallbackQuery, state: FSMContext):
    await query.answer(cache_time=10)
    level = query.data.split(':')[1]
    await state.update_data(level=level)
    await query.message.edit_text("Testlar sonini tanlang:", reply_markup=countsButton)
    await state.set_state(TestConfigState.count)


@dp.callback_query(TestConfigState.count, lambda query: query.data.startswith('count'))
async def countChoice(query: CallbackQuery, state: FSMContext):
    await query.answer(cache_time=10)
    count = query.data.split(':')[1]
    await state.update_data(count=count)
    data = await state.get_data()
    lang = data['lang']
    await state.clear()
    response = (f"✅Tushunarli, {query.from_user.full_name}\n\n"
                f"🌐Til: {LANGUAGES[lang]}\n"
                f"📊Daraja: {data['level']}\n"
                f"🔢Testlar soni: {data['count']}\n"
                f"\nTestni boshlaysizmi ...")
    await query.message.edit_text(
        text=response,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Boshlash✅",
                        callback_data=f"beginTest:{data['lang']}:{data['level']}:{data['count']}"
                    )
                ]
            ]
        )
    )
