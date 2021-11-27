from transitions import Machine


class Matter(object):
    def __init__(self):
        self.current_size = ''
        self.current_payment = ''

    def query_pizza_size(self):
        print('Какую вы хотите пиццу? Большую или маленькую?')

    def query_payment_type(self):
        print('Как вы будете платить?')

    def thanks_message(self):
        print('Спасибо за заказ\n')

    def confirmation_message(self):
        print(f'Вы хотите {self.current_size} пиццу, оплата - {self.current_payment}?')


pizza = Matter()

# The states
states = ['start_state',
          {'name': 'pizza_size', 'on_enter': ['query_pizza_size']},
          {'name': 'payment_type', 'on_exit': ['query_payment_type']},
          'confirmation', {'name': 'confirmation', 'on_exit': ['confirmation_message']},
          'thanks', {'name': 'thanks', 'on_exit': ['thanks_message']}
          ]

# Transitions between states.
transitions = [
    {'trigger': 'starting', 'source': 'start_state', 'dest': 'pizza_size'},
    {'trigger': 'size_choice', 'source': 'pizza_size', 'dest': 'payment_type'},
    {'trigger': 'payment_choice', 'source': 'payment_type', 'dest': 'confirmation'},
    {'trigger': 'confirmed', 'source': 'confirmation', 'dest': 'thanks'},
    {'trigger': 'end_order', 'source': 'thanks', 'dest': 'start_state'}
]

# Initialize
machine = Machine(model=pizza, states=states, transitions=transitions, initial='start_state')
# machine.add_ordered_transitions()

while True:
    if pizza.state == 'start_state':
        pizza.starting()
    elif pizza.state == 'pizza_size':
        pizza.size_choice()
        pizza.current_size = input('Введите ответ:')
    elif pizza.state == 'payment_type':
        pizza.payment_choice()
        pizza.current_payment = input('Введите ответ:')
    elif pizza.state == 'confirmation':
        pizza.confirmed()
        current_answer = input('Введите ответ:')
    else:
        pizza.end_order()
