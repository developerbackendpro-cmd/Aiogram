import re
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, BotCommand

API_TOKEN = '8023296312:AAFZvasvkaPKwvmfkPHXf5Q7AmoDaJLSvNg'

admission = True

YOUTUBE = 'https://www.youtube.com/watch?v=5oQ8y5itE-c'
INSTAGRAM = 'https://www.instagram.com/thompsonmaktablari.uz/'
TELEGRAM = 'https://t.me/thompson_maktablari'
LOCATION = 'https://maps.app.goo.gl/tpcktv1jTbBnBQM67'
PHONE = '+99893-123-45-67'
LATITUDE = 41.357974
LONGITUDE = 69.23971
CHAT_ID = 833921061

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class LanguageState(StatesGroup):
    language = State()

class Contact(StatesGroup):
    name = State()
    phone = State()
    message = State()

class Work(StatesGroup):
    full_name = State()
    phone = State()
    cv = State()


class Admission(StatesGroup):
    full_name_ad = State()
    phone_ad = State()
    region_ad = State()
    classes_ad = State()

async def on_startup(dp):
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/info", description="Umumiy ma'lumot"),
        BotCommand(command="/location", description="Bizning manzil"),
        BotCommand(command="/price", description="Narhlar haqida ma'lumot"),
        BotCommand(command="/advantage", description="Maktab afzaliklari"),
        BotCommand(command="/contact", description="Biz bilan bo'lanish"),
        BotCommand(command="/work", description="Ish bo'yicha"),
    ])

@dp.message_handler(lambda message: message.text in ["🇷🇺 Русский", "🇺🇿 O'zbekcha"], state='*')
async def handle_language_selection(message: types.Message, state: FSMContext):
    if message.text == "🇷🇺 Русский":
        await state.update_data(language="ru")
    elif message.text == "🇺🇿 O'zbekcha":
        await state.update_data(language="uz")
    await start(message, state)

@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    admission = True
    if select__language == "ru":
        keyboard.add(
            types.KeyboardButton("🌟 Общая информация"),
            types.KeyboardButton("📍 Наш адрес"),
        )
        keyboard.add(
            types.KeyboardButton("💰 Наши цены"),
            types.KeyboardButton("🎉 Преимущества школы"),
        )
        keyboard.add(
            types.KeyboardButton("👨‍💻 Работа"),
            types.KeyboardButton("📞 Связаться с нами"),
        )
        if admission == True:
            keyboard.add(
                types.KeyboardButton("📚 Прием в школу"),
            )
        keyboard.add(
            types.KeyboardButton("🇷🇺 Русский"),
            types.KeyboardButton("🇺🇿 O'zbekcha"),
        )
        await message.answer("<blockquote>Здравствуйте, пожалуйста, выберите один из следующих вариантов для более быстрого получения информации по вашему вопросу:</blockquote>", parse_mode=types.ParseMode.HTML, reply_markup=keyboard)
    else:
        keyboard.add(
            types.KeyboardButton("🌟 Umumiy ma'lumot"),
            types.KeyboardButton("📍 Manzilimiz"),
        )
        keyboard.add(
            types.KeyboardButton("💰 Narxlarimiz"),
            types.KeyboardButton("🎉 Maktab afzalliklari"),
        )
        keyboard.add(
            types.KeyboardButton("👨‍💻 Ish bo'yicha"),
            types.KeyboardButton("📞 Biz bilan bog'lnaish"),
        )
        if admission == True:
            keyboard.add(
                types.KeyboardButton("📚 Maktabga qabul"),
            )
        keyboard.add(
            types.KeyboardButton("🇷🇺 Русский"),
            types.KeyboardButton("🇺🇿 O'zbekcha"),
        )
        await message.answer("<blockquote>Assalomu alaykum, savolingiz bo'yicha tezroq ma'lumot olish uchun quyidagilardan birini tanlang:</blockquote>",  parse_mode=types.ParseMode.HTML, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ["🌟 Общая информация", "🌟 Umumiy ma'lumot"], state='*')
async def all_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    if select__language == "ru":
        await message.answer(f"<blockquote><b>🏫 Школа Thompson принимает учеников с 1 по 11 класс.</b></blockquote>\n\n⏰ График работы школы: с 8:00 до 16:00. / 5 дней\n\n🎯 Все предметы проводятся углубленно! \n\n📚 <b>Языкоориентированные уроки</b>\n🇬🇧 Английский язык\n🇷🇺 Русский язык\n🇨🇳 Китайский язык\n🇹🇷 Турецкий язык\n🇰🇷 Корейский язык\n🇸🇦 Арабский язык\n\n ✅ <b>Дополнительный</b>\n\n🙍‍♂️ Для мальчиков:\n🥋 Таеквандо\n⚽️ Футбол\n🎾 Теннисный корт\n🏇🏻 Верховая езда\n🏊🏻 Бассейн\n🏹 Стрельба из лука\n💻 Киберспорт\n\n🙎‍♀️ Для девочек:\n👩🏻‍⚕️ Медицинский курс\n👩🏻‍🍳 Курс национальной и европейской кухни\n🧵 Пошив одежды\n🖌️ Курс дизайна\n🦋 Курс этики и эстетики\n🧕🏼 Курс психологии\n🤸🏻 Гимнастика\n\n📙 Общий:\n📱 СММ (Мобилография)\n🎾 Теннис\n🏀 Баскетбол\n🏐 Волейбол\n📝 Архитектура\n🧑🏻‍💻 ИТ-программирование\n🧮 Бухгалтерский учет (Аудит)\n🏁 Шахматы и шашки\n🤖 Робототехника\n🚛 Логистика\n\n<blockquote>🏢 Наша школа – это процветающее учебное заведение, в котором учатся более 400 учеников, и наша учебная программа разработана так, чтобы предлагать широкий спектр предметов и навыков, чтобы обеспечить всестороннюю подготовку учащихся</blockquote>\n<blockquote>🍛 Кухня призвана предлагать здоровую, халяльную еду, чтобы поддержать концентрацию учащихся и уровень энергии в течение дня</blockquote>\n<blockquote>🗞 Большинство наших выпускников поступили в ТОП университеты мира с результатами IELTS 7-7,5</blockquote>\n<b>📌 Дополнительной информации:</b>\n☎️ {PHONE} 📍 <a href='{LOCATION}' style='color: red;'>Наш адрес</a>\n\n🔗 <b>Страницы в социальных сетях</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>\n", parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f"<blockquote><b>🏫 Thompson School maktabi 1-sinfdan 11-sinfgacha bo'lgan o'quvchilarni qabul qiladi</b></blockquote>\n\n⏰  Maktab soatlari: 8:00 dan 16:00 gacha / 5 kun\n\n🎯 Barcha fanlar chuqurlashtirilgan tarzda olib boriladi \n\n📚 <b>Tilga yo'naltirilgan darslarimiz</b>\n🇬🇧 Ingliz tili\n🇷🇺 Rus tili\n🇨🇳 Xitoy tili\n🇹🇷 Turk tili\n🇰🇷 Koreys tili\n🇸🇦 Arab tili\n\n ✅ <b>Qo'shimcha</b>\n\n🙍‍♂️ O'g'il bolalar uchun:\n🥋 Taekwondo\n⚽️ Futbo’l\n🎾 Tenis ko’rt\n🏇🏻 Ot minish\n🏊🏻 Bassen suv havzasi\n🏹 Kamondan oʻq otish\n💻 Kiber sport\n\n🙎‍♀️ Qizlar uchun:\n👩🏻‍⚕️ Tibbiyot kursi\n👩🏻‍🍳 Milliy va yevropa taomlari\n🧵 Tikuvchilik\n🖌️ Dizaynerlik\n🦋 Etika va Estetika\n🧕🏼 Psixologiya\n🤸🏻 Gimnastika\n\n📙 Umumiy:\n📱 SMM(Mobilografia)\n🎾 Tenis ko’rt\n🏀 Basketbo’l\n🏐 Valebo’l\n📝 Arxitektura\n🧑🏻‍💻 IT Dasturlash\n🧮 Buxgalteriya(Audit)\n🏁 Shaxmat Shashka\n🤖 Robototexnika\n🚛 Logistika\n\n<blockquote>🏢 Bizning maktab 400 dan ortiq o'quvchilarga ega bo'lgan rivojlanayotgan ta'lim muassasasi bo'lib, Bizning o'quv dasturimiz o'quvchilarning har tomonlama ta'lim olishlarini ta'minlaydigan keng ko'lamli fanlar va ko'nikmalarni taklif qilishga mo'ljallangan</blockquote>\n<blockquote>🍛 Oshxona kun davomida o'quvchilarning konsentratsiyasi va energiya darajasini qo'llab-quvvatlash uchun sog'lom, halol, oziq-ovqat tanlovlarini taklif qilishni maqsad qilgan</blockquote>\n<blockquote>🗞 Bitiruvchilarimizning aksari IELTS 7-7.5 natija ko'rsatib dunyoning TOP universitetlariga kirishdi</blockquote>\n<b>📌 Batafsil ma’lumot uchun:</b>\n☎️ {PHONE} 📍 <a href='{LOCATION}' style='color: red;'>Manzil</a>\n\n🔗 <b>Ijtimoiy tarmoqdagi sahifalarimiz</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>\n", parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text in ["📍 Наш адрес", "📍 Manzilimiz"], state='*')
async def location(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    if select__language == 'ru':
        await message.answer(f"<blockquote><b>Наша школа расположена в Алмазорском районе города Ташкента</b>\n<b>Место назначения: ул. Фараби, 259</b></blockquote>\n📌 <b>Дополнительной информации:</b>\n☎️ {PHONE} | <a href='{LOCATION}'>📍 Наш адрес</a>\n\n🔗 <b>Страницы в социальных сетях</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>", parse_mode=types.ParseMode.HTML)
        await message.bot.send_location(chat_id=message.chat.id, latitude=LATITUDE, longitude=LONGITUDE)
    else:
        await message.answer(f"<blockquote><b>Maktabimiz Toshkent shahrining Olmazor tumanida joylashgan</b>\n<b>Mo’ljal: Farobiy koʻchasi 259-uy</b></blockquote>\n📌 <b>Batafsil ma’lumot uchun:</b>\n☎️ {PHONE} | <a href='{LOCATION}'>📍 Manzil</a>\n\n🔗 <b>Ijtimoiy tarmoqdagi sahifalarimiz</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>", parse_mode=types.ParseMode.HTML)
        await message.bot.send_location(chat_id=message.chat.id, latitude=LATITUDE, longitude=LONGITUDE)

@dp.message_handler(lambda message: message.text in ["💰 Наши цены", "💰 Narxlarimiz"], state='*')
async def price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    if select__language == 'ru':
        await message.answer(f"<blockquote><b>Стоимость ежемесячной оплаты:</b>\n• 4 700 000 сум для начальных классов\n• Для высших классов – 4 900 000 сумов\n\n❗️ Наша школа предлагает различные скидки, чтобы сделать обучение более удобным. В нашей школе действуют скидки до 5%, 10% и 15%. Наши скидки составляют 5% от абонентской платы, если из 1 семьи приезжают 2 ребенка. А при оплате раз в полгода (независимо от того, сколько детей) действует скидка 10 процентов. При наличии 3 и более детей из 1 семьи действует скидка 15%</blockquote>\n📌 <b>Дополнительной информации:</b>\n☎️ {PHONE} | <a href='{LOCATION}'>📍 Наш адрес</a>\n\n🔗 <b>Страницы в социальных сетях</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>", parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f"<blockquote><b>Oylik to’lov narxlari:</b>\n• Boshlang'ich sinflar uchun 4,700,000 so'm\n• Yuqori sinflar uchun esa 4,900,000 so’mni tashkil qiladi\n\n❗️ Maktabimiz ta'limni yanada qulay qilish uchun turli chegirmalar taklif qilmoqda. Bizning maktabda 5 foiz, 10 foiz va 15 foizgacha chegirmalar bor Chegirmalarimiz, agar 1 ta oiladan 2 farzand keladigan bo'lsa, oylik to'lovdan 5 foizga chegirmasi bor. Va yarim yillik tol'ov amalga oshirilsa 10 foiz chegirma bo'ladi (nechta farzand bo'lishidan qat'iy nazar). Agarda 1 ta oiladan, 3 yoki undan ortiqroq farzand keladigan bo'lsa, 15 foizgacha chegirma bor</blockquote>\n📌 <b>Batafsil ma’lumot uchun:</b>\n☎️ {PHONE} | <a href='{LOCATION}'>📍 Manzil</a>\n\n🔗 <b>Ijtimoiy tarmoqdagi sahifalarimiz</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text in ["🎉 Преимущества школы", "🎉 Maktab afzalliklari"], state='*')
async def advantage(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    if select__language == "ru":
        await message.answer(f"<b>Основные сильные стороны нашей школы\n\nНашу школу отличает ориентация на десять важных направлений:</b>\n\n<blockquote><b>1 • Здание и сооружения</b>\nИнфраструктура школы тщательно спроектирована для создания оптимальной образовательной среды. Учебные классы светлые, хорошо проветриваемые и оснащены современным оборудованием. В здании есть полностью оборудованный спортивный зал, многофункциональный зал для занятий, стадион, специализированные лаборатории, технологический центр, просторный внутренний двор и зеленый сад\n\n<b>2 • Преподавательский состав</b>\nНаши преподаватели отобраны из более чем 2000 кандидатов и представляют собой лучших специалистов в своих областях. Они проходят строгий отборочный процесс, где оцениваются их опыт, знания и педагогические навыки. Мы поощряем непрерывное профессиональное развитие, и большинство наших учителей регулярно участвуют в программах повышения квалификации.\n\n<b>3 • Отбор учеников</b>\nМы поддерживаем высокий академический стандарт, принимая учеников на основе собеседования. За исключением учеников 1-4 классов, все школьники должны пройти строгий вступительный экзамен. Также мы подчеркиваем важность участия родителей в процессе отбора для обеспечения поддерживающей учебной среды\n\n<b>4 • Комплексная учебная программа</b>\nНаша учебная программа не только соответствует государственным образовательным требованиям, но и включает дополнительные программы для обогащения учебного опыта учеников. Международно признанная программа Оксфорда дополняет изучение английского языка, а расширенные учебные программы, такие как программы Петерсона и Рамзаевой, внедряются на начальных этапах\n\n<b>5 • Внеклассные программы</b>\nМы предлагаем широкий спектр внеклассных мероприятий, направленных на развитие интересов и талантов учеников. В наши кружки входят направления такие как: «SMM (Мобилография)», «Бухгалтерия (Аудит)», «Логистика», «Архитектура», «Робототехника», «Информационные технологии», «Шахматы», «Гимнастика», «Тхэквондо», «Айкидо», «Кулинария», «Физическая культура», а также изучение языков (русского, английского, китайского, корейского, турецкого и арабского)\n\n<b>6 • Качественное питание</b>\nШкольная столовая управляется опытными поварами, что обеспечивает сбалансированное и питательное питание учеников в течение дня. Программа питания включает в себя четырехразовое питание в день с акцентом на здоровые привычки питания и использование высококачественных ингредиентов\n\n<b>7 • Участие сообщества</b>\nМы активно сотрудничаем с родителями и местными организациями для поддержки развития наших учеников. Постоянные мероприятия, семинары и открытые форумы способствуют укреплению связи между школой и её сообществом\n\n<b>8 • Технологическое развитие</b>\nТехнологии глубоко интегрированы в наш образовательный подход. Учебные классы оснащены новейшим цифровым оборудованием, а ученики могут пользоваться современным информационно-технологическим центром. Мы ставим в приоритет цифровую грамотность и гарантируем, что наши ученики будут готовы к требованиям будущего в области технологий\n\n<b>9 • Безопасная среда</b>\nБезопасность наших учеников стоит на первом месте. Школа оснащена комплексными мерами безопасности, включая системы наблюдения и контролируемые точки входа. Наш персонал обучен поддерживать безопасную и поддерживающую среду для всех учеников\n\n<b>10 • Личностное развитие и поддержка</b>\nМы уделяем особое внимание личностному росту учеников, помогая им развивать уверенность в себе, стойкость и важные жизненные навыки. Регулярная обратная связь и индивидуальная поддержка обеспечивают получение каждым учеником необходимой мотивации и ресурсов для академического и личностного роста</blockquote>\n📌 <b>Дополнительной информации:</b>\n☎️ {PHONE} | <a href='{LOCATION}'>📍 Наш адрес</a>\n\n🔗 <b>Страницы в социальных сетях</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>", parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f"<b>Maktabimizning asosiy kuchli tomonlari\n\nBizning maktab o'nta muhim yo'nalishga qaratilganligi bilan ajralib turadi:</b>\n\n<blockquote><b>1 • Bino Inshootlari</b>\nMaktab infratuzilmasi optimal ta'lim muhitini yaratish uchun puxta ishlab chiqilgan. O‘quv xonalari yorug‘, havosi yaxshi, zamonaviy jihozlar bilan ta’minlangan. Binoda to‘liq jihozlangan sport zali, ko‘p funksiyali mashg‘ulotlar zali, sport stadioni, ixtisoslashtirilgan fan laboratoriyalari, texnologiya markazi, keng ochiq hovli va yam-yashil bog‘ mavjud.\n\n<b>2 • Maktab O'qtuvchilari</b>\nBizning professor-o'qituvchilar tarkibi 2000 dan ortiq nomzodlar orasidan tanlangan eng yaxshi mutaxassislardan iborat. Ularning tajribasi, fanlarni o'zlashtirishi va o'qituvchilik qobiliyatlari baholanadigan qattiq tanlov jarayonidan o'tadilar. Uzluksiz kasbiy o'sish rag'batlantiriladi, aksariyat o'qituvchilarimiz malaka oshirish dasturlarida muntazam qatnashadilar.\n\n<b>3 • O'quvchi Tanlo'vi</b>\nBiz O'quvchilarni savol-javov asosida qabul qilish orqali yuqori akademik standartlarni saqlab qolamiz. 1-4  sinf o'quvchilari bundan mustasno, barcha o'quvchilar qattiq kirish imtihonidan o'tishlari kerak. Shuningdek, biz qo'llab-quvvatlovchi o'quv muhitini ta'minlash uchun qabul jarayonida ota-onalarning ishtiroki muhimligini ta'kidlaymiz\n\n<b>4 • Kompleks o'quv dasturi</b>\nBizning o'quv dasturimiz nafaqat davlat ta'lim talablariga javob beradi, balki talabalarning o'rganish tajribasini boyitish uchun qo'shimcha dasturlarni ham o'z ichiga oladi. Xalqaro miqyosda tan olingan Oksford dasturi ingliz tilini o'qitishni to'ldiradi, Peterson va Ramzaeva dasturlari kabi kengaytirilgan o'quv dasturlari boshlang'ich bosqichda amalga oshiriladi\n\n<b>5 • Turli sinfdan tashqari dasturlar</b>\nBiz o‘quvchilarning qiziqish va iste’dodini rivojlantirishga qaratilgan keng ko‘lamli sinfdan tashqari tadbirlarni taklif etamiz. To‘garaklarimizda  “SMM(Mobilografia)”, “Buxgalteriya(Audit)”, “Logistika”, “Arxitektura”, “Robotexnika”, “Axborot texnologiyalari”, “Shaxmat”, “Gimnastika”, “Taekvondo”, “Aykido”, “Pazandachilik”, “Jismoniy tarbiya”, “Rus, Ingliz, Xtoy, Koreys, Turk va Arab tillarida til o‘rganish” kabi yo‘nalishlar mavjud\n\n<b>6 • Sifatli ovqatlanish</b>\nMaktab oshxonasi tajribali oshpazlar tomonidan boshqariladi, bu esa o‘quvchilarning kun davomida to‘yimli, muvozanatli ovqatlanishini ta’minlaydi. o‘quvchilar uchun kuniga 4 mahal ovqatlanishni o‘z ichiga olgan ovqatlanish dasturimiz sog‘lom ovqatlanish odatlari va yuqori sifatli ingredientlarga urg‘u beradi\n\n<b>7 • Jamiyat ishtiroki</b>\nO'quvchilarimizning rivojlanishini qo'llab-quvvatlash uchun ota-onalar va mahalliy tashkilotlar bilan faol hamkorlik qilamiz. Doimiy tadbirlar, seminarlar va ochiq forumlar maktab va uning jamoasi o'rtasidagi aloqani mustahkamlashga yordam beradi\n\n<b>8 • Texnologik taraqqiyot</b>\nTexnologiya bizning ta'lim yondashuvimizga chuqur integratsiyalashgan. O‘quv xonalari eng so‘nggi raqamli uskunalar bilan jihozlangan bo‘lib, talabalar zamonaviy axborot texnologiyalari xonasidan foydalanishlari mumkin. Biz raqamli savodxonlikni birinchi o'ringa qo'yamiz va o'quvchilarning kelajak texnologik talablariga yaxshi tayyorlanishini ta'minlaymiz\n\n<b>9 • Xavfsiz muhit</b>\nO'quvchilarimiz xavfsizligi birinchi o'rinda turadi. Maktab keng qamrovli xavfsizlik choralari, jumladan, kuzatuv tizimlari va boshqariladigan kirish nuqtalari bilan jihozlangan. Bizning xodimlarimiz barcha o'quvchilar uchun xavfsiz va qo'llab-quvvatlovchi muhitni saqlashga o'rgatilgan\n\n<b>10 • Shaxsiy rivojlanish va uni qo'llab-quvvatlash</b>\nBiz o‘quvchilarning shaxsiy o‘sishini ta’minlashga, ularga ishonch, chidamlilik va muhim hayotiy ko‘nikmalarni shakllantirishga yordam berishga e’tibor qaratamiz. Muntazam fikr-mulohazalar va moslashtirilgan yordam har bir o'quvchining akademik va shaxsiy rivojlanishi uchun zarur bo'lgan dalda va resurslarni olishini ta'minlaydi</blockquote>\n📌 <b>Batafsil ma’lumot uchun:</b>\n☎️ {PHONE} | <a href='{LOCATION}'>📍 Manzil</a>\n\n🔗 <b>Ijtimoiy tarmoqdagi sahifalarimiz</b>\n👉 <a href='{YOUTUBE}'>Youtube</a> | <a href='{INSTAGRAM}'>Instagram</a> | <a href='{TELEGRAM}'>Telegram</a>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text in ["📞 Связаться с нами", "📞 Biz bilan bog'lnaish"], state='*')
async def contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    if select__language == 'ru':
        await message.answer(f"<b>Введите свое имя, чтобы связаться с нами !</b>", parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f"<b>Biz bilan bog'lanish uchun ismingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
    await Contact.name.set()

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Contact.name)
async def contact_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == 'ru':
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['name'] = message.text
            await message.answer(f"<b>Введите свой номер телефона, чтобы связаться с нами\nФормат ввода знак + и 12 цифр</b>", parse_mode=types.ParseMode.HTML)
            await Contact.phone.set()
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде файла!</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде картинки !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде видео !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['name'] = message.text
            await message.answer(f"<b>Biz bilan bog'lanish uchun telefon raqamingizni kiriting\nKirish formati + belgisi va 12 raqam</b>", parse_mode=types.ParseMode.HTML)
            await Contact.phone.set()
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Xabaringizni fayil shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Xabaringizni rasim shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Xabaringizni video shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Contact.phone)
async def contact_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == 'ru':
        if message.content_type == types.ContentType.TEXT:
            phone_pattern = r'^\+\d{12}$'
            if re.match(phone_pattern, message.text):
                async with state.proxy() as data:
                    data['phone'] = message.text
                await message.answer(f"<b>Введите ваше сообщение и наши сотрудники свяжутся с вами !</b>", parse_mode=types.ParseMode.HTML)
                await Contact.message.set()
            else:
                await message.answer(f"<b>Формат ввода знак + и 12 цифр. Пожалуйста, введите снова !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде файла!</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде картинки !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде видео !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.TEXT:
            phone_pattern = r'^\+\d{12}$'
            if re.match(phone_pattern, message.text):
                async with state.proxy() as data:
                    data['phone'] = message.text
                await message.answer(f"<b>Xabaringizni kiriting xodimlarimiz siz bilan bog'lanishadi !</b>", parse_mode=types.ParseMode.HTML)
                await Contact.message.set()
            else:
                await message.answer(f"<b>Kirish formati + belgisi va 12 raqam. Iltimos, qaytadan kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Xabaringizni fayil shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Xabaringizni rasim shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Xabaringizni video shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Contact.message)
async def send_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == "ru":
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['message'] = message.text
            user_data = await state.get_data()
            phone_message = user_data.get('phone')
            contact_name = user_data.get('name')
            username = message.from_user.username
            if username:
                send_contact = f'{contact_name} - имя пользователя\n@{username} - профиль пользователя\n{phone_message} - номер телефона пользователя\n\n{message.text}'
            else:
                send_contact = f'{contact_name} - имя пользователя\n{phone_message} - номер телефона пользователя\n\n{message.text}'
            group_chat_id = CHAT_ID
            await bot.send_message(group_chat_id, f"<blockquote><b>{send_contact}</b></blockquote>", parse_mode=types.ParseMode.HTML)
            await message.answer(f"<b>Ваше сообщение успешно отправлено, спасибо !</b>", parse_mode=types.ParseMode.HTML)
            await state.reset_state(with_data=True)
            await state.update_data(language=select__language)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде файла!</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде картинки !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Не отправляйте свое сообщение в виде видео !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['message'] = message.text
            user_data = await state.get_data()
            phone_message = user_data.get('phone')
            contact_name = user_data.get('name')
            username = message.from_user.username
            if username:
                send_contact = f'{contact_name} - foydalanuvchi ismi\n@{username} - foydalanuvchi profili\n{phone_message} - foydalanuvchi telefon raqami\n\n{message.text}'
            else:
                send_contact = f'{contact_name} - foydalanuvchi ismi\n{phone_message} - foydalanuvchi telefon raqami\n\n{message.text}'
            group_chat_id = CHAT_ID
            await bot.send_message(group_chat_id, f"<blockquote><b>{send_contact}</b></blockquote>", parse_mode=types.ParseMode.HTML)
            await message.answer(f"<b>Xabaringiz muvaffaqiyatli yuborildi raxmat !</b>", parse_mode=types.ParseMode.HTML)
            await state.reset_state(with_data=True)
            await state.update_data(language=select__language)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Xabaringizni fayil shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Xabaringizni rasim shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Xabaringizni video shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text in ["👨‍💻 Работа", "👨‍💻 Ish bo'yicha"], state='*')
async def start_resume(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    if select__language == 'ru':
        await message.answer(f"<b>Для подачи заявки на вакансию введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f"<b>Ish bo'yicha hujjat topshirish uchun ism familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)
    await Work.full_name.set()

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Work.full_name)
async def work_to_full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == 'ru':
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['full_name'] = message.text
            await message.answer(f"<b>Введите свой номер для связи !</b>", parse_mode=types.ParseMode.HTML)
            await Work.phone.set()
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['full_name'] = message.text
            await message.answer(f"<b>Aloqaga chiqish uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
            await Work.phone.set()
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Isim familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Isim familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Isim familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Work.phone)
async def work_to_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == 'ru':
        if message.content_type == types.ContentType.TEXT:
            phone_pattern = r'^\+\d{12}$'
            if re.match(phone_pattern, message.text):
                async with state.proxy() as data:
                    data['phone'] = message.text
                await message.answer(f"<b>Загрузите свое резюме !</b>", parse_mode=types.ParseMode.HTML)
                await Work.cv.set()
            else:
                await message.answer(f"<b>Формат ввода знак + и 12 цифр. Пожалуйста, введите снова !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Введите свой номер, чтобы они могли связаться с вами !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Введите свой номер, чтобы они могли связаться с вами !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Введите свой номер, чтобы они могли связаться с вами !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.TEXT:
            phone_pattern = r'^\+\d{12}$'
            if re.match(phone_pattern, message.text):
                async with state.proxy() as data:
                    data['phone'] = message.text
                await message.answer(f"<b>Rezyumeni yuklang !</b>", parse_mode=types.ParseMode.HTML)
                await Work.cv.set()
            else:
                await message.answer(f"<b>Kirish formati + belgisi va 12 raqam. Iltimos, qaytadan kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Siz bilan bog'lanishlari uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Siz bilan bog'lanishlari uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Siz bilan bog'lanishlari uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Work.cv)
async def send_document(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == "ru":
        if message.content_type == types.ContentType.DOCUMENT:
            resume = message.document.mime_type
            if (resume == 'application/pdf' or resume == 'application/doc' or
                resume == 'application/docx' or resume == 'application/PDF' or
                resume == 'application/DOC' or resume == 'application/DOCX' or
                resume == 'image/jpg' or resume == 'image/jpeg' or
                resume == 'image/png' or resume == 'image/JPG' or
                resume == 'image/JPEG' or resume == 'image/PNG'
                ):
                await state.update_data(resume_id=message.document.file_id,)
                user_data = await state.get_data()
                username = message.from_user.username
                full_name = user_data.get('full_name')
                phone = user_data.get('phone')
                resume_id = user_data.get('resume_id')
                if username:
                    send_contact = f"{full_name} - Податель документа\n@{username} - Профиль пользователя\n{phone} - Номер телефона пользователя\n"
                else:
                    send_contact = f"{full_name} - Податель документа\n{phone} - Номер телефона пользователя\n"
                group_chat_id = CHAT_ID
                await bot.send_document(chat_id=group_chat_id, document=resume_id, caption=f"<blockquote><b>{send_contact}</b></blockquote>", parse_mode=types.ParseMode.HTML)
                await message.answer("<b>Документ успешно отправлен, спасибо !</b>", parse_mode=types.ParseMode.HTML)
                await state.reset_state(with_data=True)
                await state.update_data(language=select__language)
            else:
                await message.answer("<b>Файл в этом формате не принимаются ❌ \n\nПринимаются файл в формате pdf, doc, docx, jpg, jpeg, png ✅</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.TEXT:
            await message.answer(f"<b>Не вводите документ в текстовом виде !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Не отправляйте документ в виде изображения !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Не отправляйте документ в виде видео !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.DOCUMENT:
            resume = message.document.mime_type
            if (resume == 'application/pdf' or resume == 'application/doc' or
                resume == 'application/docx' or resume == 'application/PDF' or
                resume == 'application/DOC' or resume == 'application/DOCX' or
                resume == 'image/jpg' or resume == 'image/jpeg' or
                resume == 'image/png' or resume == 'image/JPG' or
                resume == 'image/JPEG' or resume == 'image/PNG'
                ):
                await state.update_data(resume_id=message.document.file_id,)
                user_data = await state.get_data()
                username = message.from_user.username
                full_name = user_data.get('full_name')
                phone = user_data.get('phone')
                resume_id = user_data.get('resume_id')
                if username:
                    send_contact = f"{full_name} - Hujjat topshiruvchi\n@{username} - Foydalanuvchi profili\n{phone} - Foydalanuvchi telefon raqami\n"
                else:
                    send_contact = f"{full_name} - Hujjat topshiruvchi\n{phone} - Foydalanuvchi telefon raqami\n"
                group_chat_id = CHAT_ID
                await bot.send_document(chat_id=group_chat_id, document=resume_id, caption=f"<blockquote><b>{send_contact}</b></blockquote>", parse_mode=types.ParseMode.HTML)
                await message.answer(f"Hujjat muvaffaqiyatli yuborildi raxmat !", parse_mode=types.ParseMode.HTML)
                await state.reset_state(with_data=True)
                await state.update_data(language=select__language)
            else:
                await message.answer("<b>Bunday farmatdagi fayillar qabul qilinmaydi ❌ \n\npdf, doc, docx, jpg, jpeg, png farmatdagi fayillar qabul qilinadi ✅</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.TEXT:
            await message.answer(f"<b>Hujjatingizni Matn shaklida kiritmang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Hujjatingizni rasim shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Hujjatingizni video shaklida yubormang !</b>", parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text in ["📚 Прием в школу", "📚 Maktabga qabul"])
async def admission(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
        await state.reset_state(with_data=True)
    await state.update_data(language=select__language)
    if select__language == 'ru':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Мирзо-Улугбекский район", callback_data='Мирзо-Улугбекский район'),
            InlineKeyboardButton("Юнусабадский район", callback_data='Yunusobod tumani'),
            InlineKeyboardButton("Кибрайский район", callback_data='Кибрайский район'),
            InlineKeyboardButton("Яшнабадский район", callback_data='Яшнабадский район'),
            InlineKeyboardButton("Мирабадский район", callback_data='Мирабадский район'),
            InlineKeyboardButton("Яккасарайский район", callback_data='Яккасарайский район'),
            InlineKeyboardButton("Чиланзорский район", callback_data='Чиланзорский район'),
            InlineKeyboardButton("Учтепинский район", callback_data='Учтепинский район'),
            InlineKeyboardButton("Алмазарский район", callback_data='Алмазарский район'),
            InlineKeyboardButton("Шайхонтохурский район", callback_data='Шайхонтохурский район'),
            InlineKeyboardButton("Сергелийский район", callback_data='Сергелийский район'),
            InlineKeyboardButton("Бектемирский район", callback_data='Бектемирский район'),
        )
        await message.answer("В каком районе вы проживаете ?", reply_markup=keyboard)
        await Admission.region_ad.set()
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Mirzo Ulugʻbek tumani", callback_data='Mirzo Ulugʻbek tumani'),
            InlineKeyboardButton("Yunusobod tumani", callback_data='Yunusobod tumani'),
            InlineKeyboardButton("Qibray tumani", callback_data=' Qibray tumani'),
            InlineKeyboardButton("Yashnabod tumani", callback_data='Yashnabod tumani'),
            InlineKeyboardButton("Mirobod tumani", callback_data='Mirobod tumani'),
            InlineKeyboardButton("Yakkasaroy tumani", callback_data='Yakkasaroy tumani'),
            InlineKeyboardButton("Chilonzor tumani", callback_data='Chilonzor tumani'),
            InlineKeyboardButton("Uchtepa tumani", callback_data='Uchtepa tumani'),
            InlineKeyboardButton("Olmazor tumani", callback_data='Olmazor tumani'),
            InlineKeyboardButton("Shayxontohur tumani", callback_data='Shayxontohur tumani'),
            InlineKeyboardButton("Sergeli tumani", callback_data='Sergeli tumani'),
            InlineKeyboardButton("Bektemir tumani", callback_data='Bektemir tumani'),
        )
        await message.answer("Qaysi tumanda istiqomat qilasiz ?", reply_markup=keyboard)
        await Admission.region_ad.set()

@dp.callback_query_handler(state=Admission.region_ad)
async def select_region(callback_query: types.CallbackQuery, state: FSMContext):
    region_name = callback_query.data
    await state.update_data(region_ad=region_name)
    await bot.answer_callback_query(callback_query.id)
    await admission_class(callback_query.message, state)

async def admission_class(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == 'ru':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Начальный класс", callback_data='Начальный класс'),
            InlineKeyboardButton("Старшие классы", callback_data='Старшие классы'),
        )
        await message.answer("В какой класс переходит ваш ребенок?", reply_markup=keyboard)
        await Admission.classes_ad.set()
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Boshlang’ich sinf", callback_data='Boshlang’ich sinf'),
            InlineKeyboardButton("Yuqori sinf", callback_data='Yuqori sinf'),
        )
        await message.answer("Farzandingiz qaysi sinfga oʻtkazmoqchisz ?", reply_markup=keyboard)
        await Admission.classes_ad.set()

@dp.callback_query_handler(state=Admission.classes_ad)
async def select_classes(callback_query: types.CallbackQuery, state: FSMContext):
    type_classes = callback_query.data
    await state.update_data(classes_ad=type_classes)
    await bot.answer_callback_query(callback_query.id)
    await start_adission(callback_query.message, state)

async def start_adission(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    await state.update_data(language=select__language)
    if select__language == 'ru':
        await message.answer(f"<b>Для приема введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f"<b>Qabul uchun ism familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)
        await Admission.full_name_ad.set()

@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Admission.full_name_ad)
async def admission_to_full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == 'ru':
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['full_name_ad'] = message.text
            await message.answer(f"<b>Введите свой номер для связи !</b>", parse_mode=types.ParseMode.HTML)
            await Admission.phone_ad.set()
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Введите полное имя и фамилию !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.TEXT:
            async with state.proxy() as data:
                data['full_name_ad'] = message.text
            await message.answer(f"<b>Aloqaga chiqish uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
            await Admission.phone_ad.set()
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Isim familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Isim familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Isim familya to'liq kiriting !</b>", parse_mode=types.ParseMode.HTML)


@dp.message_handler(content_types=[types.ContentType.TEXT, types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.VIDEO], state=Admission.phone_ad)
async def admission_to_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        select__language = data.get('language')
    if select__language == 'ru':
        if message.content_type == types.ContentType.TEXT:
            phone_pattern = r'^\+\d{12}$'
            if re.match(phone_pattern, message.text):
                async with state.proxy() as data:
                    data['phone_ad'] = message.text
                async with state.proxy() as data:
                    admission_full_name = data.get('full_name_ad')
                    admission_phone = data.get('phone_ad')
                    region_name = data.get('region_ad')
                    classes_name = data.get('classes_ad')
                username = message.from_user.username
                if username:
                    send_admission = f"{admission_full_name} - Для поступления в школу! заявитель\n@{username} - Профиль заявителя\n{admission_phone} - Телефон заявителя\n{region_name} - Регион, выбранный заявителем\n{classes_name} - Школьный класс, выбранный заявителем\n"
                else:
                    send_admission = f"{admission_full_name} - Для поступления в школу! заявитель\n{admission_phone} - Телефон заявителя\n{region_name} - Регион, выбранный заявителем\n{classes_name} - Школьный класс, выбранный заявителем\n"
                group_chat_id = CHAT_ID
                await bot.send_message(group_chat_id, f"<blockquote><b>{send_admission}</b></blockquote>", parse_mode=types.ParseMode.HTML)
                await message.answer(f"<b>Ваша заявка успешно отправлена, спасибо !</b>", parse_mode=types.ParseMode.HTML)
                await state.reset_state(with_data=True)
                await state.update_data(language=select__language)
            else:
                await message.answer(f"<b>Формат ввода знак + и 12 цифр. Пожалуйста, введите снова !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Введите свой номер, чтобы они могли связаться с вами !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Введите свой номер, чтобы они могли связаться с вами !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Введите свой номер, чтобы они могли связаться с вами !</b>", parse_mode=types.ParseMode.HTML)
    else:
        if message.content_type == types.ContentType.TEXT:
            phone_pattern = r'^\+\d{12}$'
            if re.match(phone_pattern, message.text):
                async with state.proxy() as data:
                    data['phone_ad'] = message.text
                async with state.proxy() as data:
                    admission_full_name = data.get('full_name_ad')
                    admission_phone = data.get('phone_ad')
                    admission_region = data.get('region_ad')
                    admission_classes = data.get('classes_ad')
                username = message.from_user.username
                if username:
                    send_admission = f'{admission_full_name} - Qabul uchun ariza qoldiruvchi\n@{username} - Arizachi profili\n{admission_phone} - Arizachi telefon raqami\n{admission_region} - Arizachi tanlagan hudud\n{admission_classes} - Arizachi tanlagan sinf\n'
                else:
                    send_admission = f'{admission_full_name} - Qabul uchun ariza qoldiruvchi\n{admission_phone} - Arizachi telefon raqami\n{admission_region} - Arizachi tanlagan hudud\n{admission_classes} - Arizachi tanlagan sinf\n'
                group_chat_id = CHAT_ID
                await bot.send_message(group_chat_id, f"<blockquote><b>{send_admission}</b></blockquote>", parse_mode=types.ParseMode.HTML)
                await message.answer(f"<b>Qabul uchun arizangiz muvaffaqiyatli yuborildi raxmat !</b>", parse_mode=types.ParseMode.HTML)
                await state.reset_state(with_data=True)
                await state.update_data(language=select__language)
            else:
                await message.answer(f"<b>Kirish formati + belgisi va 12 raqam. Iltimos, qaytadan kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.DOCUMENT:
            await message.answer(f"<b>Siz bilan bog'lanishlari uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.PHOTO:
            await message.answer(f"<b>Siz bilan bog'lanishlari uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
        elif message.content_type == types.ContentType.VIDEO:
            await message.answer(f"<b>Siz bilan bog'lanishlari uchun raqamingizni kiriting !</b>", parse_mode=types.ParseMode.HTML)
########################################################################################################################
if __name__ == '__main__':
    from aiogram import executor
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True, on_startup=on_startup)
