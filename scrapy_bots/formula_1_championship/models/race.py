from scrapy import Field, Item
from scrapy.loader.processors import MapCompose, TakeFirst


def remove_blanck_spaces(value: str):
    return value.strip()

def remove_special_characters(value: str):
    return value.replace('“', '').replace('”', '').replace('"', '')

class Race(Item):
    name = Field(
        input_processor=MapCompose(remove_blanck_spaces, remove_special_characters),
        output_processor=TakeFirst()
    )
    local = Field(
        input_processor=MapCompose(remove_blanck_spaces, remove_special_characters),
        output_processor=TakeFirst()
    )
    winner = Field(
        input_processor=MapCompose(remove_blanck_spaces, remove_special_characters),
        output_processor=TakeFirst()
    )
    circuit_time = Field(
        input_processor=MapCompose(remove_blanck_spaces, remove_special_characters),
        output_processor=TakeFirst()
    )
