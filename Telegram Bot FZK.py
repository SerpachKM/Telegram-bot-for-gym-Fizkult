import telebot
from telebot import types
import sqlite3
import time
import datetime
from data_tele_bot import TOKEN, message_admin, tzs, tzs_tren, fpfv, fpsb, fpfusy, fpysk

#Создаем экземпляр класса TeleBot
bot = telebot.TeleBot(TOKEN)

#Напоминание пользователю
def reminder(callback):
    time.sleep(60)
    bot.send_message(callback.message.chat.id, 'Вас что-то отвлекло? Выберите, пожалуйста, кнопку выше.👆')
    time.sleep(82800)
    bot.send_message(callback.message.chat.id, 'Вы так и не закончили запись.Не упускайте шанс, быть лучшей версией себя.')

#Выбор
@bot.message_handler(commands=['start'])
def handle_start(message):
    #Узнаем id пользователя
    user_id = message.from_user.id

    # Создаем объект с кнопками клавиатуры
    markup = types.InlineKeyboardMarkup()
    # Создаем первую строку кнопок
    raw1 = types.InlineKeyboardButton('Для себя', callback_data='btn1')
    raw2 = types.InlineKeyboardButton('Для ребенка', callback_data='btn2')
    # Добавляем кнопки на клавиатуру
    markup.add(raw1)
    markup.add(raw2)
    bot.send_message(message.chat.id, 'Приветствуем вас в тренажерном фитнес-зале «КЛС Физкульт Гвардейское».'
                                      '\n\nДля кого подбираете программу?', reply_markup=markup)
    # Подключаемся к базе данных
    conn = sqlite3.connect('data_pearson.db')
    cur = conn.cursor()

    # Проверяем, существует ли уже запись с указанным user_id
    cur.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (user_id,))
    result = cur.fetchone()
    count = result[0]

    if not message_admin['id_pearson']:
        message_admin['id_pearson'] = count

    else:
        del message_admin['id_pearson']
        message_admin['id_pearson'] = count

    # Закрываем соединение
    cur.close()
    conn.close()

class ForMyself:

    # Для себя
    @bot.callback_query_handler(func=lambda call: call.data == 'btn1')
    def action_for_self(callback):
        # Создаем объект с кнопками клавиатуры
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw3 = types.InlineKeyboardButton('Узнать о предложениях', callback_data='btn3')
        raw4 = types.InlineKeyboardButton('Записаться на пробное', callback_data='btn4')
        raw5 = types.InlineKeyboardButton('Приобрести абонемент', callback_data='btn5')
        # Добавляем кнопки на клавиатуру
        markup.add(raw3)
        markup.add(raw4)
        markup.add(raw5)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Физкульт–привет 👋\n\nРады, что вы решили познакомиться с нами поближе. "
                         "Мы – клуб любителей спорта “Физкульт”. Наша мечта: помочь "
                         "как можно большему количеству людей получить красивое и здоровое тело\n💪"
                         "\n\nДля этого мы разработали индивидуальные и групповые методики, "
                         "организовали пространство со всеми необходимыми инструментами и "
                         "команду профессионалов, которые помогут со всем разобраться.\n\nА чего хотели бы вы?",
                         reply_markup=markup)
        reminder(callback)

    # Узнать о предложениях
    @bot.callback_query_handler(func=lambda call: call.data == 'btn3')
    def action_for_child_learn_about_offers(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw6 = types.InlineKeyboardButton('Тренажерный зал', callback_data='btn6')
        raw7 = types.InlineKeyboardButton('Фитнес-программы', callback_data='btn7')
        raw8 = types.InlineKeyboardButton('Не опредилился', callback_data='btn8')
        # Добавляем кнопки на клавиатуру
        markup.add(raw6)
        markup.add(raw7)
        markup.add(raw8)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Отлично."
                                                   "\nЧтоб Вам было бы интересно?", reply_markup=markup)
        reminder(callback)

    # Трен-зал
    @bot.callback_query_handler(func=lambda call: call.data == 'btn6' or call.data == 'btn21' or call.data == 'btn55'
                                                  or call.data == 'btn64' or call.data == 'btn71' or call.data == 'btn78'
                                                  or call.data == 'btn85')
    def action_for_chil(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw13 = types.InlineKeyboardButton('Самостоятельно', callback_data='btn13')
        raw14 = types.InlineKeyboardButton('С тренером', callback_data='btn14')
        raw15 = types.InlineKeyboardButton('Не решил', callback_data='btn15')
        # Добавляем кнопки на клавиатуру
        markup.add(raw13)
        markup.add(raw14)
        markup.add(raw15)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Чтобы подобрать актуальное предложение, зададим вам пару вопросов:"
                                                   "\n\nКак вам было бы комфортнее заниматься в тренажерном зале?",
                         reply_markup=markup)
        reminder(callback)

    # Самостоятельно
    @bot.callback_query_handler(func=lambda call: call.data == 'btn43' or call.data == 'btn13' or call.data == 'btn22')
    def action_fil(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw39 = types.InlineKeyboardButton('Подробнее о занятиях с тренером', callback_data='btn39')
        raw40 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn40')
        raw41 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn41')
        raw42 = types.InlineKeyboardButton('Посмотреть фитнес-программы', callback_data='btn42')
        # Добавляем кнопки на клавиатуру
        markup.add(raw39)
        markup.add(raw40)
        markup.add(raw41)
        markup.add(raw42)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Наш тренажерный зал находится по адресу: Гагарина, 95/6\n\nОн работает по расписанию:"
                         "\nпн/ср/пт – 8:00-21:00\nвт/чт – 8:00-10:00 и 16:00-21:00\nсб – 9:00-13:00\nвс – выходной"
                         "\n\nДля посещения вы можете приобрести один из следующих\nабонементов:"
                         f"\n\n“Утро” – действует с 8:00 до 16:00, стоимость {tzs[3]}₽ за 4 тренировки, {tzs[2]}₽ за 8 и {tzs[1]}₽ за 12."
                         f"\n\n“Обед” – действует в дневные часы с 12:00 до 16:00, стоимость от {tzs[4]}₽ за 4 тренировки до {tzs[2]}₽ за 12."
                         "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по расписанию работы тренажерного зала"
                         f" или времени занятия по фитнес–программе, стоимость абонемента от {tzs[2]}₽ за 4 тренировки до {tzs[-1]}₽ за 12 тренировок."
                         "\n\n“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен "
                         f"количеством тренировок, стоимость {tzs[0]}₽ на 30 дней."
                         "\n\nВ стоимость этих абонементов включена типовая программа тренировок и помощь "
                         "тренера для обучения работы на тренажерах.\n\nНаши абонементы действуют на оба зала: тренажерный и фитнес. "
                         "Вы можете взять абонемент на 4, 8 или 12 занятий, и разделить их между двумя залами. Таким образом "
                         "ваши тренировки смогут быть еще более эффективными!\n\nСамостоятельное посещение тренажерного зала "
                         "подходит вам, если у вас нет медицинских противопоказаний, и целью вашего посещения является "
                         "не восстановление после травм, операций и пр.\n\nВ противном случае мы рекомендуем занятия с нашими тренерами.",
                         reply_markup=markup)
        reminder(callback)

    # С тренером
    @bot.callback_query_handler(func=lambda call: call.data == 'btn47' or call.data == 'btn14' or call.data == 'btn39'
                                                  or call.data == 'btn23')
    def action_foh(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw43 = types.InlineKeyboardButton('Подробнее о самостоятельном посещении', callback_data='btn43')
        raw44 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn44')
        raw45 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn45')
        raw46 = types.InlineKeyboardButton('Посмотреть фитнес-программы', callback_data='btn46')
        # Добавляем кнопки на клавиатуру
        markup.add(raw43)
        markup.add(raw44)
        markup.add(raw45)
        markup.add(raw46)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Решили заниматься с тренером? Это оптимальное решение для людей с "
                                                   "медицинскими противопоказаниями, после травм или при болях в спине, "
                                                   "суставах и т.п., потому что тренер подберет нужные именно под ваши "
                                                   "запросы упражнения и проконтролирует технику их выполнения."
                                                   "\n\nВ нашем зале вас встретят Владимир и Ольга – сертифицированные"
                                                   " инструкторы тренажерного зала, прошедшие специальную подготовку в "
                                                   "Центре InstructorPRO, имеющем государственную лицензию."
                                                   "\n\nОни проведут необходимые тесты и составят для вас оптимальную "
                                                   "программу тренировок, дадут все необходимые рекомендации и сделают"
                                                   " ваши занятия полезными и эффективными для достижения ваших целей."
                                                   f"\n\nАбонементы на занятия с тренером:\n8 занятий – {tzs_tren[1]}₽\n10 занятий – {tzs_tren[0]}₽."
                                                   "\n\nВы можете выбрать время начала занятий:\n\nу Ольги\nпн – 17:00, 18:00, 19:00, 20:00"
                                                   "\nвт – 18:00\nср – 17:00, 18:00\nчт – 17:00, 18:00\nпт – 17:00, 18:00, 19:00, 20:00"
                                                   "\nсб – 11:00, 12:00\n\nу Владимира\nпн – 19:00, 20:00\nср – 19:00, 20:00"
                                                   "\nпт – 19:00, 20:00\n\nЗапишитесь на пробное занятие, чтобы все подробно обсудить с тренером.",
                         reply_markup=markup)
        reminder(callback)

    # Не решил
    @bot.callback_query_handler(func=lambda call: call.data == 'btn15' or call.data == 'btn24')
    def action_h(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw47 = types.InlineKeyboardButton('Подробнее о занятиях с тренером', callback_data='btn47')
        raw48 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn48')
        raw49 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn49')
        raw50 = types.InlineKeyboardButton('Посмотреть фитнес-программы', callback_data='btn50')
        # Добавляем кнопки на клавиатуру
        markup.add(raw47)
        markup.add(raw48)
        markup.add(raw49)
        markup.add(raw50)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Ну что ж.\nНачнем с самостоятельного посещения.\n\nНаш тренажерный зал находится по адресу: Гагарина, 95/6"
                         "\n\nОн работает по расписанию:\nпн/ср/пт – 8:00-21:00\nвт/чт – 8:00-10:00 и 16:00-21:00\nсб – 9:00-13:00\nвс – выходной"
                         "\n\nnДля посещения вы можете приобрести один из следующих абонементов:"
                         f"\n\n“Утро” – действует с 8:00 до 16:00, стоимость {tzs[-3]}₽ за 4 тренировки, {tzs[2]}₽ за 8 и {tzs[1]}₽ за 12."
                         f"\n\n“Обед” – действует в дневные часы с 12:00 до 16:00, стоимость от {tzs[-2]}₽ за 4 тренировки до {tzs[2]}₽ за 12."
                         "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по расписанию работы тренажерного зала "
                         f"или времени занятия по фитнес–программе, стоимость абонемента от {tzs[2]}₽ за 4 тренировки до {tzs[-1]}₽ за 12 тренировок."
                         "\n\n“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен "
                         f"количеством тренировок, стоимость {tzs[0]}₽ на 30 дней.\n\nВ стоимость этих абонементов включена типовая "
                         "программа тренировок и помощь тренера для обучения работы на тренажерах."
                         "Наши абонементы действуют на оба зала: тренажерный и фитнес. Вы можете взять абонемент на 4, 8 или 12 занятий, "
                         "и разделить их между двумя залами. Таким образом ваши тренировки смогут быть еще более эффективными!"
                         "\n\nСамостоятельное посещение тренажерного зала подходит вам, если у вас нет медицинских противопоказаний, и"
                         " целью вашего посещения является не восстановление после травм, операций и пр."
                         "\n\nВ противном случае мы рекомендуем занятия с нашими тренерами.", reply_markup=markup)
        reminder(callback)

    # Фит-прог
    @bot.callback_query_handler(func=lambda call: call.data == 'btn42' or call.data == 'btn46' or call.data == 'btn7' or call.data == 'btn50')
    def action_for_ch(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw16 = types.InlineKeyboardButton('Фитнес-вечер', callback_data='btn16')
        raw17 = types.InlineKeyboardButton('Фитнес-утро', callback_data='btn17')
        raw18 = types.InlineKeyboardButton('Растяжка', callback_data='btn18')
        raw19 = types.InlineKeyboardButton('Умное тело', callback_data='btn19')
        raw20 = types.InlineKeyboardButton('Йога', callback_data='btn20')
        raw21 = types.InlineKeyboardButton('Подробнее о тренажерном зале', callback_data='btn21')
        # Добавляем кнопки на клавиатуру
        markup.add(raw16)
        markup.add(raw17)
        markup.add(raw18)
        markup.add(raw19)
        markup.add(raw20)
        markup.add(raw21)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Выберите программу, о которой хотите узнать больше:",
                         reply_markup=markup)
        reminder(callback)

    # Фит-вечер
    @bot.callback_query_handler(func=lambda call: call.data == 'btn16' or call.data == 'btn79' or call.data == 'btn72' or call.data == 'btn65' or call.data == 'btn58')
    def action_for_chedrserrfderefd(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw51 = types.InlineKeyboardButton('Фитнес-утро', callback_data='btn51')
        raw52 = types.InlineKeyboardButton('Растяжка', callback_data='btn52')
        raw53 = types.InlineKeyboardButton('Умное тело', callback_data='btn53')
        raw54 = types.InlineKeyboardButton('Йога', callback_data='btn54')
        raw55 = types.InlineKeyboardButton('Подробнее о тренажерном зале', callback_data='btn55')
        raw56 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn56')
        raw57 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn57')
        # Добавляем кнопки на клавиатуру
        markup.add(raw51)
        markup.add(raw52)
        markup.add(raw53)
        markup.add(raw54)
        markup.add(raw55)
        markup.add(raw56)
        markup.add(raw57)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Фитнес–вечер – это программа смешанных тренировок. "
                                                   "В разные дни мы даем упражнения на разные группы мышц и равномерно прокачиваем все тело."
                                                   " Силовые тренировки чередуются с кардио. Упор делается на “медленный фитнес”, когда мы "
                                                   "учимся слушать свое тело и давать ту нагрузку, которая необходима в данный момент. "
                                                   "Это дает максимум эффекта для поддержания себя в хорошей физической форме, формирует подтянутую фигуру и эластичные мышцы."
                                                   "\n\nРасписание тренировок публикуем заранее на нашей страничке в ВК на весь месяц."
                                                   "\n\nВремя проведения занятий 18:10 и 19:10 по понедельникам, средам и пятницам."
                                                   "\n\nДля посещения подходит наш единый абонемент на оба зала – фитнес и тренажерный:"
                                                   f"\n\n“Утро” – действует с 8:00 до 16:00, стоимость {fpfv[-1]}₽ за 4 тренировки, {fpfv[3]}₽ за 8 и {fpfv[5]}₽ за 12."
                                                   f"\n\n“Обед” – действует в дневные часы с 12:00 до 16:00, стоимость от {fpfv[4]}₽ за 4 тренировки до {fpfv[3]}₽ за 12."
                                                   "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по расписанию работы тренажерного зала"
                                                   f" или времени занятия по фитнес–программе, стоимость абонемента от {fpfv[3]}₽ за 4 тренировки до {fpfv[1]}₽ за 12 тренировок."
                                                   "\n\nn“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен"
                                                   f" количеством тренировок, стоимость {fpfv[0]}₽ на 30 дней."
                                                   "\n\nВыбирайте пробное занятие, чтобы оценить эту программу и ждем вас в нашем Физкульт–клубе!",
                         reply_markup=markup)
        reminder(callback)

    # Фит-утро
    @bot.callback_query_handler(func=lambda call: call.data == 'btn17' or call.data == 'btn73' or call.data == 'btn80' or call.data == 'btn66' or call.data == 'btn51')
    def actn_for_ch(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw58 = types.InlineKeyboardButton('Фитнес-вечер', callback_data='btn58')
        raw59 = types.InlineKeyboardButton('Растяжка', callback_data='btn59')
        raw60 = types.InlineKeyboardButton('Умное тело', callback_data='btn60')
        raw61 = types.InlineKeyboardButton('Йога', callback_data='btn61')
        raw62 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn62')
        raw63 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn63')
        raw64 = types.InlineKeyboardButton('Подробнее о тренажерном зале', callback_data='btn64')
        # Добавляем кнопки на клавиатуру
        markup.add(raw59)
        markup.add(raw60)
        markup.add(raw61)
        markup.add(raw62)
        markup.add(raw63)
        markup.add(raw64)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Фитнес–утро включает в себя занятия йогой, растяжкой и пилатесом с фитболом. "
                         "В основе сбалансированная core-тренировка, которая позволяет проработать все "
                         "главные мышцы тела и комплексно улучшить свою физическую подготовку. "
                         "Ориентирована на получение заряда энергии и качественное владение собственным телом. "
                         "После занятий вы будете себя чувствовать бодро, свободно, повысится выносливость, "
                         "самочувствие и настроение.\n\nНачало занятий в 9:00 по понедельникам, средам и пятницам."
                         "\n\nРасписание тренировок публикуем заранее на нашей страничке в ВК на весь месяц."
                         "\n\nДля посещения подходит наш единый абонемент на оба зала – фитнес и тренажерный:"
                         f"\n\n“Утро” – действует с 8:00 до 16:00, стоимость {fpfusy[-1]}₽ за 4 тренировки, {fpfusy[3]}₽ за 8 и {fpfusy[-2]}₽ за 12."
                         "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по расписанию работы тренажерного зала"
                         f" или времени занятия по фитнес–программе, стоимость абонемента от {fpfusy[3]}₽ за 4 тренировки до {fpfusy[1]}₽ за 12 тренировок."
                         "\n\n“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен "
                         f"количеством тренировок, стоимость {fpfusy[0]}₽ на 30 дней."
                         "\n\nВыбирайте пробное занятие, чтобы оценить эту программу и ждем вас в нашем Физкульт–клубе!",
                         reply_markup=markup)
        reminder(callback)

    # Растяжка
    @bot.callback_query_handler(func=lambda call: call.data == 'btn18' or call.data == 'btn89' or call.data == 'btn74' or call.data == 'btn59' or call.data == 'btn52')
    def actioor_ch(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw65 = types.InlineKeyboardButton('Фитнес-вечер', callback_data='btn65')
        raw66 = types.InlineKeyboardButton('Фитнес-утро', callback_data='btn66')
        raw67 = types.InlineKeyboardButton('Умное тело', callback_data='btn67')
        raw68 = types.InlineKeyboardButton('Йога', callback_data='btn68')
        raw69 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn69')
        raw70 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn70')
        raw71 = types.InlineKeyboardButton('Подробнее о тренажерном зале', callback_data='btn71')
        # Добавляем кнопки на клавиатуру
        markup.add(raw65)
        markup.add(raw66)
        markup.add(raw67)
        markup.add(raw68)
        markup.add(raw69)
        markup.add(raw70)
        markup.add(raw71)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Растяжка – это комплекс специальных упражнений на совершенствование "
                         "гибкости, развития качественной подвижности в суставах и эластичности мышц. "
                         "Такие упражнения необходимы каждому, независимо от возраста и степени развития гибкости."
                         "\n\nОни отлично восстанавливают силы. Могут использоваться как дополнительные к "
                         "основным тренировкам, так и являться самостоятельным комплексом."
                         "\n\nnМы проводим занятия по понедельникам, средам и пятницам в 10:00."
                         "\n\nДля посещения подходит наш единый абонемент на оба зала – фитнес и "
                         "тренажерный на утренние часы или без привязки ко времени:"
                         f"\n\n“Утро” – действует с 8:00 до 16:00, стоимость {fpfusy[-1]}₽ за 4 тренировки, {fpfusy[3]}₽ за 8 и {fpfusy[-2]}₽ за 12."
                         "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по расписанию работы тренажерного зала "
                         f"или времени занятия по фитнес–программе, стоимость абонемента от {fpfusy[3]}₽ за 4 тренировки до {fpfusy[1]}₽ за 12."
                         f"\n\n“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен количеством тренировок, стоимость {fpfusy[0]}₽ на 30 дней."
                         "\n\nДля записи выбирайте “Купить абонемент” или “Записаться на пробное”. С вами свяжется наш администратор. До встречи в “Физкульт”!",
                         reply_markup=markup)
        reminder(callback)

    # Умное-тело
    @bot.callback_query_handler(func=lambda call: call.data == 'btn19' or call.data == 'btn60' or call.data == 'btn53' or call.data == 'btn82' or call.data == 'btn67')
    def actionrere4or_ch(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw72 = types.InlineKeyboardButton('Фитнес-вечер', callback_data='btn72')
        raw73 = types.InlineKeyboardButton('Фитнес-утро', callback_data='btn73')
        raw74 = types.InlineKeyboardButton('Растяжка', callback_data='btn74')
        raw75 = types.InlineKeyboardButton('Йога', callback_data='btn75')
        raw76 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn76')
        raw77 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn77')
        raw78 = types.InlineKeyboardButton('Подробнее о тренажерном зале', callback_data='btn78')
        # Добавляем кнопки на клавиатуру
        markup.add(raw72)
        markup.add(raw73)
        markup.add(raw74)
        markup.add(raw75)
        markup.add(raw76)
        markup.add(raw77)
        markup.add(raw78)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "“Умное тело” – это терапевтические тренировки. Они подходят тем, "
                                                   "у кого имеются проблемные зоны, например, плоскостопие, боли в спине или"
                                                   " суставах, напряжение в шее и плечах, дискомфортные состояния при "
                                                   "физической активности или требуется восстановление, например, после родов."
                                                   "\n\nС помощью доступных техник, не требующих выносливости и специальных навыков, "
                                                   "мы поможем вам укрепить мышечный корсет, развить дыхание, координацию движений и самоконтроль."
                                                   "\n\nСреднее время тренировки 55 минут. Виталий – опытный тренер, который специализируется на этой программе. "
                                                   "Он вместе с вами простроит такой комплекс упражнений, который поможет "
                                                   "в решении именно вашей задачи, покажет и научит вас правильной механики выполнения."
                                                   "\n\nЗанятия проходят в нашем зале по адресу улица Бирюкова, 1 по вечерам в 20:10, понедельник, среда и пятница."
                                                   "\n\nДля посещения подойдет наш единый абонемент на оба зала – фитнес и тренажерный без привязки ко времени:"
                                                   "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по "
                                                   f"расписанию работы тренажерного зала или времени занятия по фитнес–программе, стоимость абонемента от {fpsb[3]}₽ за 4 тренировки до {fpsb[1]}₽ за 12."
                                                   f"\n\n“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен количеством тренировок, стоимость {fpsb[0]}₽ на 30 дней."
                                                   "\n\nДля записи выбирайте “Купить абонемент” или “Записаться на пробное”. С вами свяжется наш администратор. До встречи в “Физкульт”!",
                         reply_markup=markup)
        reminder(callback)

    # Йога
    @bot.callback_query_handler(func=lambda call: call.data == 'btn20' or call.data == 'btn54' or call.data == 'btn68' or call.data == 'btn61' or call.data == 'btn75')
    def ac(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw79 = types.InlineKeyboardButton('Фитнес-вечер', callback_data='btn79')
        raw80 = types.InlineKeyboardButton('Фитнес-утро', callback_data='btn80')
        raw81 = types.InlineKeyboardButton('Растяжка', callback_data='btn81')
        raw82 = types.InlineKeyboardButton('Умное тело', callback_data='btn82')
        raw83 = types.InlineKeyboardButton('Купить абонемент', callback_data='btn83')
        raw84 = types.InlineKeyboardButton('Записаться на пробное занятие', callback_data='btn84')
        raw85 = types.InlineKeyboardButton('Подробнее о тренажерном зале', callback_data='btn85')
        # Добавляем кнопки на клавиатуру
        markup.add(raw79)
        markup.add(raw80)
        markup.add(raw81)
        markup.add(raw82)
        markup.add(raw83)
        markup.add(raw84)
        markup.add(raw85)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Йогу в нашем клубе проводят тренеры высшей категории, имеющие опыт "
                                                   "работы в фитнес–индустрии 15+ лет и профильное образование, а также "
                                                   "получившие диплом йога-тренера. Поэтому практикуем не только асаны, "
                                                   "но и необходимые для правильной отработки дыхательные практики. "
                                                   "Это позволяет получить тот самый комплекс физического и "
                                                   "ментального здоровья, за который так ценится во всем мире йога. "
                                                   "Улучшится гибкость, мобильность и подвижность."
                                                   "\n\nДля начинающих предлагаем занятия хатха-йогой с элементами прана вьяямы - "
                                                   "улучшением функции внешнего дыхания. Время занятий 9:00 по средам и пятницам."
                                                   "\n\nДля более продвинутых или тех, кто решил посвятить себя этому направлению, "
                                                   "есть “Спецкласс Йога” по субботам в 7:00. Разбираем более детально все асаны, "
                                                   "выстраиваем правильное дыхание, учим балансам и совершенствуем тело."
                                                   "\n\nПосещение простой группы по йоге возможно с нашим единым абонементом на оба зала – фитнес и тренажерный:"
                                                   f"\n\n“Утро” – действует с 8:00 до 16:00, стоимость {fpfusy[-1]}₽ за 4 тренировки, {fpfusy[3]}₽ за 8 и {fpfusy[-2]}₽ за 12."
                                                   "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по расписанию работы тренажерного зала "
                                                   f"или времени занятия по фитнес–программе, стоимость абонемента от {fpfusy[3]}₽ за 4 тренировки до {fpfusy[1]}₽ за 12 тренировок."
                                                   f"\n\n“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен количеством тренировок, стоимость {fpfusy[-1]}₽ на 30 дней."
                                                   "\nТакже занятий йогой включены в наши фитнес–программы: фитнес–утро и фитнес–вечер. Для них также подойдут указанные абонементы."
                                                   f"\n\nДля участия в “Спецклассе” необходимо заполнение заявки. Группа ограничена. Стоимость 1 занятия – {fpysk[0]}₽."
                                                   "\n\nДля записи выбирайте “Купить абонемент” или “Записаться на пробное”. С вами свяжется наш администратор. До встречи в “Физкульт”!",
                         reply_markup=markup)
        reminder(callback)

    # Не-опред
    @bot.callback_query_handler(func=lambda call: call.data == 'btn8')
    def action_for_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw22 = types.InlineKeyboardButton('Самостоятельно', callback_data='btn22')
        raw23 = types.InlineKeyboardButton('С тренером', callback_data='btn23')
        raw24 = types.InlineKeyboardButton('Не решил', callback_data='btn24')
        # Добавляем кнопки на клавиатуру
        markup.add(raw22)
        markup.add(raw23)
        markup.add(raw24)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Да, чтобы определиться, нужно больше информации. Мы готовы ее предоставить!"
                         "\n\nНачнем с тренажерного зала, а потом вы сможете ознакомиться с фитнес–программами."
                         "\n\nЧтобы подобрать актуальное предложение, зададим вам пару вопросов:"
                         "\n\nКак вам было бы комфортнее заниматься в тренажерном зале?", reply_markup=markup)
        reminder(callback)

    # Если человек уже записывался
    @bot.callback_query_handler(func=lambda call: call.data == 'btn4' and message_admin['id_pearson'] > 0)
    def action_for_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw130 = types.InlineKeyboardButton('Абонемент', callback_data='btn130')
        raw131 = types.InlineKeyboardButton('Связаться с администратором', callback_data='btn131')
        # Добавляем кнопки на клавиатуру
        markup.add(raw130)
        markup.add(raw131)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,"Спасибо, что выбрали нас!\nЕсли вам понравилось пробное занятие, то будем рады видеть вас в зале,"
                                                  " а если остались вопросы, то наш администратор все вам разъяснит.", reply_markup=markup)
        reminder(callback)

    # Записаться на пробное
    @bot.callback_query_handler(func=lambda call: call.data == 'btn4' or call.data == 'btn84' or call.data == 'btn77'
                                                  or call.data == 'btn70' or call.data == 'btn63' or call.data == 'btn57'
                                                  or call.data == 'btn41' or call.data == 'btn45' or call.data == 'btn49'
                                                  or call.data == 'btn57' or call.data == 'btn63' or call.data == 'btn70'
                                                  or call.data == 'btn77' or call.data == 'btn84')
    def action_for_child_sign_up_for_a_trial(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw9 = types.InlineKeyboardButton('Тренажерный зал', callback_data='Тренажерный зал')
        raw10 = types.InlineKeyboardButton('Фитнес-программы', callback_data='Фитнес-программы')
        # Добавляем кнопки на клавиатуру
        markup.add(raw9)
        markup.add(raw10)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Куда вас записать?", reply_markup=markup)
        reminder(callback)

    # Трен-зал
    @bot.callback_query_handler(func=lambda call: call.data == 'Тренажерный зал')
    def action_for_child_sign_up_for_a_t(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw25 = types.InlineKeyboardButton('Самостоятельно', callback_data='Самостоятельно')
        raw26 = types.InlineKeyboardButton('С тренером', callback_data='С тренером')
        # Добавляем кнопки на клавиатуру
        markup.add(raw25)
        markup.add(raw26)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "С тренером или самостоятельно?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['mesto']:
            message_admin['mesto'] = button_text

        else:
            del message_admin['mesto']
            message_admin['mesto'] = button_text
        reminder(callback)

    # Самостоятельно
    @bot.callback_query_handler(func=lambda call: call.data == 'Самостоятельно')
    def action_for_child_sign_up_for_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw115 = types.InlineKeyboardButton('Пн,Ср,Пт 8:00 - 21:00', callback_data='Пн,Ср,Пт 8:00 - 21:00')
        raw116 = types.InlineKeyboardButton('Вт,Чт 8:00 - 10:00 16:00 - 21:00', callback_data='Вт,Чт 8:00 - 10:00 16:00 - 21:00')
        raw117 = types.InlineKeyboardButton('Сб 9:00 - 13:00', callback_data='Сб 9:00 - 13:00')
        # Добавляем кнопки на клавиатуру
        markup.add(raw115)
        markup.add(raw116)
        markup.add(raw117)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "В какое время вы бы хотели посещать зал?"
                                                   "\n\nМы предлагаем единые абонементы на оба зала: фитнес и тренажерный. "
                                                   "В них предусмотрено 4, 8 и 12 тренировок, а также безлимитный вариант."
                                                   f"\n\n“Утро” – действует с 8:00 до 16:00, стоимость {tzs[3]}₽ за 4 тренировки, {tzs[2]}₽ за 8 и {tzs[1]}₽ за 12."
                                                   f"\n\n“Обед” – действует в дневные часы с 12:00 до 16:00, стоимость от {tzs[-2]}₽ за 4 тренировки до {tzs[2]}₽ за 12."
                                                   "\n\n“Когда хочу, тогда хожу” – вы сможете приходить в любое время по расписанию работы тренажерного зала"
                                                   f" или времени занятия по фитнес–программе, стоимость абонемента от {tzs[2]}₽ за 4 тренировки до {tzs[-1]}₽ за 12 тренировок."
                                                   "\n\n“Безлимитный” – действует в любое время по расписанию работы тренажерного и фитнес–зала и не ограничен "
                                                   f"количеством тренировок, стоимость {tzs[0]}₽ на 30 дней.\n\nВы сами определяете сколько тренировок у вас будет в каком зале."
                                                   "\n\nИтак, какой период времени вы выбираете?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['s_trenerom_and_sam']:
            message_admin['s_trenerom_and_sam'] = button_text

        else:
            del message_admin['s_trenerom_and_sam']
            message_admin['s_trenerom_and_sam'] = button_text
        reminder(callback)

    # С тренером
    @bot.callback_query_handler(func=lambda call: call.data == 'С тренером')
    def action_for_child_sign_up_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw118 = types.InlineKeyboardButton('Пн,Ср,Пт 17:00, 18:00, 19:00, 20:00', callback_data='Пн,Ср,Пт 17:00, 18:00, 19:00, 20:00')
        raw119 = types.InlineKeyboardButton('Вт,Чт 17:00, 18:00, 20:00', callback_data='Вт,Чт 17:00, 18:00, 20:00')
        # Добавляем кнопки на клавиатуру
        markup.add(raw118)
        markup.add(raw119)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "В какое время вам удобно?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['s_trenerom_and_sam']:
            message_admin['s_trenerom_and_sam'] = button_text

        else:
            del message_admin['s_trenerom_and_sam']
            message_admin['s_trenerom_and_sam'] = button_text
        reminder(callback)

    # Фит-прог
    @bot.callback_query_handler(
        func=lambda call: call.data == 'Фитнес-программы' or call.data == 'btn121' or call.data == 'btn123'
                          or call.data == 'btn129' or call.data == 'btn127' or call.data == 'btn125')
    def action_for_child_sign_up_for_a(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw27 = types.InlineKeyboardButton('Фитнес-вечер', callback_data='btn27')
        raw28 = types.InlineKeyboardButton('Фитнес-утро', callback_data='btn28')
        raw29 = types.InlineKeyboardButton('Растяжка', callback_data='btn29')
        raw30 = types.InlineKeyboardButton('Умное тело', callback_data='btn30')
        raw31 = types.InlineKeyboardButton('Йога', callback_data='btn31')
        # Добавляем кнопки на клавиатуру
        markup.add(raw27)
        markup.add(raw28)
        markup.add(raw29)
        markup.add(raw30)
        markup.add(raw31)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Какая программа вам была бы интересна?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['mesto']:
            message_admin['mesto'] = button_text

        else:
            del message_admin['mesto']
            message_admin['mesto'] = button_text
        reminder(callback)

    # Фит-вечер
    @bot.callback_query_handler(func=lambda call: call.data == 'btn27')
    def acion_for_child_sign_up_for_a(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw120 = types.InlineKeyboardButton('Да', callback_data='Фитнес-вечер')
        raw121 = types.InlineKeyboardButton('Выбрать другую программу', callback_data='btn121')
        # Добавляем кнопки на клавиатуру
        markup.add(raw120)
        markup.add(raw121)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Тренировки проходят — "
                                                   "\nПн, Ср, Пт\n18:00, 19:00\n\nВас устраивает?", reply_markup=markup)
        reminder(callback)

    # Фит-утро
    @bot.callback_query_handler(func=lambda call: call.data == 'btn28')
    def acionor_chi_sign_up_for_a(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw122 = types.InlineKeyboardButton('Да', callback_data='Фитнес-утро')
        raw123 = types.InlineKeyboardButton('Выбрать другую программу', callback_data='btn123')
        # Добавляем кнопки на клавиатуру
        markup.add(raw122)
        markup.add(raw123)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Тренировки проходят —\nПн 9:00\nПилатес и фитбол\nСр, Пт, 9.00\nЙога"
                         "\n\nВас устраивает?", reply_markup=markup)
        reminder(callback)

    # Растяжка
    @bot.callback_query_handler(func=lambda call: call.data == 'btn29')
    def acionor_chi_sign8r_a(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw124 = types.InlineKeyboardButton('Да', callback_data='Растяжка')
        raw125 = types.InlineKeyboardButton('Выбрать другую программу', callback_data='btn125')
        # Добавляем кнопки на клавиатуру
        markup.add(raw124)
        markup.add(raw125)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Тренировки проходят —\nПн, Ср, Пт\n10:00\n\nВас устраивает?", reply_markup=markup)
        reminder(callback)

    # Умное-тело
    @bot.callback_query_handler(func=lambda call: call.data == 'btn30')
    def acionor_chi_si8r_a(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw126 = types.InlineKeyboardButton('Да', callback_data='Умное тело')
        raw127 = types.InlineKeyboardButton('Выбрать другую программу', callback_data='btn127')
        # Добавляем кнопки на клавиатуру
        markup.add(raw126)
        markup.add(raw127)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Тренировки проходят —\nПн, Ср, Пт\n20:10\n\nВас устраивает?", reply_markup=markup)
        reminder(callback)

    # Йога
    @bot.callback_query_handler(func=lambda call: call.data == 'btn31')
    def acionor_i_si8r_a(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw128 = types.InlineKeyboardButton('Да', callback_data='Йога')
        raw129 = types.InlineKeyboardButton('Выбрать другую программу', callback_data='btn129')
        # Добавляем кнопки на клавиатуру
        markup.add(raw128)
        markup.add(raw129)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Тренировки проходят —\nСр, Пт\n9:00\n\nВас устраивает?", reply_markup=markup)
        reminder(callback)

    # Приобрести абонемент
    @bot.callback_query_handler(func=lambda call: call.data == 'btn5' or call.data == 'btn40' or call.data == 'btn44'
                                                  or call.data == 'btn48' or call.data == 'btn56' or call.data == 'btn62'
                                                  or call.data == 'btn69' or call.data == 'btn76' or call.data == 'btn83'
                                                  or call.data == 'btn130')
    def action_for_child_purchase_a_subscription(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw11 = types.InlineKeyboardButton('Тренажерный зал', callback_data='Тренажерный - зал')
        raw12 = types.InlineKeyboardButton('Фитнес-программы', callback_data='Фитнес - программы')
        # Добавляем кнопки на клавиатуру
        markup.add(raw11)
        markup.add(raw12)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Выберите нужный пункт.", reply_markup=markup)
        reminder(callback)

    # Трен-зал
    @bot.callback_query_handler(func=lambda call: call.data == 'Тренажерный - зал')
    def action_for_child_sign_up_for_a_t(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw32 = types.InlineKeyboardButton('Самостоятельно', callback_data='Самостоятельно')
        raw33 = types.InlineKeyboardButton('С тренером', callback_data='С тренером')
        # Добавляем кнопки на клавиатуру
        markup.add(raw32)
        markup.add(raw33)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "С тренером или самостоятельно?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['mesto']:
            message_admin['mesto'] = button_text

        else:
            del message_admin['mesto']
            message_admin['mesto'] = button_text
        reminder(callback)

    # С тренером
    @bot.callback_query_handler(func=lambda call: call.data == 'С тренером')
    def action_for_ld_sign_up_for_a_t(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw97 = types.InlineKeyboardButton('Владимир', callback_data='Владимир')
        raw98 = types.InlineKeyboardButton('Ольга', callback_data='Ольга')
        raw99 = types.InlineKeyboardButton('Любой из них', callback_data='Любой из них')
        # Добавляем кнопки на клавиатуру
        markup.add(raw97)
        markup.add(raw98)
        markup.add(raw99)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "В  тренажерном зале у нас два тренера: "
                                                   "Владимир и Ольга – оба сертифицированные инструкторы тренажерного зала, "
                                                   "прошедшие специальную подготовку в Центре InstructorPRO, имеющем государственную лицензию."
                                                   "\n\nВремя начала занятий у Ольги:\nпн – 17:00, 18:00, 19:00, 20:00\nвт – 18:00"
                                                   "\nср – 17:00, 18:00\nчт – 17:00, 18:00\nпт – 17:00, 18:00, 19:00, 20:00\nсб – 11:00, 12:00"
                                                   "\n\nВремя начала занятий у Владимира:\nпн – 19:00, 20:00\nср – 19:00, 20:00\nпт – 19:00, 20:00"
                                                   "\n\nУ вас есть какие-то предпочтения или вам подходит любое время с любым из наших тренеров?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['s_trenerom_and_sam']:
            message_admin['s_trenerom_and_sam'] = button_text

        else:
            del message_admin['s_trenerom_and_sam']
            message_admin['s_trenerom_and_sam'] = button_text
        reminder(callback)

    # Посещения
    @bot.callback_query_handler(func=lambda call: call.data == 'Владимир' or call.data == 'Ольга' or call.data == 'Любой из них')
    def actfor_child_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw100 = types.InlineKeyboardButton(f'10 посещений - {tzs_tren[0]}Р', callback_data=f'10 посещений-{tzs_tren[0]}Р')
        raw101 = types.InlineKeyboardButton(f'8 посещений - {tzs_tren[1]}Р', callback_data=f'8 посещений-{tzs_tren[1]}Р')
        raw102 = types.InlineKeyboardButton(f'4 посещений - {tzs_tren[2]}Р', callback_data=f'4 посещений-{tzs_tren[2]}Р')
        # Добавляем кнопки на клавиатуру
        markup.add(raw100)
        markup.add(raw101)
        markup.add(raw102)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Какой абонемент Вы выберете?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['tren_name']:
            message_admin['tren_name'] = button_text

        else:
            del message_admin['tren_name']
            message_admin['tren_name'] = button_text
        reminder(callback)

    # Самостоятельно
    @bot.callback_query_handler(func=lambda call: call.data == 'Самостоятельно')
    def action_for_child_si(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw86 = types.InlineKeyboardButton('Утро (8.00-16.00)', callback_data='Утро (8.00-16.00)')
        raw87 = types.InlineKeyboardButton('Обед (12.00-16.00)', callback_data='Обед (12.00-16.00)')
        raw88 = types.InlineKeyboardButton('Когда хочу, тогда хожу', callback_data='Когда хочу, тогда хожу')
        raw89 = types.InlineKeyboardButton(f'Безлемитный - {tzs[0]}Р', callback_data=f'безлемитный - {tzs[0]}Р')
        # Добавляем кнопки на клавиатуру
        markup.add(raw86)
        markup.add(raw87)
        markup.add(raw88)
        markup.add(raw89)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "В какое время вам удобнее посещать?\n- Абонемент сроком на 30 дней"
                                                   f"\n- Цена завит от количества посещений в месяц. «Утро» от {tzs[3]} р, "
                                                   f"\n«Обед» от {tzs[-2]}, В любое время от {tzs[2]}, безлимит - {tzs[0]}"
                                                   "\n- количество посещений вам будет предложено выбрать в следующем сообщении", reply_markup=markup)

        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['s_trenerom_and_sam']:
            message_admin['s_trenerom_and_sam'] = button_text

        else:
            del message_admin['s_trenerom_and_sam']
            message_admin['s_trenerom_and_sam'] = button_text
        reminder(callback)

    # Посещения
    @bot.callback_query_handler(func=lambda call: call.data == 'Утро (8.00-16.00)' or call.data == 'Обед (12.00-16.00)' or call.data == 'Когда хочу, тогда хожу')
    def action_for_child_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw90 = types.InlineKeyboardButton(f'12 посещений - {tzs[1]}Р', callback_data=f'12 Посещений - {tzs[1]}Р')
        raw91 = types.InlineKeyboardButton(f'8 посещений - {tzs[2]}Р', callback_data=f'8 Посещений - {tzs[2]}Р')
        raw92 = types.InlineKeyboardButton(f'4 посещений - {tzs[3]}Р', callback_data=f'4 Посещений - {tzs[3]}Р')
        # Добавляем кнопки на клавиатуру
        markup.add(raw90)
        markup.add(raw91)
        markup.add(raw92)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Выберете оптимальное для себя количество тренировок в месяц.", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['time_tren']:
            message_admin['time_tren'] = button_text

        else:
            del message_admin['time_tren']
            message_admin['time_tren'] = button_text
        reminder(callback)

    # Канал связи
    @bot.callback_query_handler(func=lambda call: call.data == f'10 посещений-{tzs_tren[0]}Р' or call.data == f'8 посещений-{tzs_tren[1]}Р'
                                                  or call.data == f'4 посещений-{tzs_tren[2]}Р' or call.data == f'безлемитный - {tzs[0]}Р'
                                                  or call.data == f'12 Посещений - {tzs[1]}Р' or call.data == f'8 Посещений - {tzs[2]}Р'
                                                  or call.data == f'4 Посещений - {tzs[3]}Р' or call.data == f'Безлимитный - {fpsb[0]}p'
                                                  or call.data == f'12 посещений - {fpsb[5]}p' or call.data == f'8 посещений - {fpsb[-1]}p'
                                                  or call.data == f'4 посещений - {fpsb[3]}p' or call.data == f'Безлимитный - {fpfusy[0]}Р.'
                                                  or call.data == f'12 посещений - {fpfusy[-2]}Р.' or call.data == f'8 посещений - {fpfusy[3]}Р.'
                                                  or call.data == f'4 посещений - {fpfusy[-1]}Р.' or call.data == f'Безлимитный - {fpfv[0]}Р'
                                                  or call.data == f'12 посещений - {fpfv[1]}Р' or call.data == f'8 посещений - {fpfv[2]}Р'
                                                  or call.data == f'4 посещений - {fpfv[3]}Р' or call.data == 'Пн,Ср,Пт 8:00 - 21:00'
                                                  or call.data == 'Вт,Чт 8:00 - 10:00 16:00 - 21:00' or call.data == 'Сб 9:00 - 13:00'
                                                  or call.data == 'Пн,Ср,Пт 17:00, 18:00, 19:00, 20:00' or call.data == 'Вт,Чт 17:00, 18:00, 20:00'
                                                  or call.data == 'Фитнес-вечер' or call.data == 'Фитнес-утро' or call.data == 'Йога'
                                                  or call.data == 'Растяжка' or call.data == 'Умное тело')
    def action_for_chil_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw93 = types.InlineKeyboardButton('Звонок по телефону', callback_data='Звонок по телефону')
        raw94 = types.InlineKeyboardButton('Telegram', callback_data='Telegram')
        raw95 = types.InlineKeyboardButton('WhatsApp', callback_data='WhatsApp')
        raw96 = types.InlineKeyboardButton('ВКонтакте', callback_data='ВКонтакте')
        # Добавляем кнопки на клавиатуру
        markup.add(raw93)
        markup.add(raw94)
        markup.add(raw95)
        markup.add(raw96)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id,
                         "Спасибо за ваши ответы. Наш администратор свяжется с вами в ближайшее время "
                         "для оформления и ответит на ваши вопросы, если такие еще остались."
                         "\n\nКакой канал связи для вас будет удобен?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if button_text == 'Фитнес-вечер' or button_text == 'Фитнес-утро' or button_text == 'Йога' or button_text == 'Растяжка' or button_text == 'Умное тело':
            if not message_admin['fit_prog']:
                message_admin['fit_prog'] = button_text
            else:
                del message_admin['fit_prog']
                message_admin['fit_prog'] = button_text


        elif button_text == 'Пн,Ср,Пт 17:00, 18:00, 19:00, 20:00' or button_text == 'Вт,Чт 17:00, 18:00, 20:00' or button_text == 'Пн,Ср,Пт 8:00 - 21:00' or button_text == 'Вт,Чт 8:00 - 10:00 16:00 - 21:00' or button_text == 'Сб 9:00 - 13:00':
            if not message_admin['time_tren']:
                message_admin['time_tren'] = button_text
            else:
                del message_admin['time_tren']
                message_admin['time_tren'] = button_text

        if button_text == f'10 посещений-{tzs_tren[0]}Р' or button_text == f'8 посещений-{tzs_tren[1]}Р' or button_text == f'4 посещений-{tzs_tren[2]}Р' or button_text == f'безлемитный - {tzs[0]}Р' or button_text == f'12 Посещений - {tzs[1]}Р' or button_text == f'8 Посещений - {tzs[2]}Р' or button_text == f'4 Посещений - {tzs[3]}Р' or button_text == f'Безлимитный - {fpsb[0]}p' or button_text == f'12 посещений - {fpsb[5]}p' or button_text == f'8 посещений - {fpsb[-1]}p' or button_text == f'4 посещений - {fpsb[3]}p' or button_text == f'Безлимитный - {fpfusy[0]}Р.' or button_text == f'12 посещений - {fpfusy[-2]}Р.' or button_text == f'8 посещений - {fpfusy[3]}Р.' or button_text == f'4 посещений - {fpfusy[-1]}Р.' or button_text == f'Безлимитный - {fpfv[0]}Р' or button_text == f'12 посещений - {fpfv[1]}Р' or button_text == f'8 посещений - {fpfv[2]}Р' or button_text == f'4 посещений - {fpfv[3]}Р':
            if not message_admin['pos']:
                message_admin['pos'] = button_text
            else:
                del message_admin['pos']
                message_admin['pos'] = button_text
        reminder(callback)

    #Данные для связи
    @bot.callback_query_handler(func=lambda call: call.data == 'Звонок по телефону' or call.data == 'Telegram' or call.data == 'WhatsApp' or call.data == 'ВКонтакте')
    def action_fotrgfor_a(callback):
        bot.send_message(callback.message.chat.id, "Введите, пожалуйста, ваш номер "
                                          "(Если вы хотите связаться через ВКоктакте то введите ссылку на ваш аккаунт).")
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['data for communication']:
            message_admin['data for communication'] = button_text
        else:
            del message_admin['data for communication']
            message_admin['data for communication'] = button_text
        reminder(callback)

    #Время для связи
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        # Узнаем id пользователя
        user_id = message.from_user.id
        # Подключаемся к базе данных
        conn = sqlite3.connect('data_pearson.db')
        cur = conn.cursor()

        # Проверяем, существует ли уже запись с указанным user_id
        cur.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (user_id,))
        result = cur.fetchone()
        count = result[0]

        if count > 0:
            bot.send_message(message.chat.id, "Запись уже существует!")
        else:
            # Добавляем аккаунт в базу данных
            cur.execute('INSERT INTO users (id, user_id) VALUES (?, ?)', (None, user_id))
            conn.commit()
            bot.send_message(message.chat.id, "Аккаунт добавлен в базу данных!")

        # Закрываем соединение
        cur.close()
        conn.close()

        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw115 = types.InlineKeyboardButton('С 8 до 13', callback_data='С 8 до 13')
        raw116 = types.InlineKeyboardButton('С 13 до 18', callback_data='С 13 до 18')
        raw117 = types.InlineKeyboardButton('С 18 до 22', callback_data='С 18 до 22')
        raw118 = types.InlineKeyboardButton('Все равно', callback_data='Все равно')
        # Добавляем кнопки на клавиатуру
        markup.add(raw115)
        markup.add(raw116)
        markup.add(raw117)
        markup.add(raw118)
        # Отправляем сообщение с клавиатурой
        bot.send_message(message.chat.id, "Когда вам удобнее принять звонок?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        text = message.text

        if not message_admin['phone']:
            message_admin['phone'] = text
        else:
            del message_admin['phone']
            message_admin['phone'] = text

    @bot.callback_query_handler(func=lambda call: call.data == 'С 8 до 13' or call.data == 'С 13 до 18' or call.data == 'С 18 до 22'
                                                  or call.data == 'Все равно')
    def _message(callback):
        bot.send_message(callback.message.chat.id, "Ожидайте звонка:].")
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['sv']:
            message_admin['sv'] = button_text

        else:
            del message_admin['sv']
            message_admin['sv'] = button_text
        bot.send_message(callback.message.chat.id, f"{message_admin}")
        reminder(callback)

    #Фит-программы
    @bot.callback_query_handler(func=lambda call: call.data == 'Фитнес - программы')
    def action_for_child_n_up_for_a(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw34 = types.InlineKeyboardButton('Фитнес-вечер', callback_data='Фитнес - вечер')
        raw35 = types.InlineKeyboardButton('Фитнес-утро', callback_data='Фитнес - утро')
        raw36 = types.InlineKeyboardButton('Растяжка', callback_data='Растяжка.')
        raw37 = types.InlineKeyboardButton('Умное тело', callback_data='Умное - тело')
        raw38 = types.InlineKeyboardButton('Йога', callback_data='Йога.')
        # Добавляем кнопки на клавиатуру
        markup.add(raw34)
        markup.add(raw35)
        markup.add(raw36)
        markup.add(raw37)
        markup.add(raw38)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Какая программа вам была бы интересна?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['mesto']:
            message_admin['mesto'] = button_text

        else:
            del message_admin['mesto']
            message_admin['mesto'] = button_text
        reminder(callback)

    # Фит-вечер
    @bot.callback_query_handler(func=lambda call: call.data == 'Фитнес - вечер')
    def actior_child_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw103 = types.InlineKeyboardButton(f'Безлимитный - {fpfv[0]}Р', callback_data=f'Безлимитный - {fpfv[0]}Р')
        raw104 = types.InlineKeyboardButton(f'12 посещений - {fpfv[1]}Р', callback_data=f'12 посещений - {fpfv[1]}Р')
        raw105 = types.InlineKeyboardButton(f'8 посещений - {fpfv[2]}Р', callback_data=f'8 посещений - {fpfv[2]}Р')
        raw106 = types.InlineKeyboardButton(f'4 посещений - {fpfv[3]}Р', callback_data=f'4 посещений - {fpfv[3]}Р')
        # Добавляем кнопки на клавиатуру
        markup.add(raw103)
        markup.add(raw104)
        markup.add(raw105)
        markup.add(raw106)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Какой абонемент вы выберете?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['fit_prog']:
            message_admin['fit_prog'] = button_text

        else:
            del message_admin['fit_prog']
            message_admin['fit_prog'] = button_text
        reminder(callback)

    # Фит-утро Растяжка Йога
    @bot.callback_query_handler(func=lambda call: call.data == 'Фитнес - утро' or call.data == 'Йога.' or call.data == 'Растяжка.')
    def actior_chi(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw107 = types.InlineKeyboardButton(f'Безлимитный - {fpfusy[0]}Р', callback_data=f'Безлимитный - {fpfusy[0]}Р.')
        raw108 = types.InlineKeyboardButton(f'12 посещений - {fpfusy[-2]}Р', callback_data=f'12 посещений - {fpfusy[-2]}Р.')
        raw109 = types.InlineKeyboardButton(f'8 посещений - {fpfusy[3]}Р', callback_data=f'8 посещений - {fpfusy[3]}Р.')
        raw110 = types.InlineKeyboardButton(f'4 посещений - {fpfusy[-1]}Р', callback_data=f'4 посещений - {fpfusy[-1]}Р.')
        # Добавляем кнопки на клавиатуру
        markup.add(raw107)
        markup.add(raw108)
        markup.add(raw109)
        markup.add(raw110)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Какой абонемент вы выберете?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['fit_prog']:
            message_admin['fit_prog'] = button_text

        else:
            del message_admin['fit_prog']
            message_admin['fit_prog'] = button_text
        reminder(callback)

    # Умное-тело
    @bot.callback_query_handler(func=lambda call: call.data == 'Умное - тело')
    def actd_(callback):
        markup = types.InlineKeyboardMarkup()
        # Создаем первую строку кнопок
        raw111 = types.InlineKeyboardButton(f'Безлимитный - {fpsb[0]}Р', callback_data=f'Безлимитный - {fpsb[0]}p')
        raw112 = types.InlineKeyboardButton(f'12 посещений - {fpsb[5]}Р', callback_data=f'12 посещений - {fpsb[5]}p')
        raw113 = types.InlineKeyboardButton(f'8 посещений - {fpsb[-1]}Р', callback_data=f'8 посещений - {fpsb[-1]}p')
        raw114 = types.InlineKeyboardButton(f'4 посещений - {fpsb[3]}Р', callback_data=f'4 посещений - {fpsb[3]}p')
        # Добавляем кнопки на клавиатуру
        markup.add(raw111)
        markup.add(raw112)
        markup.add(raw113)
        markup.add(raw114)
        # Отправляем сообщение с клавиатурой
        bot.send_message(callback.message.chat.id, "Какой абонемент вы выберете?", reply_markup=markup)
        # Получаем текст нажатой кнопки
        button_text = callback.data

        if not message_admin['fit_prog']:
            message_admin['fit_prog'] = button_text

        else:
            del message_admin['fit_prog']
            message_admin['fit_prog'] = button_text
        reminder(callback)


if __name__ == '__main__':
    # Запуск бота
    while True:
        try:
            bot.polling(none_stop=True, timeout=90)
        except Exception as e:
            print(datetime.datetime.now(), e)
            time.sleep(5)
            continue
