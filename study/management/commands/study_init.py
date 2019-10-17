from django.core.management.base import BaseCommand

from study.models import School, Grade, Subject, Unit, Publisher, Textbook, TextbookUnit, TextbookChapter, Word


def base_create(klass, *args):
    """
    :param klass Model class
    :type args list of dict
    arg = kwargs
    """
    for arg in args:
        obj = klass.objects.filter(**arg)
        if obj:
            print('%s は既に存在しています' % obj)
            continue
        else:
            obj = klass(**arg)
            obj.save()
            print('%s を作成します' % obj)


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


def textbook_unit_create():
    textbook = Textbook.objects.get(name='COLUMBUS 21')
    units = [
        {
            'name': "Unit1 Tina's Speech",
            'textbook': textbook,
        },
        {
            'name': 'Unit2 Nick Helps a Dog',
            'textbook': textbook,
        },
    ]
    base_create(TextbookUnit, *units)


def textbook_chapter_create():
    unit = TextbookUnit.objects.get(name="Unit1 Tina's Speech")
    args = [{
        'textbook_unit': unit,
        'name': name
    } for name in ['Part1', 'Part2', 'Part3', 'You Can Do It!']]
    base_create(TextbookChapter, *args)


def word_create():
    grade = Grade.objects.get(name=2, school__name='中学')
    subject = Subject.objects.get(name='英語')
    textbook_unit = TextbookUnit.objects.get(name="Unit1 Tina's Speech")
    chap1, chap2, chap3, ycdi = textbook_unit.textbookchapter_set.all()
    words = {
        chap1: [
            {
                'name': 'came',
                'mean': 'comeの過去形、来た'
            }, {
                'name': 'before',
                'mean': '～の前に',
            }, {
                'name': 'city',
                'mean': '市、都市、都会',
            }, {
                'name': 'best',
                'mean': '最もよい、最良の、最良、最善',
            }, {
                'name': 'castle',
                'mean': '城',
            }, {
                'name': 'view',
                'mean': '眺め、景色',
            }, {
                'name': 'shopping',
                'mean': '買い物',
            }
        ],
        chap2: [
            {
                'name': 'was',
                'mean': 'am，isの過去形',
            }, {
                'name': 'born',
                'mean': '生まれる',
            }, {
                'name': 'grew',
                'mean': 'growの過去形、成長した、育った',
            }, {
                'name': 'grow',
                'mean': '成長する、育つ',
            }, {
                'name': 'spoke',
                'mean': 'speakの過去形、話した',
            }, {
                'name': 'language',
                'mean': '言語、言葉',
            }, {
                'name': 'were',
                'mean': 'areの過去形',
            }, {
                'name': 'Mt.',
                'mean': '山',
            }, {
                'name': 'kitchen',
                'mean': '台所',
            }, {
                'name': 'exciting',
                'mean': 'わくわくさせる、興奮させる',
            }, {
                'name': 'easy',
                'mean': '簡単な',
            }, {
                'name': 'difficult',
                'mean': '難しい',
            }],
        chap3: [
            {
                'name': 'question',
                'mean': '質問',
            }, {
                'name': 'group',
                'mean': '班、組',
            }, {
                'name': 'information',
                'mean': '情報',
            }, {
                'name': 'Internet',
                'mean': 'インターネット',
            }, {
                'name': 'special',
                'mean': '特別な',
            }, {
                'name': 'friendly',
                'mean': '友好的な、人なつっこい'
            }
        ],
        ycdi: [
            {
                'name': 'stadium',
                'mean': '競技場、スタジアム',
            }, {
                'name': 'won',
                'mean': 'winの過去形、勝った',
            }, {
                'name': 'win',
                'mean': '勝つ'
            }
        ],
    }
    args = [{
        'grade': grade,
        'subject': subject,
        'textbook_unit': textbook_unit,
        'textbook_chapter': chapter,
        'name': word['name'],
        'mean': word['mean'],
    } for chapter, chap_word in words.items() for word in chap_word]
    base_create(Word, *args)


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
