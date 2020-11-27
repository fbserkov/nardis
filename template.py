from os.path import join

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import ttfonts
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

from convert import date2str, datetime2str, datetime2str_time, time2str

LEADING, SIZE = 14, 12
_story = []

registerFont(ttfonts.TTFont('Arial', join('fonts', 'ArialMT.ttf')))
registerFont(ttfonts.TTFont('ArialBd', join('fonts', 'Arial-BoldMT.ttf')))
registerFontFamily('Arial', normal='Arial', bold='ArialBd')


def _item_0(db):
    _tbl(
        db.select(0, 'organization'),
        'Медицинская документация\nУчетная форма № 307/у-05\n'
        'Утверждена приказом Министерства\nздравоохранения '
        'Российской Федерации\nот 18 декабря 2015 г. № 933н',
    )
    _spacer(3)
    _liner('АКТ', is_centered=True)
    _liner(
        'медицинского освидетельствования на состояние опьянения',
        is_centered=True,
    )
    _liner(
        '(алкогольного, наркотического или иного токсического)',
        is_centered=True,
    )
    _liner(
        '№', str(db.select(0, 'number')) + '/' + str(db.select(0, 'year')),
        is_centered=True,
    )
    _spacer(2)
    datetime = db.select(4, 'datetime')
    _liner('', datetime.strftime(f'"{datetime.day}" %B %Y г.'))


def _item_1(db):
    _spacer(1)
    _liner('1. Сведения об освидетельствуемом лице:')
    _liner('Фамилия, имя, отчество', db.select(1, 'full_name'))
    _liner('Дата рождения', date2str(db.select(1, 'date')))
    _liner('Адрес места жительства', db.select(1, 'address'))
    _liner(
        'Сведения об освидетельствуемом лице заполнены на основании',
        db.select(1, 'document'),
    )


def _item_2(db):
    _spacer(1)
    _liner(
        '2. Основание для медицинского освидетельствования',
        db.select(2, 'document'),
    )
    _liner('Кем направлен', db.select(2, 'full_name'))


def _item_3(db):
    _spacer(1)
    _liner(
        '3. Наименование структурного подразделения медицинской организации, '
        'в котором проводится медицинское освидетельствование',
        db.select(3, 'subdivision'),
    )


def _item_4(db):
    _spacer(1)
    _liner(
        '4. Дата и точное время начала медицинского освидетельствования',
        datetime2str(db.select(4, 'datetime')),
    )


def _item_5(db):
    _spacer(1)
    _liner('5. Кем освидетельствован', db.select(5, 'doctor'))
    _liner(
        'Cведения о прохождении подготовки по вопросам проведения '
        'медицинского освидетельствования (наименование медицинской '
        'организации, дата выдачи документа)', db.select(5, 'training'),
    )


def _item_6(db):
    _spacer(1)
    _liner('6. Внешний вид освидетельствуемого', db.select(6, 'appearance'))


def _item_7(db):
    _spacer(1)
    _liner(
        '7. Жалобы освидетельствуемого на свое состояние',
        db.select(7, 'complaints'),
    )


def _item_8(db):
    _spacer(1)
    _liner('8. Изменения психической деятельности освидетельствуемого')
    _liner('состояние сознания', db.select(8, 'consciousness'))
    _liner('поведение', db.select(8, 'behavior'))
    _liner(
        'ориентировка в месте, времени, ситуации', db.select(8, 'orientation'))
    _liner('Результат пробы Шульте', db.select(8, 'schulte'))


def _item_9(db):
    _spacer(1)
    _liner('9. Вегетативно-сосудистые реакции освидетельствуемого')
    _liner('зрачки', db.select(9, 'pupils'))
    _liner('реакция на свет', db.select(9, 'reaction'))
    _liner('склеры', db.select(9, 'scleras'))
    _liner('нистагм', db.select(9, 'nystagmus'))


def _item_10(db):
    _spacer(1)
    _liner('10. Двигательная сфера освидетельствуемого')
    _liner('речь', db.select(10, 'speech'))
    _liner('походка', db.select(10, 'gait'))
    _liner('устойчивость в позе Ромберга', db.select(10, 'romberg'))
    _liner(
        'точность выполнения координационных проб',
        db.select(10, 'coordination'),
    )
    _liner('результат пробы Ташена', db.select(10, 'tashen'))


def _item_11(db):
    _spacer(1)
    _liner(
        '11. Наличие заболеваний нервной системы, '
        'психических расстройств, перенесенных травм '
        '(со слов освидетельствуемого)', db.select(11, 'comorbidity'),
    )


def _item_12(db):
    _spacer(1)
    _liner(
        '12. Сведения о последнем употреблении алкоголя, '
        'лекарственных средств, наркотических средств и психотропных веществ '
        '(со слов освидетельствуемого)', db.select(12, 'drug_use'),
    )


def _item_13(db):
    _spacer(1)
    _liner('13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого')
    _liner(
        '13.1 Время первого исследования',
        datetime2str_time(db.select(13, 'datetime_1')),
    )
    _liner(
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db.select(13, 'device_1'),
    )
    _liner('результат исследования', db.select(13, 'result_1'))
    _liner(
        '13.2 Второе исследование через 15-20 минут: время исследования',
        datetime2str_time(db.select(13, 'datetime_2')),
    )
    _liner(
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db.select(13, 'device_2'),
    )
    _liner('результат исследования', db.select(13, 'result_2'))


def _item_14(db):
    _spacer(1)
    time = time2str(db.select(14, 'time'))
    _liner(
        '14. Время отбора биологического объекта '
        'у освидетельствуемого (среда)',
        time + f' ({db.select(14, "material")})' if time else '',
    )
    _liner(
        'Результаты химико-токсикологических '
        'исследований биологических объектов'
    )
    _liner('название лаборатории', db.select(14, 'laboratory'))
    _liner('методы исследований', db.select(14, 'method'))
    result = db.select(14, 'result')
    _liner(
        'результаты исследований',
        ', '.join(k + ' ' + v for k, v in result.items())
        if type(result) is dict else result,
    )
    _liner(
        'номер справки о результатах химико-токсикологических исследований',
        db.select(14, 'number'),
    )


def _item_15(db):
    _spacer(1)
    _liner(
        '15. Другие данные медицинского осмотра или представленных документов',
        db.select(15, 'other'),
    )


def _item_16(db):
    _spacer(1)
    _liner(
        '16. Дата и точное время окончания медицинского освидетельствования',
        datetime2str(db.select(16, 'datetime')),
    )


def _item_17(db):
    _spacer(1)
    _liner('17. Медицинское заключение', db.select(17, 'opinion'))
    _liner('дата его вынесения', date2str(db.select(17, 'date')))


def _item_18(db):
    _spacer(1)
    _liner('18. Подпись врача ______________', f'/ {db.select(5, "doctor")} /')
    _liner('М.П.', is_indented=True)


def _liner(text, bold='', is_centered=False, is_indented=False):
    if bold:
        text += ' ' + f'<b>{bold}</b>'
    attributes = f'fontName=Arial fontSize={SIZE}'
    attributes += f' leading={LEADING}'
    if is_centered:
        attributes += ' alignment=center'
    if is_indented:
        attributes += f' leftIndent={12.5*cm}'
    _story.append(Paragraph(f'<para {attributes}>' + text + '</para>'))


def _page_1(canvas, names):
    canvas.setFont('Arial', SIZE)
    canvas.drawString(2.5*cm, 1*cm + 2*LEADING, 'Подпись врача ______________')
    canvas.drawString(14*cm, 1*cm + LEADING, 'М.П.')
    canvas.drawRightString(A4[0] - 1*cm, 1*cm, 'Страница 1 из 2')
    canvas.setFont('ArialBd', SIZE)
    canvas.drawString(9.0 * cm, 1 * cm + 2*LEADING, names)


def _page_2(canvas):
    canvas.setFont('Arial', SIZE)
    canvas.drawString(16.5*cm, 1*cm, 'Страница 2 из 2')


def _spacer(n):
    for i in range(n):
        _story.append(Spacer(1, LEADING))


def _tbl(line1, line2):
    temp = Table([[line1, line2]])
    temp.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (1, 0), 'Arial'),
        ('ALIGN', (0, 0), (1, 0), 'CENTER'),
        ('SIZE', (0, 0), (1, 0), SIZE),
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
        onFirstPage=lambda canvas, _: _page_1(  # TODO do not need lambda (5.2)
            canvas, f'/ {db.select(5, "doctor")} /'),
        onLaterPages=lambda canvas, _: _page_2(canvas),
    )
