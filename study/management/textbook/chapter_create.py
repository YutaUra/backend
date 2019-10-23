from study.models import TextbookUnit, TextbookChapter


def base_chapter_create(unit_name, part_num, ycdi=True):
    from study.management.commands.study_init import base_create
    unit = TextbookUnit.objects.get(name=unit_name)
    parts = [f'Part{num + 1}' for num in range(part_num)]
    if ycdi:
        parts += ['You Can Do It!']
    args = [{
        'textbook_unit': unit,
        'name': name
    } for name in parts]
    base_create(TextbookChapter, *args)


def chapter_2_1():
    unit_name = "Unit1 Tina's Speech"
    base_chapter_create(unit_name, 3)


def chapter_2_2():
    unit_name = 'Unit2 Nick Helps a Dog'
    base_chapter_create(unit_name, 3)


def chapter_2_3():
    unit_name = 'Unit3 Plans for the Summer'
    base_chapter_create(unit_name, 4)


def textbook_chapter_create():
    chapter_2_1()
    chapter_2_2()
    chapter_2_3()
