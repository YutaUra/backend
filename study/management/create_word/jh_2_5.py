from study.models import Subject, TextbookUnit
from study.words import Word
from study.words.models import TextbookWord


def word_create():
    from study.management.commands.study_init import base_create

    subject = Subject.objects.get(name='英語')

    words = [
        {
            'name': 'experience',
            'mean': '経験'
        }, {
            'name': 'amazing',
            'mean': '素晴らしい',
        }, {
            'name': 'sea',
            'mean': '海',
        }, {
            'name': 'collect',
            'mean': '集める',
        }, {
            'name': 'peace',
            'mean': '平和',
        }, {
            'name': 'memorial',
            'mean': '記念の',
        }, {
            'name': 'important',
            'mean': '重要な',
        }, {
            'name': 'stone',
            'mean': '石',
        }, {
            'name': 'monument',
            'mean': '記念碑',
        }, {
            'name': 'war',
            'mean': '戦争',
        }, {
            'name': 'victim',
            'mean': '被害者',
        }, {
            'name': 'pointed',
            'mean': 'pointの過去形、指さした',
        }, {
            'name': 'shop',
            'mean': '店',
        }, {
            'name': 'fast',
            'mean': '速い',
        }, {
            'name': 'quiz',
            'mean': 'クイズ',
        }, {
            'name': 'terrible',
            'mean': '恐ろしい',
        }, {
            'name': 'world',
            'mean': '世界',
        }, {
            'name': 'folk',
            'mean': '民間の、民衆の',
        }, {
            'name': 'tear(s)',
            'mean': '涙',
        }, {
            'name': 'such',
            'mean': '～のような',
        }, {
            'name': 'power',
            'mean': '力',
        }, {
            'name': 'future',
            'mean': '将来、未来',
        }, {
            'name': 'florist',
            'mean': '花屋',
        }, {
            'name': 'astronaut',
            'mean': '宇宙飛行士',
        }, {
            'name': 'flight attendant',
            'mean': '客室乗務員'
        }, {
            'name': 'driver',
            'mean': '運転士'
        }, {
            'name': 'Chinatown',
            'mean': '中華街'
        }, {
            'name': 'crowded',
            'mean': '混んでいる'
        }, {
            'name': 'finally',
            'mean': '最後に、ついには'
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

    textbook_unit = TextbookUnit.objects.get(name="Unit5 Aya\'s Time in Okinawa")
    chap1 = textbook_unit.textbookchapter_set.get(name='Part1')
    chap2 = textbook_unit.textbookchapter_set.get(name='Part2')
    chap3 = textbook_unit.textbookchapter_set.get(name='Part3')
    ycdi = textbook_unit.textbookchapter_set.get(name='You Can Do It!')
    unit_words = {
        chap1: ['experience', 'amazing', 'sea', 'collect'],
        chap2: ['peace', 'memorial', 'important', 'stone', 'monument', 'war', 'victim', 'pointed', 'shop', 'fast',
                'quiz'],
        chap3: ['terrible', 'world', 'folk', 'tear(s)', 'such', 'power', 'future', 'florist', 'astronaut',
                'flight attendant', 'driver'],
        ycdi: ['Chinatown', 'crowded', 'finally'],
    }
    textbook_words = [{
        'textbook_unit': textbook_unit,
        'textbook_chapter': chapter,
        'word': Word.objects.get(name=word_name),
    } for chapter, words in unit_words.items() for word_name in words]
    base_create(TextbookWord, *textbook_words)
