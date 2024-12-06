"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


users = ["Tania", "Zhuika", "krevetka"]
statuses = ["success", "expired", "random"]


@pytest.mark.parametrize(
    "user_name, status, expected_log_msg",
    [
        (users[0], statuses[0], f"Login event - Username: {users[0]}, Status: {statuses[0]}"),
        (users[1], statuses[1], f"Login event - Username: {users[1]}, Status: {statuses[1]}"),
        (users[2], statuses[2], f"Login event - Username: {users[2]}, Status: {statuses[2]}"),

    ],
    ids=[
        "user_success",
        "user_expired",
        "random_status"
    ],
)
def test_logger_functioning(user_name: str, status: str, expected_log_msg):
    log_event(user_name, status)
    with open("login_system.log", "r") as log:
        log_msg = log.read()

    assert expected_log_msg in log_msg
