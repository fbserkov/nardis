from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle('Normal+', leading=14))
styles.add(ParagraphStyle('Center', leading=14, alignment=TA_CENTER))
styles.add(ParagraphStyle('Indent', leading=14, leftIndent=12.5*cm))

pdfmetrics.registerFont(ttfonts.TTFont('arial', 'ArialMT.ttf'))
pdfmetrics.registerFont(ttfonts.TTFont('arialbd', 'Arial-BoldMT.ttf'))

story = []


def create_pdf(filename, data):
    report = data.reports[-1]  # TODO delete

    tbl(
        data.select(0, 'organization'),
        'Медицинская документация\nУчетная форма № 307/у-05\n'
        'Утверждена приказом Министерства\nздравоохранения '
        'Российской Федерации\nот 18 декабря 2015 г. № 933н',
    )
    spacer(3)
    liner('Center', 'АКТ')
    liner('Center', 'медицинского освидетельствования на состояние опьянения')
    liner('Center', '(алкогольного, наркотического или иного токсического)')
    liner('Center', '№', data.select(0, 'act_number'))
    spacer(2)
    liner('Normal+', '', '')  # TODO !? rus local for format_date(report[4][0])

    spacer(1)
    liner('Normal+', '1. Сведения об освидетельствуемом лице:')
    liner('Normal+', 'Фамилия, имя, отчество', data.select(1, 'full_name'))
    date = data.select(1, 'date')
    liner(
        'Normal+', 'Дата рождения', date.strftime('%d.%m.%Y') if date else '')
    liner('Normal+', 'Адрес места жительства', data.select(1, 'address'))
    liner(
        'Normal+',
        'Сведения об освидетельствуемом лице заполнены на основании',
        data.select(1, 'document'),
    )

    spacer(1)
    liner(
        'Normal+',
        '2. Основание для медицинского освидетельствования',
        data.select(2, 'document'),
    )
    liner('Normal+', 'Кем направлен', data.select(2, 'full_name'))

    spacer(1)
    liner(
        'Normal+',
        '3. Наименование структурного подразделения медицинской организации, '
        'в котором проводится медицинское освидетельствование',
        data.select(3, 'unit_name'),
    )

    spacer(1)
    date, time = data.select(4, 'date'), data.select(4, 'time')
    liner(
        'Normal+',
        '4. Дата и точное время начала медицинского освидетельствования',
        (date.strftime('%d.%m.%Y') if date else '') +
        ' ' + (time.strftime('%H:%M') if time else ''),
    )

    spacer(1)
    liner('Normal+', '5. Кем освидетельствован', report[5][0])
    liner(
        'Normal+',
        'Cведения о прохождении подготовки по вопросам проведения '
        'медицинского освидетельствования (наименование медицинской '
        'организации, дата выдачи документа)',
        report[5][1],
    )

    spacer(1)
    liner('Normal+', '6. Внешний вид освидетельствуемого', report[6])

    spacer(1)
    liner(
        'Normal+',
        '7. Жалобы освидетельствуемого на свое состояние',
        report[7],
    )

    spacer(1)
    liner(
        'Normal+',
        '8. Изменения психической деятельности освидетельствуемого',
    )
    liner('Normal+', 'состояние сознания', report[8][0])
    liner('Normal+', 'поведение', report[8][1])
    liner('Normal+', 'ориентировка в месте, времени, ситуации', report[8][2])
    liner('Normal+', 'Результат пробы Шульте', report[8][3])

    spacer(1)
    liner('Normal+', '9. Вегетативно-сосудистые реакции освидетельствуемого')
    liner('Normal+', 'зрачки', report[9][0])
    liner('Normal+', 'реакция на свет', report[9][1])
    liner('Normal+', 'склеры', report[9][2])
    liner('Normal+', 'нистагм', report[9][3])

    spacer(1)
    liner('Normal+', '10. Двигательная сфера освидетельствуемого')
    liner('Normal+', 'речь', report[10][0])
    liner('Normal+', 'походка', report[10][1])
    liner('Normal+', 'устойчивость в позе Ромберга', report[10][2])
    liner('Normal+', 'точность выполнения координационных проб', report[10][3])
    liner('Normal+', 'результат пробы Ташена', report[10][4])

    spacer(1)
    liner(
        'Normal+',
        '11. Наличие заболеваний нервной системы, психических расстройств, '
        'перенесенных травм (со слов освидетельствуемого)', report[11],
    )

    spacer(1)
    liner(
        'Normal+',
        '12. Сведения о последнем употреблении алкоголя, '
        'лекарственных средств, наркотических средств и психотропных веществ '
        '(со слов освидетельствуемого)', report[12],
    )

    spacer(1)
    liner(
        'Normal+',
        '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого',
    )
    liner('Normal+', '13.1 Время первого исследования', report[13][0])
    liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        report[13][2],
    )
    liner('Normal+', 'результат исследования', report[13][1])
    liner(
        'Normal+',
        '13.2 Второе исследование через 15-20 минут: время исследования',
        report[13][3],
    )
    liner(
        'Normal+',
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения',
        report[13][5],
    )
    liner('Normal+', 'результат исследования', report[13][4])

    spacer(1)
    liner(
        'Normal+',
        '14. Время отбора биологического объекта '
        'у освидетельствуемого (среда)', report[14][0],
    )
    liner(
        'Normal+',
        'Результаты химико-токсикологических '
        'исследований биологических объектов',
    )
    liner('Normal+', 'название лаборатории', report[14][1])
    liner('Normal+', 'методы исследований', report[14][2])
    liner('Normal+', 'результаты исследований', report[14][4])
    liner(
        'Normal+',
        'номер справки о результатах химико-токсикологических исследований',
        report[14][3],
    )

    spacer(1)
    liner(
        'Normal+',
        '15. Другие данные медицинского осмотра или представленных документов',
        report[15],
    )

    spacer(1)
    date, time = data.select(16, 'date'), data.select(16, 'time')
    liner(
        'Normal+',
        '16. Дата и точное время окончания медицинского освидетельствования',
        (date.strftime('%d.%m.%Y') if date else '') +
        ' ' + (time.strftime('%H:%M') if time else ''),
    )

    spacer(1)
    liner('Normal+', '17. Медицинское заключение', report[17][0])
    liner('Normal+', 'дата его вынесения', report[17][1])

    spacer(1)
    names = '/ ' + report[5][0] + ' /'
    liner('Normal+', '18. Подпись врача ______________', names)
    liner('Indent', 'М.П.')

    SimpleDocTemplate(
        filename, leftMargin=1.5*cm, rightMargin=1*cm,
        topMargin=1.5*cm, bottomMargin=3*cm,
    ).build(
        story,
        onFirstPage=lambda canvas, _: page_1(canvas, names),
        onLaterPages=lambda canvas, _: page_2(canvas),
    )


def format_date(date):
    if not date:
        return ''
    day, month, year = date.split('.')
    month_words = (
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря',
    )
    return f'"{int(day)}" {month_words[int(month) - 1]} {year} г.'


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


def liner(style, line1, line2=''):
    if line1:
        line1 = '<font name="arial" size=12>' + line1 + '</font>'
    if line2:
        line2 = ' ' + '<font name="arialbd" size=12>' + line2 + '</font>'
    story.append(Paragraph(line1 + line2, styles[style]))


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
