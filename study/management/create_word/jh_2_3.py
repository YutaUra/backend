from study.models import Subject, TextbookUnit
from study.words import Word
from study.words.models import TextbookWord


def word_create():
    from study.management.commands.study_init import base_create

    subject = Subject.objects.get(name='英語')

    words = [
        {
            'name': 'came',
            'mean': 'comeの過去形、来た'
        },
        {
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
        },
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
        },
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
        },
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
    ]
    args = [{
        'subject': subject,
        'name': word['name'],
        'mean': word['mean'],
    } for word in words]
    base_create(Word, *args)


def textbook_word_create():
    from study.management.commands.study_init import base_create

    textbook_unit = TextbookUnit.objects.get(name="Unit1 Tina's Speech")
    chap1 = textbook_unit.textbookchapter_set.get(name='Part1')
    chap2 = textbook_unit.textbookchapter_set.get(name='Part2')
    chap3 = textbook_unit.textbookchapter_set.get(name='Part3')
    ycdi = textbook_unit.textbookchapter_set.get(name='You Can Do It!')
    unit_words = {
        chap1: ['came', 'before', 'city', 'best', 'castle', 'view', 'shopping'],
        chap2: ['was', 'born', 'grew', 'grow', 'spoke', 'language', 'were', 'Mt.', 'kitchen', 'exciting', 'easy',
                'difficult'],
        chap3: ['question', 'group', 'information', 'Internet', 'special', 'friendly'],
        ycdi: ['stadium', 'won', 'win'],
    }
    textbook_words = [{
        'textbook_unit': textbook_unit,
        'textbook_chapter': chapter,
        'word': Word.objects.get(name=word_name),
    } for chapter, words in unit_words.items() for word_name in words]
    base_create(TextbookWord, *textbook_words)
