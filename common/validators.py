from datetime import date

from django.utils import timezone
from rest_framework.exceptions import ValidationError


def validate_user_age(birthdate):

    # Проверяем, указана ли дата рождения
    if not birthdate:
        raise ValidationError(
            "Укажите дату рождения, чтобы создать продукт."
        )

    # Преобразуем дату в формат date
    try:
        birthdate = date.fromisoformat(str(birthdate))
    except (ValueError, TypeError):
        raise ValidationError(
            "Некорректная дата рождения."
        )

    # Получаем сегодняшнюю дату
    today = timezone.localdate()

    # Вычисляем возраст
    age = today.year - birthdate.year

    if (today.month, today.day) < (
        birthdate.month,
        birthdate.day
    ):
        age -= 1

    # Проверяем возраст
    if age < 18:
        raise ValidationError(
            "Вам должно быть 18 лет, чтобы создать продукт."
        )

    return True

# from datetime import date
#
# from rest_framework.exceptions import ValidationError
#
#
# def check_user_age(token):
#     birthdate = token.get("birthdate")
#
#     if not birthdate:
#         raise ValidationError(
#             "Укажите дату рождения, чтобы создать продукт."
#         )
#
#     birthdate = date.fromisoformat(birthdate)
#     today = date.today()
#
#     age = today.year - birthdate.year
#
#     if (today.month, today.day) < (birthdate.month, birthdate.day):
#         age -= 1
#
#     if age < 18:
#         raise ValidationError(
#             "Вам должно быть 18 лет, чтобы создать продукт."
#         )