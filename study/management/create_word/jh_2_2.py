from study.models import Subject, TextbookUnit
from study.words import Word
from study.words.models import TextbookWord


def word_create():
    from study.management.commands.study_init import base_create

    subject = Subject.objects.get(name='英語')

    words = [
        {
            'name': 'slow',
            'mean': '遅い'
        }, {
            'name': 'hurt',
            'mean': '傷ついた',
        }, {
            'name': 'thing',
            'mean': 'もの、こと',
        }, {
            'name': 'vet',
            'mean': '獣医',
        }, {
            'name': 'bike',
            'mean': '自転車',
        }, {
            'name': 'number',
            'mean': '数字',
        }, {
            'name': 'coin',
            'mean': 'コイン、硬貨',
        },
        {
            'name': 'diary',
            'mean': '日記',
        }, {
            'name': 'sunny',
            'mean': '晴れの日',
        }, {
            'name': 'along',
            'mean': '～に沿って',
        }, {
            'name': 'found',
            'mean': 'findの過去形、見つけた',
        }, {
            'name': 'find',
            'mean': '見つける',
        }, {
            'name': 'weak',
            'mean': '弱い',
        }, {
            'name': 'shy',
            'mean': '恥ずかしがりや',
        }, {
            'name': 'worried',
            'mean': '～を心配して',
        }, {
            'name': 'cloudy',
            'mean': '曇りの日',
        }, {
            'name': 'news',
            'mean': '知らせ',
        }, {
            'name': 'glad',
            'mean': 'うれしい',
        }, {
            'name': 'lost',
            'mean': '無くした、迷った',
        },
        {
            'name': 'enter',
            'mean': '入る',
        }, {
            'name': 'shoe(s)',
            'mean': '靴',
        }, {
            'name': 'computer',
            'mean': 'コンピューター',
        }, {
            'name': 'bookstore',
            'mean': '本屋',
        }, {
            'name': 'chopstick(s)',
            'mean': '箸',
        }, {
            'name': 'knife',
            'mean': 'ナイフ',
        }, {
            'name': 'fork',
            'mean': 'フォーク'
        },
        {
            'name': 'early',
            'mean': '早い',
        }, {
            'name': 'myself',
            'mean': '自分自身',
        }, {
            'name': 'omelet',
            'mean': 'オムレツ'
        }, {
            'name': 'French',
            'mean': 'フランス人、フランス語、フランスの'
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

    textbook_unit = TextbookUnit.objects.get(name="Unit2 Nick Helps a Dog")
    chap1 = textbook_unit.textbookchapter_set.get(name='Part1')
    chap2 = textbook_unit.textbookchapter_set.get(name='Part2')
    chap3 = textbook_unit.textbookchapter_set.get(name='Part3')
    ycdi = textbook_unit.textbookchapter_set.get(name='You Can Do It!')
    unit_words = {
        chap1: ['slow', 'hurt', 'thing', 'vet', 'bike', 'number', 'coin'],
        chap2: ['diary', 'sunny', 'along', 'found', 'find', 'weak', 'shy', 'worried'],
        chap3: ['cloudy', 'news', 'glad', 'lost', 'enter', 'shoe(s)', 'computer', 'bookstore', 'chopstick(s)', 'knife',
                'fork'],
        ycdi: ['early', 'myself', 'omelet', 'French'],
    }
    textbook_words = [{
        'textbook_unit': textbook_unit,
        'textbook_chapter': chapter,
        'word': Word.objects.get(name=word_name),
    } for chapter, words in unit_words.items() for word_name in words]
    base_create(TextbookWord, *textbook_words)
