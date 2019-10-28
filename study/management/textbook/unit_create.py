from study.models import Textbook, TextbookUnit


def textbook_unit_create():
    from study.management.commands.study_init import base_create

    textbook = Textbook.objects.get(name='COLUMBUS 21')
    units = [
        {
            'name': "Unit1 Tina's Speech",
            'textbook': textbook,
        }, {
            'name': 'Unit2 Nick Helps a Dog',
            'textbook': textbook,
        }, {
            'name': 'Unit3 Plans for the Summer',
            'textbook': textbook,
        }, {
            'name': 'Unit4 Taku Gets Lost',
            'textbook': textbook,
        }, {
            'name': 'Let\'s Read 1 The Letter',
            'textbook': textbook,
        }
    ]
    base_create(TextbookUnit, *units)
