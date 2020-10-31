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
    report = data.reports[-1]
    data_ = [[f'{j}-{i}' for i in range(5)] for j in range(19)]

    tbl(
        data.settings['Организация'],  # TODO !!!
        'Медицинская документация\nУчетная форма № 307/у-05\n'
        'Утверждена приказом Министерства\nздравоохранения '
        'Российской Федерации\nот 18 декабря 2015 г. № 933н',
    )
    spacer(3)
    liner('Center', 'АКТ')
    liner('Center', 'медицинского освидетельствования на состояние опьянения')
    liner('Center', '(алкогольного, наркотического или иного токсического)')
    liner('Center', '№', report[0])
    spacer(2)
    liner('Normal+', '', format_date(report[4][0]))

    spacer(1)
    liner('Normal+', '1. Сведения об освидетельствуемом лице:')
    liner('Normal+', 'Фамилия, имя, отчество', report[1][0])
    liner('Normal+', 'Дата рождения', report[1][1])
    liner('Normal+', 'Адрес места жительства', report[1][2])
    liner(
        'Normal+',
        'Сведения об освидетельствуемом лице заполнены на основании',
        report[1][3],
    )

    spacer(1)
    liner(
        'Normal+',
        '2. Основание для медицинского освидетельствования',
        report[2][0],
    )
    liner('Normal+', 'Кем направлен', report[2][1])

    spacer(1)
    liner(
        'Normal+',
        '3. Наименование структурного подразделения медицинской организации, '
        'в котором проводится медицинское освидетельствование',
        report[3],
    )

    spacer(1)
    liner(
        'Normal+',
        '4. Дата и точное время начала медицинского освидетельствования',
        report[4][0] + ' ' + report[4][1],
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
    liner('Normal+', 'состояние сознания', data_[8][0])
    liner('Normal+', 'поведение', data_[8][1])
    liner('Normal+', 'ориентировка в месте, времени, ситуации', data_[8][2])
    liner('Normal+', 'Результат пробы Шульте', data_[8][3])

    spacer(1)
    liner('Normal+', '9. Вегетативно-сосудистые реакции освидетельствуемого')
    liner('Normal+', 'зрачки', data_[9][0])
    liner('Normal+', 'реакция на свет', data_[9][1])
    liner('Normal+', 'склеры', data_[9][2])
    liner('Normal+', 'нистагм', data_[9][3])

    spacer(1)
    liner('Normal+', '10. Двигательная сфера освидетельствуемого')
    liner('Normal+', 'речь', data_[10][0])
    liner('Normal+', 'походка', data_[10][1])
    liner('Normal+', 'устойчивость в позе Ромберга', data_[10][2])
    liner('Normal+', 'точность выполнения координационных проб', data_[10][3])
    liner('Normal+', 'результат пробы Ташена', data_[10][4])

    spacer(1)
    liner(
        'Normal+',
        '11. Наличие заболеваний нервной системы, психических расстройств, '
        'перенесенных травм (со слов освидетельствуемого)',
        data_[11][0],
    )

    spacer(1)
    liner(
        'Normal+',
        '12. Сведения о последнем употреблении алкоголя, '
        'лекарственных средств, наркотических средств и психотропных веществ '
        '(со слов освидетельствуемого)',
        data_[12][0],
    )

    spacer(1)
    liner(
        'Normal+',
        '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого',
    )
    liner(
        'Normal+',
        '13.1 Время первого исследования, '
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения, результат исследования',
        data_[13][0],
    )
    liner(
        'Normal+',
        '13.2 Второе исследование через 15-20 минут: время исследования, '
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения, результат исследования',
        data_[13][1],
    )

    spacer(1)
    liner(
        'Normal+',
        '14. Время отбора биологического объекта '
        'у освидетельствуемого (среда)',
        data_[14][0],
    )
    liner(
        'Normal+',
        'Результаты химико-токсикологических исследований '
        'биологических объектов (название лаборатории, методы исследований, '
        'результаты исследований, номер справки о результатах '
        'химико-токсикологических исследований)',
        data_[14][1],
    )

    spacer(1)
    liner(
        'Normal+',
        '15. Другие данные медицинского осмотра или представленных документов',
        data_[15][0],
    )

    spacer(1)
    liner(
        'Normal+',
        '16. Дата и точное время окончания медицинского освидетельствования',
        data_[16][0],
    )

    spacer(1)
    liner('Normal+', '17. Медицинское заключение', data_[17][0])
    liner('Normal+', 'дата его вынесения', data_[17][1])

    spacer(1)
    liner('Normal+', '18. Подпись врача ______________', data_[18][0])
    liner('Indent', 'М.П.')

    SimpleDocTemplate(
        filename, leftMargin=1.5*cm, rightMargin=1*cm,
        topMargin=1.5*cm, bottomMargin=3*cm,
    ).build(
        story,
        onFirstPage=lambda canvas, _: page_1(canvas, data_[18][0]),
        onLaterPages=lambda canvas, _: page_2(canvas),
    )


def format_date(date):
    day, month, year = date.split('.')
    month_words = (
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря',
    )
    return f'"{int(day)}" {month_words[int(month) - 1]} {year} г.'


def page_1(canvas, signature):
    canvas.setFont('arial', 12)
    canvas.drawString(2.5*cm, 1*cm + 28, 'Подпись врача ______________')
    canvas.drawString(14.0*cm, 1*cm + 14, 'М.П.')
    canvas.drawString(16.5*cm, 1*cm, 'Страница 1 из 2')
    canvas.setFont('arialbd', 12)
    canvas.drawString(9.0*cm, 1*cm + 28, signature)


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
