from study.models import Subject, TextbookUnit
from study.words import Word
from study.words.models import TextbookWord


def word_create():
    from study.management.commands.study_init import base_create

    subject = Subject.objects.get(name='英語')

    words = [
        {
            'name': 'porch',
            'mean': '玄関'
        },
        {
            'name': 'said',
            'mean': 'sayの過去形、言った',
        }, {
            'name': 'matter',
            'mean': '問題',
        }, {
            'name': 'always',
            'mean': 'いつも',
        }, {
            'name': 'unhappy',
            'mean': '不幸な',
        }, {
            'name': 'never',
            'mean': 'どんなときでも～ない',
        }, {
            'name': 'ever',
            'mean': '今までに',
        }, {
            'name': 'sat',
            'mean': 'sitの過去形、座った',
        }, {
            'name': 'envelope',
            'mean': '封筒',
        }, {
            'name': 'out',
            'mean': '外へ',
        }, {
            'name': 'ran',
            'mean': 'runの過去形、走った',
        }, {
            'name': 'nap',
            'mean': 'うたた寝',
        }, {
            'name': 'window',
            'mean': '窓',
        }, {
            'name': 'silly',
            'mean': 'ばかな',
        }, {
            'name': 'other',
            'mean': '他の',
        }, {
            'name': 'sent',
            'mean': '送る',
        }, {
            'name': 'send',
            'mean': 'sentの過去形、送った',
        }, {
            'name': 'deliver',
            'mean': '配達する',
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

    textbook_unit = TextbookUnit.objects.get(name="Let's Read 1 The Letter")
    page1 = textbook_unit.textbookchapter_set.get(name='Page1')
    page2 = textbook_unit.textbookchapter_set.get(name='Page2')
    page3 = textbook_unit.textbookchapter_set.get(name='Page3')
    page4 = textbook_unit.textbookchapter_set.get(name='Page4')
    page5 = textbook_unit.textbookchapter_set.get(name='Page5')
    unit_words = {
        page1: ['porch', 'said', 'matter', 'always', 'unhappy', 'never', 'ever', 'sat'],
        page2: ['envelope', 'out'],
        page3: ['ran', 'nap', 'window', 'silly', 'other'],
        page4: ['sent', 'send'],
        page5: ['deliver'],
    }
    textbook_words = [{
        'textbook_unit': textbook_unit,
        'textbook_chapter': chapter,
        'word': Word.objects.get(name=word_name),
    } for chapter, words in unit_words.items() for word_name in words]
    base_create(TextbookWord, *textbook_words)
