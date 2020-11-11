import locale

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

from convert import date2str, datetime2str, datetime2str_time, time2str

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
    item_8(db)
    item_9(db)
    item_10(db)
    item_11(db)
    item_12(db)
    item_13(db)
    item_14(db)
    item_15(db)
    item_16(db)
    item_17(db)
    item_18(db)

    SimpleDocTemplate(
        filename, leftMargin=1.5*cm, rightMargin=1*cm,
        topMargin=1.5*cm, bottomMargin=3*cm,
    ).build(
        story,
        onFirstPage=lambda canvas, _: page_1(
            canvas, f'/ {db.select(5, "doctor")} /'),
        onLaterPages=lambda canvas, _: page_2(canvas),
    )


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
    liner('Center', '№', f'{db.select(0, "number")}/{db.select(0, "year")}')
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
        db.select(3, 'subdivision'),
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
    liner('Normal+', 'состояние сознания', db.select(8, 'consciousness'))
    liner('Normal+', 'поведение', db.select(8, 'behavior'))
    liner(
        'Normal+',
        'ориентировка в месте, времени, ситуации', db.select(8, 'orientation'),
    )
    liner('Normal+', 'Результат пробы Шульте', db.select(8, 'schulte'))


def item_9(db):
    spacer(1)
    liner('Normal+', '9. Вегетативно-сосудистые реакции освидетельствуемого')
    liner('Normal+', 'зрачки', db.select(9, 'pupils'))
    liner('Normal+', 'реакция на свет', db.select(9, 'reaction'))
    liner('Normal+', 'склеры', db.select(9, 'scleras'))
    liner('Normal+', 'нистагм', db.select(9, 'nystagmus'))


def item_10(db):
    spacer(1)
    liner('Normal+', '10. Двигательная сфера освидетельствуемого')
    liner('Normal+', 'речь', db.select(10, 'speech'))
    liner('Normal+', 'походка', db.select(10, 'gait'))
    liner('Normal+', 'устойчивость в позе Ромберга', db.select(10, 'romberg'))
    liner(
        'Normal+',
        'точность выполнения координационных проб',
        db.select(10, 'coordination'),
    )
    liner('Normal+', 'результат пробы Ташена', db.select(10, 'tashen'))


def item_11(db):
    spacer(1)
    liner(
        'Normal+',
        '11. Наличие заболеваний нервной системы, '
        'психических расстройств, перенесенных травм '
        '(со слов освидетельствуемого)', db.select(11, 'comorbidity'),
    )


def item_12(db):
    spacer(1)
    liner(
        'Normal+',
        '12. Сведения о последнем употреблении алкоголя, '
        'лекарственных средств, наркотических средств и психотропных веществ '
        '(со слов освидетельствуемого)', db.select(12, 'drug_use'),
    )


def item_13(db):
    spacer(1)
    liner(
        'Normal+',
        '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого',
    )
    liner(
        'Normal+', '13.1 Время первого исследования',
        datetime2str_time(db.select(13, 'datetime_1')),
    )
    liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db.select(13, 'device_1'),
    )
    liner('Normal+', 'результат исследования', db.select(13, 'result_1'))
    liner(
        'Normal+',
        '13.2 Второе исследование через 15-20 минут: время исследования',
        datetime2str_time(db.select(13, 'datetime_2')),
    )
    liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        db.select(13, 'device_2'),
    )
    liner('Normal+', 'результат исследования', db.select(13, 'result_2'))


def item_14(db):
    spacer(1)
    time = time2str(db.select(14, 'time'))
    liner(
        'Normal+',
        '14. Время отбора биологического объекта '
        'у освидетельствуемого (среда)',
        time + f' ({db.select(14, "material")})' if time else '',
    )
    liner(
        'Normal+',
        'Результаты химико-токсикологических '
        'исследований биологических объектов',
    )
    liner('Normal+', 'название лаборатории', db.select(14, 'laboratory'))
    liner('Normal+', 'методы исследований', db.select(14, 'method'))
    liner('Normal+', 'результаты исследований', db.select(14, 'result'))
    liner(
        'Normal+',
        'номер справки о результатах химико-токсикологических исследований',
        db.select(14, 'number'),
    )


def item_15(db):
    spacer(1)
    liner(
        'Normal+',
        '15. Другие данные медицинского осмотра или представленных документов',
        db.select(15, 'other'),
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
    liner('Normal+', '17. Медицинское заключение', db.select(17, 'opinion'))
    liner('Normal+', 'дата его вынесения', date2str(db.select(17, 'date')))


def item_18(db):
    spacer(1)
    liner(
        'Normal+',
        '18. Подпись врача ______________', f'/ {db.select(5, "doctor")} /',
    )
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
