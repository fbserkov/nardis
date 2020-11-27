from os.path import join

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

from convert import date2str, datetime2str, datetime2str_time, time2str

LEADING = 14
_styles = getSampleStyleSheet()
_styles.add(ParagraphStyle('Normal+', leading=LEADING))  # TODO see 6.2 <para>
_styles.add(ParagraphStyle('Center', leading=LEADING, alignment=TA_CENTER))
_styles.add(ParagraphStyle('Indent', leading=LEADING, leftIndent=12.5 * cm))

pdfmetrics.registerFont(ttfonts.TTFont('arial', 'ArialMT.ttf'))
pdfmetrics.registerFont(ttfonts.TTFont('arialbd', 'Arial-BoldMT.ttf'))

_story = []


def _item_0(db):
    _tbl(
        db.select(0, 'organization'),
        'Медицинская документация\nУчетная форма № 307/у-05\n'
        'Утверждена приказом Министерства\nздравоохранения '
        'Российской Федерации\nот 18 декабря 2015 г. № 933н',
    )
    _spacer(3)
    _liner('Center', 'АКТ')
    _liner('Center', 'медицинского освидетельствования на состояние опьянения')
    _liner('Center', '(алкогольного, наркотического или иного токсического)')
    _liner('Center', '№', f'{db.select(0, "number")}/{db.select(0, "year")}')
    _spacer(2)
    datetime = db.select(4, 'datetime')
    _liner('Normal+', '', datetime.strftime(f'"{datetime.day}" %B %Y г.'))


def _item_1(db):
    _spacer(1)
    _liner('Normal+', '1. Сведения об освидетельствуемом лице:')
    _liner('Normal+', 'Фамилия, имя, отчество', db.select(1, 'full_name'))
    _liner(
        'Normal+', 'Дата рождения', date2str(db.select(1, 'date')))
    _liner('Normal+', 'Адрес места жительства', db.select(1, 'address'))
    _liner(
        'Normal+',
        'Сведения об освидетельствуемом лице заполнены на основании',
        db.select(1, 'document'),
    )


def _item_2(db):
    _spacer(1)
    _liner(
        'Normal+',
        '2. Основание для медицинского освидетельствования',
        db.select(2, 'document'),
    )
    _liner('Normal+', 'Кем направлен', db.select(2, 'full_name'))


def _item_3(db):
    _spacer(1)
    _liner(
        'Normal+',
        '3. Наименование структурного подразделения медицинской организации, '
        'в котором проводится медицинское освидетельствование',
        db.select(3, 'subdivision'),
    )


def _item_4(db):
    _spacer(1)
    _liner(
        'Normal+',
        '4. Дата и точное время начала медицинского освидетельствования',
        datetime2str(db.select(4, 'datetime')),
    )


def _item_5(db):
    _spacer(1)
    _liner('Normal+', '5. Кем освидетельствован', db.select(5, 'doctor'))
    _liner(
        'Normal+',
        'Cведения о прохождении подготовки по вопросам проведения '
        'медицинского освидетельствования (наименование медицинской '
        'организации, дата выдачи документа)',
        db.select(5, 'training'),
    )


def _item_6(db):
    _spacer(1)
    _liner(
        'Normal+',
        '6. Внешний вид освидетельствуемого', db.select(6, 'appearance'),
    )


def _item_7(db):
    _spacer(1)
    _liner(
        'Normal+',
        '7. Жалобы освидетельствуемого на свое состояние',
        db.select(7, 'complaints'),
    )


def _item_8(db):
    _spacer(1)
    _liner(
        'Normal+',
        '8. Изменения психической деятельности освидетельствуемого',
    )
    _liner('Normal+', 'состояние сознания', db.select(8, 'consciousness'))
    _liner('Normal+', 'поведение', db.select(8, 'behavior'))
    _liner(
        'Normal+',
        'ориентировка в месте, времени, ситуации', db.select(8, 'orientation'),
    )
    _liner('Normal+', 'Результат пробы Шульте', db.select(8, 'schulte'))


def _item_9(db):
    _spacer(1)
    _liner('Normal+', '9. Вегетативно-сосудистые реакции освидетельствуемого')
    _liner('Normal+', 'зрачки', db.select(9, 'pupils'))
    _liner('Normal+', 'реакция на свет', db.select(9, 'reaction'))
    _liner('Normal+', 'склеры', db.select(9, 'scleras'))
    _liner('Normal+', 'нистагм', db.select(9, 'nystagmus'))


def _item_10(db):
    _spacer(1)
    _liner('Normal+', '10. Двигательная сфера освидетельствуемого')
    _liner('Normal+', 'речь', db.select(10, 'speech'))
    _liner('Normal+', 'походка', db.select(10, 'gait'))
    _liner('Normal+', 'устойчивость в позе Ромберга', db.select(10, 'romberg'))
    _liner(
        'Normal+',
        'точность выполнения координационных проб',
        db.select(10, 'coordination'),
    )
    _liner('Normal+', 'результат пробы Ташена', db.select(10, 'tashen'))


def _item_11(db):
    _spacer(1)
    _liner(
        'Normal+',
        '11. Наличие заболеваний нервной системы, '
        'психических расстройств, перенесенных травм '
        '(со слов освидетельствуемого)', db.select(11, 'comorbidity'),
    )


def _item_12(db):
    _spacer(1)
    _liner(
        'Normal+',
        '12. Сведения о последнем употреблении алкоголя, '
        'лекарственных средств, наркотических средств и психотропных веществ '
        '(со слов освидетельствуемого)', db.select(12, 'drug_use'),
    )


def _item_13(db):
    _spacer(1)
    _liner(
        'Normal+',
        '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого',
    )
    _liner(
        'Normal+', '13.1 Время первого исследования',
        datetime2str_time(db.select(13, 'datetime_1')),
    )
    _liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db.select(13, 'device_1'),
    )
    _liner('Normal+', 'результат исследования', db.select(13, 'result_1'))
    _liner(
        'Normal+',
        '13.2 Второе исследование через 15-20 минут: время исследования',
        datetime2str_time(db.select(13, 'datetime_2')),
    )
    _liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db.select(13, 'device_2'),
    )
    _liner('Normal+', 'результат исследования', db.select(13, 'result_2'))


def _item_14(db):
    _spacer(1)
    time = time2str(db.select(14, 'time'))
    _liner(
        'Normal+',
        '14. Время отбора биологического объекта '
        'у освидетельствуемого (среда)',
        time + f' ({db.select(14, "material")})' if time else '',
    )
    _liner(
        'Normal+',
        'Результаты химико-токсикологических '
        'исследований биологических объектов',
    )
    _liner('Normal+', 'название лаборатории', db.select(14, 'laboratory'))
    _liner('Normal+', 'методы исследований', db.select(14, 'method'))
    result = db.select(14, 'result')
    _liner(
        'Normal+', 'результаты исследований',
        ', '.join(k + ' ' + v for k, v in result.items())
        if type(result) is dict else result,
    )
    _liner(
        'Normal+',
        'номер справки о результатах химико-токсикологических исследований',
        db.select(14, 'number'),
    )


def _item_15(db):
    _spacer(1)
    _liner(
        'Normal+',
        '15. Другие данные медицинского осмотра или представленных документов',
        db.select(15, 'other'),
    )


def _item_16(db):
    _spacer(1)
    _liner(
        'Normal+',
        '16. Дата и точное время окончания медицинского освидетельствования',
        datetime2str(db.select(16, 'datetime')),
    )


def _item_17(db):
    _spacer(1)
    _liner('Normal+', '17. Медицинское заключение', db.select(17, 'opinion'))
    _liner('Normal+', 'дата его вынесения', date2str(db.select(17, 'date')))


def _item_18(db):
    _spacer(1)
    _liner(
        'Normal+',
        '18. Подпись врача ______________', f'/ {db.select(5, "doctor")} /',
    )
    _liner('Indent', 'М.П.')


def _liner(style, line1, line2=''):
    if line1:
        line1 = '<font name="arial" size=12>' + line1 + '</font>'
    if line2:
        line2 = ' ' + '<font name="arialbd" size=12>' + line2 + '</font>'
    _story.append(Paragraph(line1 + line2, _styles[style]))


def _page_1(canvas, names):
    canvas.setFont('arial', 12)
    canvas.drawString(2.5*cm, 1*cm + 2*LEADING, 'Подпись врача ______________')
    canvas.drawString(14*cm, 1*cm + LEADING, 'М.П.')
    canvas.drawRightString(A4[0] - 1*cm, 1*cm, 'Страница 1 из 2')
    canvas.setFont('arialbd', 12)
    canvas.drawString(9.0 * cm, 1 * cm + 2*LEADING, names)


def _page_2(canvas):
    canvas.setFont('arial', 12)
    canvas.drawString(16.5*cm, 1*cm, 'Страница 2 из 2')


def _spacer(n):
    for i in range(n):
        _story.append(Spacer(1, LEADING))


def _tbl(line1, line2):
    temp = Table([[line1, line2]])
    temp.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (1, 0), 'arial'),
        ('ALIGN', (0, 0), (1, 0), 'CENTER'),
        ('SIZE', (0, 0), (1, 0), 12),
        ('LEADING', (0, 0), (1, 0), LEADING)
    ]))
    _story.append(temp)


def create_pdf(db):
    for i in range(19):
        fnc_name = '_item_' + str(i)
        globals()[fnc_name](db)

    filename = f'{db.select(0, "year")}_{db.select(0, "number"):04}'
    filename += ' ' + db.select(1, 'full_name') + '.pdf'

    SimpleDocTemplate(
        join('acts', filename), leftMargin=1.5*cm, rightMargin=1*cm,
        topMargin=1.5*cm, bottomMargin=3*cm,
    ).build(
        _story,
        onFirstPage=lambda canvas, _: _page_1(
            canvas, f'/ {db.select(5, "doctor")} /'),
        onLaterPages=lambda canvas, _: _page_2(canvas),
    )
