import datetime
from utils import data


def new_list(data):
    """Создает список только с выполненными операциями EXECUTED """
    return [entry for entry in data if entry.get("state") == "EXECUTED"]
new_list = (new_list(data))


def sorted_list(new_list):
    """Сортировка списка по дате"""
    return sorted(new_list, key=lambda x: x['date'], reverse=True)
sorted_list=sorted_list(new_list)

def format_operation(sorted_list):
    '''Основное форматирование операций'''
    date = datetime.datetime.strptime(sorted_list["date"], "%Y-%m-%dT%H:%M:%S.%f")
    amount = float(sorted_list["operationAmount"]["amount"])
    currency = sorted_list["operationAmount"]["currency"]["name"]
    description = sorted_list["description"]
    from_account = sorted_list["from"] if "from" in sorted_list else ""
    to_account = sorted_list["to"] if "to" in sorted_list else ""

    formatted_date = date.strftime("%d.%m.%Y")
    formatted_amount = f"{amount:.2f} {currency}"
    if len(from_account) == 25:
        formatted_from_account = from_account[:4] + ' **' + from_account[-4:]
    else:
        formatted_from_account = from_account[:-12] + " " + from_account[-12:-10] + "".join("*" if i.isdigit() else i for i in from_account[-10:-8]) + " " + "".join("*" if i.isdigit() else i for i in from_account[-8:-4]) + " " + from_account[-4:]
    formatted_to_account = '**' + to_account[-4:]

    return f"{formatted_date} {description}\n{formatted_from_account} -> Счет {formatted_to_account}\n{formatted_amount}"