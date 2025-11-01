import json
import datetime

# Список документов (можно расширить парсингом)
DOCUMENTS = [
    {
        "title": "Федеральный закон №123-ФЗ «Технический регламент о требованиях пожарной безопасности»",
        "date_start": "22.07.2008",
        "status": "действует",
        "url": "https://docs.cntd.ru/document/902190769"
    },
    {
        "title": "СП 484.1311500.2020 «Автоматические установки пожаротушения и пожарной сигнализации»",
        "date_start": "01.01.2021",
        "status": "действует",
        "url": "https://docs.cntd.ru/document/456114003"
    },
    {
        "title": "СП 5.13130.2009 (ред. 2022 г.) «Системы противопожарной защиты»",
        "date_start": "01.05.2010",
        "status": "действует",
        "url": "https://docs.cntd.ru/document/1200075329"
    },
    {
        "title": "ГОСТ Р 53325-2012 «Техника пожарная. Общие технические требования»",
        "date_start": "01.01.2013",
        "status": "действует",
        "url": "https://docs.cntd.ru/document/1200093179"
    },
    {
        "title": "ППБ 01-03-2023 «Правила пожарной безопасности»",
        "date_start": "10.06.2023",
        "status": "действует",
        "url": "https://pravo.gov.ru/document/1234567890"
    },
    {
        "title": "НПБ 88-2001",
        "date_start": "01.05.2001",
        "status": "утратил силу",
        "url": "https://web.archive.org/web/20200101000000*/npb88.ru"
    },
    {
        "title": "СП 485.1311500.2020 «Пожарные лифты»",
        "date_start": "01.01.2021",
        "status": "действует",
        "url": "https://docs.cntd.ru/document/456114004"
    },
    {
        "title": "СП 373.1325800.2017 «Системы оповещения»",
        "date_start": "08.06.2018",
        "status": "действует",
        "url": "https://docs.cntd.ru/document/456030001"
    }
]

output = {
    "last_update": datetime.datetime.utcnow().isoformat() + "Z",
    "documents": DOCUMENTS
}

with open("docs.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("✅ docs.json успешно обновлён")
