import locale

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle('Normal+', leading=14))
styles.add(ParagraphStyle('Center', leading=14, alignment=TA_CENTER))
styles.add(ParagraphStyle('Indent', leading=14, leftIndent=12.5*cm))

pdfmetrics.registerFont(ttfonts.TTFont('arial', 'ArialMT.ttf'))
pdfmetrics.registerFont(ttfonts.TTFont('arialbd', 'Arial-BoldMT.ttf'))

story = []


def create_pdf(filename, db):
    item_0(db)
    item_1(db)
    item_2(db)
    item_3(db)
    item_4(db)
    item_5(db)
    item_6(db)
    item_7(db)

    db_ = db.reports[-1]  # TODO delete
    item_8(db_)
    item_9(db_)
    item_10(db_)
    item_11(db_)
    item_12(db_)
    item_13(db_)
    item_14(db_)
    item_15(db_)
    item_16(db)
    item_17(db_)
    item_18(db_)

    SimpleDocTemplate(
        filename, leftMargin=1.5*cm, rightMargin=1*cm,
        topMargin=1.5*cm, bottomMargin=3*cm,
    ).build(
        story,
        onFirstPage=lambda canvas, _: page_1(canvas, f'/ {db_[5][0]} /'),
        onLaterPages=lambda canvas, _: page_2(canvas),
    )


def date2str(date):
    if date is None:
        return ''
    return date.strftime('%d.%m.%Y')


def datetime2str(datetime):
    if datetime is None:
        return ''
    return datetime.strftime('%d.%m.%Y %H:%M')


def item_0(db):
    tbl(
        db.select(0, 'organization'),
        'Медицинская документация\nУчетная форма № 307/у-05\n'
        'Утверждена приказом Министерства\nздравоохранения '
        'Российской Федерации\nот 18 декабря 2015 г. № 933н',
    )
    spacer(3)
    liner('Center', 'АКТ')
    liner('Center', 'медицинского освидетельствования на состояние опьянения')
    liner('Center', '(алкогольного, наркотического или иного токсического)')
    liner('Center', '№', db.select(0, 'act_number'))
    spacer(2)
    datetime = db.select(4, 'datetime')
    liner('Normal+', '', datetime.strftime(f'"{datetime.day}" %B %Y г.'))


def item_1(db):
    spacer(1)
    liner('Normal+', '1. Сведения об освидетельствуемом лице:')
    liner('Normal+', 'Фамилия, имя, отчество', db.select(1, 'full_name'))
    liner(
        'Normal+', 'Дата рождения', date2str(db.select(1, 'date')))
    liner('Normal+', 'Адрес места жительства', db.select(1, 'address'))
    liner(
        'Normal+',
        'Сведения об освидетельствуемом лице заполнены на основании',
        db.select(1, 'document'),
    )


def item_2(db):
    spacer(1)
    liner(
        'Normal+',
        '2. Основание для медицинского освидетельствования',
        db.select(2, 'document'),
    )
    liner('Normal+', 'Кем направлен', db.select(2, 'full_name'))


def item_3(db):
    spacer(1)
    liner(
        'Normal+',
        '3. Наименование структурного подразделения медицинской организации, '
        'в котором проводится медицинское освидетельствование',
        db.select(3, 'unit_name'),
    )


def item_4(db):
    spacer(1)
    liner(
        'Normal+',
        '4. Дата и точное время начала медицинского освидетельствования',
        datetime2str(db.select(4, 'datetime')),
    )


def item_5(db):
    spacer(1)
    liner('Normal+', '5. Кем освидетельствован', db.select(5, 'doctor'))
    liner(
        'Normal+',
        'Cведения о прохождении подготовки по вопросам проведения '
        'медицинского освидетельствования (наименование медицинской '
        'организации, дата выдачи документа)',
        db.select(5, 'training'),
    )


def item_6(db):
    spacer(1)
    liner(
        'Normal+',
        '6. Внешний вид освидетельствуемого', db.select(6, 'appearance'),
    )


def item_7(db):
    spacer(1)
    liner(
        'Normal+',
        '7. Жалобы освидетельствуемого на свое состояние',
        db.select(7, 'complaints'),
    )


def item_8(db):
    spacer(1)
    liner(
        'Normal+',
        '8. Изменения психической деятельности освидетельствуемого',
    )
    liner('Normal+', 'состояние сознания', db[8][0])
    liner('Normal+', 'поведение', db[8][1])
    liner('Normal+', 'ориентировка в месте, времени, ситуации', db[8][2])
    liner('Normal+', 'Результат пробы Шульте', db[8][3])


def item_9(db):
    spacer(1)
    liner('Normal+', '9. Вегетативно-сосудистые реакции освидетельствуемого')
    liner('Normal+', 'зрачки', db[9][0])
    liner('Normal+', 'реакция на свет', db[9][1])
    liner('Normal+', 'склеры', db[9][2])
    liner('Normal+', 'нистагм', db[9][3])


def item_10(db):
    spacer(1)
    liner('Normal+', '10. Двигательная сфера освидетельствуемого')
    liner('Normal+', 'речь', db[10][0])
    liner('Normal+', 'походка', db[10][1])
    liner('Normal+', 'устойчивость в позе Ромберга', db[10][2])
    liner('Normal+', 'точность выполнения координационных проб', db[10][3])
    liner('Normal+', 'результат пробы Ташена', db[10][4])


def item_11(db):
    spacer(1)
    liner(
        'Normal+',
        '11. Наличие заболеваний нервной системы, психических расстройств, '
        'перенесенных травм (со слов освидетельствуемого)', db[11],
    )


def item_12(db):
    spacer(1)
    liner(
        'Normal+',
        '12. Сведения о последнем употреблении алкоголя, '
        'лекарственных средств, наркотических средств и психотропных веществ '
        '(со слов освидетельствуемого)', db[12],
    )


def item_13(db):
    spacer(1)
    liner(
        'Normal+',
        '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого',
    )
    liner('Normal+', '13.1 Время первого исследования', db[13][0])
    liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db[13][2],
    )
    liner('Normal+', 'результат исследования', db[13][1])
    liner(
        'Normal+',
        '13.2 Второе исследование через 15-20 минут: время исследования',
        db[13][3],
    )
    liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db[13][5],
    )
    liner('Normal+', 'результат исследования', db[13][4])


def item_14(db):
    spacer(1)
    liner(
        'Normal+',
        '14. Время отбора биологического объекта '
        'у освидетельствуемого (среда)', db[14][0],
    )
    liner(
        'Normal+',
        'Результаты химико-токсикологических '
        'исследований биологических объектов',
    )
    liner('Normal+', 'название лаборатории', db[14][1])
    liner('Normal+', 'методы исследований', db[14][2])
    liner('Normal+', 'результаты исследований', db[14][4])
    liner(
        'Normal+',
        'номер справки о результатах химико-токсикологических исследований',
        db[14][3],
    )


def item_15(db):
    spacer(1)
    liner(
        'Normal+',
        '15. Другие данные медицинского осмотра или представленных документов',
        db[15],
    )


def item_16(db):
    spacer(1)
    liner(
        'Normal+',
        '16. Дата и точное время окончания медицинского освидетельствования',
        datetime2str(db.select(16, 'datetime')),
    )


def item_17(db):
    spacer(1)
    liner('Normal+', '17. Медицинское заключение', db[17][0])
    liner('Normal+', 'дата его вынесения', db[17][1])


def item_18(db):
    spacer(1)
    liner('Normal+', '18. Подпись врача ______________', f'/ {db[5][0]} /')
    liner('Indent', 'М.П.')


def liner(style, line1, line2=''):
    if line1:
        line1 = '<font name="arial" size=12>' + line1 + '</font>'
    if line2:
        line2 = ' ' + '<font name="arialbd" size=12>' + line2 + '</font>'
    story.append(Paragraph(line1 + line2, styles[style]))


def page_1(canvas, names):
    canvas.setFont('arial', 12)
    canvas.drawString(2.5*cm, 1*cm + 28, 'Подпись врача ______________')
    canvas.drawString(14.0*cm, 1*cm + 14, 'М.П.')
    canvas.drawString(16.5*cm, 1*cm, 'Страница 1 из 2')
    canvas.setFont('arialbd', 12)
    canvas.drawString(9.0 * cm, 1 * cm + 28, names)


def page_2(canvas):
    canvas.setFont('arial', 12)
    canvas.drawString(16.5*cm, 1*cm, 'Страница 2 из 2')


def spacer(n):
    for i in range(n):
        story.append(Spacer(1, 14))


def tbl(line1, line2):
    temp = Table([[line1, line2]])
    temp.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (1, 0), 'arial'),
        ('ALIGN', (0, 0), (1, 0), 'CENTER'),
        ('SIZE', (0, 0), (1, 0), 12),
        ('LEADING', (0, 0), (1, 0), 14)
    ]))
    story.append(temp)
