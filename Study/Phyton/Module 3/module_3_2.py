def send_email(message, recipient,*, sender='university.help@gmail.com'):
    #----------------------------------------------------------------------------
    # Проверка на '@', '.ru', '.com', '.net'

    for i in [recipient,sender]:
        for j in ['.ru', '.com', '.net']:
            if i[len(i) - len(j): len(i)] in j:
                result = True
                break
            else:
                result = False
    for i in [recipient,sender]:
        if '@' in i:
            result2 = True
        else:
            result2 = False
    if result == False or result2 == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        pass
    #----------------------------------------------------------------------------
    # Проверка на отправку самому себе

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        pass
    # ----------------------------------------------------------------------------
    # Стандартный отправитель

    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    # Конец функции
    # ----------------------------------------------------------------------------


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')