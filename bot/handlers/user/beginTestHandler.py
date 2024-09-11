from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from data.test_chooser import test_chooser
from states.TestState import TestState
from keyboards.inline.testKeyboard import test_buttons
from loader import dp

@dp.callback_query(lambda query: query.data.startswith('beginTest'))
async def beginTest(query: CallbackQuery, state: FSMContext):
    await query.answer(cache_time=10)
    lang = query.data.split(':')[1]
    level = query.data.split(':')[2]
    count = query.data.split(':')[3]
    if lang == "TR" and level == "A1" and (count == "10" or count == "20"):
        tests = test_chooser(lang, level, count)
        test = tests[0]
        await query.message.answer(
            text=test["question"],
            reply_markup=test_buttons(test)
        )
        await state.set_state(TestState.index)
        await state.update_data(test=tests, index=1, correct=0, count=int(count))
    else:
        await query.message.answer("Bazamizda hali testlar yetarli emas!😕")


@dp.callback_query(TestState.index, lambda query: query.data.startswith('test'))
async def testHandler(query: CallbackQuery, state: FSMContext):
    await query.answer(cache_time=10)
    option = query.data.split(':')[1]
    answer = query.data.split(':')[2]

    data = await state.get_data()
    index = data['index']
    test = data['test']
    correct = data['correct']
    count = data['count']

    prev_test = f"{test[index-1]['question']}\n\n"
    for p_option in test[index-1]['options']:
        prev_test += f"{p_option}"
        if p_option == answer:
            prev_test += "✅"
        elif p_option == option:
            prev_test += "❌"
        prev_test += "\n"
    await query.message.edit_text(prev_test)

    if option == answer:
        correct += 1

    if index < count:
        await query.message.answer(
            text=test[index]["question"],
            reply_markup=test_buttons(test[index])
        )
        index += 1
        await state.set_state(TestState.index)
        await state.update_data(index=index, correct=correct)
    else:
        response = (f"Test yakunlandi!\n"
                    f"\nJami testlar soni: {count}\n"
                    f"To'g'ri javoblar soni: {correct}\n"
                    f"Noto'g'ri javoblar soni: {count-correct}\n"
                    f"\nQaytadan test yechasizmi?")
        await query.message.answer(
            text=response,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Test yechish✅",
                            callback_data="start_test"
                        )
                    ]
                ]
            )
        )






