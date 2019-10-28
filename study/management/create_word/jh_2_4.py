from study.models import Subject, TextbookUnit
from study.words import Word
from study.words.models import TextbookWord


def word_create():
    from study.management.commands.study_init import base_create

    subject = Subject.objects.get(name='英語')

    words = [
        {
            'name': 'pond',
            'mean': '池'
        },
        {
            'name': 'anything',
            'mean': '何か',
        }, {
            'name': 'else',
            'mean': '他に',
        }, {
            'name': 'tree',
            'mean': '木',
        }, {
            'name': 'dream',
            'mean': '夢',
        }, {
            'name': 'building',
            'mean': '建物',
        }, {
            'name': 'past',
            'mean': '過去',
        }, {
            'name': 'reach',
            'mean': '～に着く、～に到着する',
        }, {
            'name': 'corner',
            'mean': '角',
        }, {
            'name': 'south',
            'mean': '南',
        }, {
            'name': 'statue',
            'mean': '銅像',
        }, {
            'name': 'Chinese',
            'mean': '中国人、中国語、中国の',
        }, {
            'name': 'follow',
            'mean': '～についていく、～に従う',
        }, {
            'name': 'concert',
            'mean': 'コンサート',
        }, {
            'name': 'until',
            'mean': '～まで',
        }, {
            'name': 'helpful',
            'mean': '役に立つ、協力的な',
        }, {
            'name': 'both',
            'mean': '～の両方',
        }, {
            'name': 'center',
            'mean': '真ん中',
        }, {
            'name': 'full',
            'mean': 'いっぱいに',
        }, {
            'name': 'lake',
            'mean': '湖',
        }, {
            'name': 'change',
            'mean': '変わる',
        }, {
            'name': 'even',
            'mean': '～でさえ',
        }, {
            'name': 'museum',
            'mean': '博物館',
        }, {
            'name': 'anyway',
            'mean': 'とにかく',
        }, {
            'name': 'sometime',
            'mean': 'いつか'
        }
    ]
    args = [{
        'subject': subject,
        'name': word['name'],
        'mean': word['mean'],
    } for word in words]
    base_create(Word, *args)


def textbook_word_create():
    from study.management.commands.study_init import base_create

    textbook_unit = TextbookUnit.objects.get(name="Unit4 Taku Gets Lost")
    chap1 = textbook_unit.textbookchapter_set.get(name='Part1')
    chap2 = textbook_unit.textbookchapter_set.get(name='Part2')
    chap3 = textbook_unit.textbookchapter_set.get(name='Part3')
    ycdi = textbook_unit.textbookchapter_set.get(name='You Can Do It!')
    unit_words = {
        chap1: ['pond', 'anything', 'else', 'tree', 'dream'],
        chap2: ['building', 'past', 'reach', 'corner', 'south', 'statue', 'Chinese'],
        chap3: ['follow', 'concert', 'until', 'helpful', 'both'],
        ycdi: ['center', 'full', 'lake', 'change', 'even', 'museum', 'anyway', 'sometime'],
    }
    textbook_words = [{
        'textbook_unit': textbook_unit,
        'textbook_chapter': chapter,
        'word': Word.objects.get(name=word_name),
    } for chapter, words in unit_words.items() for word_name in words]
    base_create(TextbookWord, *textbook_words)
