def handle_size(text: str, context: dict, scenario_name: str, user_id: int) -> bool:
    """
    Обрабатывает названия размера пиццы.
    При корректном значении заносит в context.
    :param text: текст сообщения пользователя
    :param context: словарь с информацией, получаемой из ответов пользователя
    :param scenario_name: название сценария
    :param user_id: идентификатор пользователя
    :return:
    """
    # проверка допустимости размера пиццы
    context['size'] = text
    return True


def handle_method(text: str, context: dict, scenario_name: str, user_id: int) -> bool:
    """
    Обрабатывает метод оплаты.
    При корректном значении заносит в context.
    :param text: текст сообщения пользователя
    :param context: словарь с информацией, получаемой из ответов пользователя
    :param scenario_name: название сценария
    :param user_id: идентификатор пользователя
    :return:
    """
    # проверка допустимости метода оплаты
    context['method'] = text
    return True


def handle_confirm(text: str, context: dict, scenario_name: str, user_id: int) -> bool:
    """
    Обрабатывает подтверждение заказа.
    :param text: текст сообщения пользователя
    :param context: словарь с информацией, получаемой из ответов пользователя
    :param scenario_name: название сценария
    :param user_id: идентификатор пользователя
    :return:
    """
    # проверка подтверждения заказа
    return True

