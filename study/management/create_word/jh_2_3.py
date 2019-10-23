from study.models import Subject, TextbookUnit
from study.words import Word
from study.words.models import TextbookWord


def word_create():
    from study.management.commands.study_init import base_create

    subject = Subject.objects.get(name='英語')

    words = [
        {
            'name': 'some',
            'mean': 'いくつかの'
        },
        {
            'name': 'as',
            'mean': '～と同じ',
        }, {
            'name': 'usual',
            'mean': '普段',
        }, {
            'name': 'tournament',
            'mean': 'トーナメント、勝ち抜き試合',
        }, {
            'name': 'sound',
            'mean': '音、響き',
        }, {
            'name': 'only',
            'mean': '～だけ',
        }, {
            'name': 'also',
            'mean': '～もまた',
        },
        {
            'name': 'pool',
            'mean': 'プール',
        }, {
            'name': 'movie',
            'mean': '映画',
        }, {
            'name': 'camping',
            'mean': 'キャンプ',
        }, {
            'name': 'will',
            'mean': '～だろう',
        }, {
            'name': 'guess',
            'mean': '～だと思う、～を推測する',
        }, {
            'name': 'boring',
            'mean': '退屈な',
        }, {
            'name': 'lucky',
            'mean': '幸運な',
        }, {
            'name': 'warm',
            'mean': '暖かい',
        }, {
            'name': 'cool',
            'mean': '涼しい',
        }, {
            'name': 'weather',
            'mean': '天気、気候',
        }, {
            'name': 'sun',
            'mean': '太陽',
        }, {
            'name': 'cloud',
            'mean': '雲',
        }, {
            'name': 'rain',
            'mean': '雨',
        }, {
            'name': 'rainy',
            'mean': '雨の日',
        }, {
            'name': 'snow',
            'mean': '雪',
        }, {
            'name': 'snowy',
            'mean': '雪の日',
        }, {
            'name': 'wind',
            'mean': '風',
        }, {
            'name': 'windy',
            'mean': '風の吹く日'
        },
        {
            'name': 'tomorrow',
            'mean': '明日',
        }, {
            'name': 'grandma',
            'mean': 'おばあちゃん、祖母',
        }, {
            'name': 'grandpa',
            'mean': 'おじちゃん、祖父'
        }, {
            'name': 'arrive',
            'mean': '到着する'
        }, {
            'name': 'pick',
            'mean': '～を選ぶ'
        }, {
            'name': 'forward',
            'mean': '前に'
        }, {
            'name': 'again',
            'mean': '再び、また'
        }, {
            'name': 'flight',
            'mean': '飛行、（飛行機の）便'
        }, {
            'name': 'arrival',
            'mean': '到着'
        }, {
            'name': 'hour',
            'mean': '1時間'
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

    textbook_unit = TextbookUnit.objects.get(name="Unit3 Plans for the Summer")
    chap1 = textbook_unit.textbookchapter_set.get(name='Part1')
    chap2 = textbook_unit.textbookchapter_set.get(name='Part2')
    chap3 = textbook_unit.textbookchapter_set.get(name='Part3')
    chap4 = textbook_unit.textbookchapter_set.get(name='Part4')
    ycdi = textbook_unit.textbookchapter_set.get(name='You Can Do It!')
    unit_words = {
        chap1: ['some', 'as', 'usual', 'tournament'],
        chap2: ['sound', 'only', 'also', 'pool', 'movie', 'camping'],
        chap3: ['will', 'guess', 'boring', 'lucky', 'warm', 'cool', 'weather', 'sun', 'cloud', 'rain', 'rainy', 'snow',
                'snowy', 'wind', 'windy', 'tomorrow'],
        chap4: ['grandma', 'grandpa', 'arrive', 'pick', 'forward', 'again'],
        ycdi: ['flight', 'arrival', 'hour'],
    }
    textbook_words = [{
        'textbook_unit': textbook_unit,
        'textbook_chapter': chapter,
        'word': Word.objects.get(name=word_name),
    } for chapter, words in unit_words.items() for word_name in words]
    base_create(TextbookWord, *textbook_words)
