# сообщение для команды /help и при нераспознанном сообщении до старта сценария
HELP_ANSWER = 'Это бот для заказа пиццы.\n' \
              'Возможные команды:\n /pizza — заказ пиццы,\n' \
              ' /help — помощь по командам бота.'

# структура соответствия допустимых команд и действий: либо сообщение в ответ на команду,
# либо название сценария, обрабатывающего эту команду
INTENTS = [
    {
        'name': 'помощь по командам бота',
        'command': '/help',
        'scenario': None,
        'answer': HELP_ANSWER
    },
    {
        'name': 'заказ пиццы',
        'command': '/pizza',
        'scenario': 'ordering_pizza',
        'answer': None
    },

]

# структуры сценариев
SCENARIOS = {
    'ordering_pizza': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Какую вы хотите пиццу? Большую или маленькую?',
                'failure_text': 'Неверный размер пиццы. Попробуйте ещё раз.',
                'handler': 'handle_size',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Как вы будете платить?',
                'failure_text': 'Неверный метод оплаты. Попробуйте ещё раз.',
                'handler': 'handle_method',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Вы хотите {size} пиццу, оплата - {method}?',
                'failure_text': 'Неверное подтверждение заказа. Попробуйте ещё раз.',
                'handler': 'handle_confirm',
                'next_step': 'step4'
            },
            'step4': {
                'text': 'Спасибо за заказ.',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }

    }
}
