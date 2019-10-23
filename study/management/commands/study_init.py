from django.core.management.base import BaseCommand

from study.models import School, Grade, Subject, Unit, Publisher, Textbook
from study.words.models import Mode
from ..create_word import word_create, textbook_word_create
from ..textbook import textbook_chapter_create, textbook_unit_create


def base_create(klass, *args):
    """
    :param klass Model class
    :type args list of dict
    arg = kwargs
    """
    objects = []
    for kwargs in args:
        obj = klass.objects.filter(**kwargs)
        if obj:
            print('%s は既に存在しています' % obj)
            continue
        else:
            obj = klass(**kwargs)
            objects.append(obj)
            print('%s を作成します' % obj)
    klass.objects.bulk_create(objects)


def school_create():
    school_name = ['小学', '中学', '高校', '大学']
    args = [{'name': school} for school in school_name]
    base_create(School, *args)


def grade_create():
    school_grades = {
        '小学': [1, 2, 3, 4, 5, 6],
        '中学': [1, 2, 3],
        '高校': [1, 2, 3],
        '大学': [1, 2, 3, 4, 5, 6]
    }
    for school_name, grades in school_grades.items():
        school = School.objects.get(name=school_name)
        args = [
            {'school': school,
             'name': grade}
            for grade in grades
        ]
        base_create(Grade, *args)


def subject_create():
    subjects = [
        {'name': subject}
        for subject in ['英語', '数学', '国語', '理科', '社会']
    ]
    base_create(Subject, *subjects)


def unit_create():
    subject = Subject.objects.get(name='英語')
    grade_units = {
        1: [
            {
                'name': 'be動詞',
            }, {
                'name': '一般動詞',
            }, {
                'name': '疑問文',
            }, {
                'name': '否定文',
            }, {
                'name': '疑問詞',
                'parent': ['疑問文'],
            }, {
                'name': '命令文',
            }, {
                'name': '三単現',
                'parent': ['一般動詞'],
            }, {
                'name': '現在進行形',
                'parent': ['be動詞', '一般動詞'],
            }, {
                'name': 'can',
                'parent': ['一般動詞'],
            }, {
                'name': '過去形(一般動詞)',
                'parent': ['一般動詞'],
            }, {
                'name': '名詞の複数形',
            }, {
                'name': '代名詞',
            }
        ],
        2: [
            {
                'name': '過去形(be動詞)',
                'parent': ['be動詞'],
            }, {
                'name': '過去進行形',
                'parent': ['過去形(be動詞)', '現在進行形'],
            }, {
                'name': '未来形',
            }, {
                'name': '動名詞',
            }, {
                'name': '不定詞１',
            }, {
                'name': '助動詞',
                'parent': ['can', '未来形'],
            }, {
                'name': '比較',
            }, {
                'name': 'there is(are)',
            }, {
                'name': '接続詞',
            }, {
                'name': '受動態(受け身)',
            },
        ],
        3: [
            {
                'name': '現在完了',
            }, {
                'name': '不定詞２',
                'parent': ['不定詞１'],
            }, {
                'name': '分詞',
            }, {
                'name': '間接疑問文',
            }, {
                'name': '関係代名詞',
            }, {
                'name': '形容詞',
            }, {
                'name': '副詞'
            }
        ],
    }
    for grade, units in grade_units.items():
        grade = Grade.objects.get(name=grade, school__name='中学')
        args = [{
            'grade': grade,
            'subject': subject,
            'name': unit['name'],
        } for unit in units]
        base_create(Unit, *args)
        for unit in units:
            if unit.get('parent'):
                u = Unit.objects.get(name=unit['name'])
                for parent in unit['parent']:
                    parent = Unit.objects.get(name=parent)
                    u.parent.add(parent)
                u.save()


def publisher_create():
    publishers = [
        {'name': name}
        for name in ['光村図書']]
    base_create(Publisher, *publishers)


def textbook_create():
    publisher = Publisher.objects.get(name='光村図書')
    grade = Grade.objects.get(name=2, school__name='中学')
    subject = Subject.objects.get(name='英語')
    name = 'COLUMBUS 21'
    base_create(Textbook, dict(
        publisher=publisher,
        grade=grade,
        subject=subject,
        name=name
    ))


def mode_create():
    subject = Subject.objects.get(name='英語')
    args = [
        {
            'subject': subject,
            'name': name
        }
        for name in ['read', 'write']]
    base_create(Mode, *args)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        school_create()
        grade_create()
        subject_create()
        unit_create()
        publisher_create()
        textbook_create()
        textbook_unit_create()
        textbook_chapter_create()
        word_create()
        textbook_word_create()
        mode_create()
