import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    try:
        logger.debug(f"Попытка замаскировать номер карты: {card_number}")
        card_str = str(card_number)

        if len(card_str) != 16:
            error_msg = "Номер карты некорректный - длина не равна 16 символам"
            logger.error(error_msg)
            raise ValueError(error_msg)

        first_six = card_str[:6]
        last_four = card_str[-4:]
        masked_part = "** ****"
        masked_card = f"{first_six[:4]} {first_six[4:6]}{masked_part} {last_four}"

        logger.info(f"Успешно замаскирован номер карты: {masked_card}")
        return masked_card

    except Exception as ex:
        logger.error(f"Ошибка при маскировании номера карты {card_number}: {str(ex)}")
        raise


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    try:
        logger.debug(f"Попытка замаскировать номер счета: {account_number}")
        account_str = str(account_number)
        masked_account = f"**{account_str[-4:]}"

        logger.info(f"Успешно замаскирован номер счета: {masked_account}")
        return masked_account

    except Exception as ex:
        logger.error(f"Ошибка при маскировании номера счета {account_number}: {str(ex)}")
        raise
