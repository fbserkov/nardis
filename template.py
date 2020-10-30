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


def tbl(line1, line2):
    temp = Table([[line1, line2]])
    temp.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (1, 0), 'arial'),
        ('ALIGN', (0, 0), (1, 0), 'CENTER'),
        ('SIZE', (0, 0), (1, 0), 12),
        ('LEADING', (0, 0), (1, 0), 14)
    ]))
    story.append(temp)


def spcr(n):
    for i in range(n):
        story.append(Spacer(1, 14))


def prgr(style, line1, line2=''):
    if line1:
        line1 = '<font name="arial" size=12>' + line1 + '</font>'
    if line2:
        line2 = ' ' + '<font name="arialbd" size=12>' + line2 + '</font>'
    story.append(Paragraph(line1 + line2, styles[style]))


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


def create_pdf(filename, data):
    report = data.reports[-1]
    data_ = [[f'{j}-{i}' for i in range(5)] for j in range(19)]

    tbl(
        data.settings['Организация'],
        'Медицинская документация\nУчетная форма № 307/у-05\n'
        'Утверждена приказом Министерства\nздравоохранения '
        'Российской Федерации\nот 18 декабря 2015 г. № 933н',
    )
    spcr(3)
    prgr('Center', 'АКТ')
    prgr('Center', 'медицинского освидетельствования на состояние опьянения')
    prgr('Center', '(алкогольного, наркотического или иного токсического)')
    prgr('Center', '№', report[0])
    spcr(2)
    prgr('Normal+', '', data_[0][2])

    spcr(1)
    prgr('Normal+', '1. Сведения об освидетельствуемом лице:')
    prgr('Normal+', 'Фамилия, имя, отчество', data_[1][0])
    prgr('Normal+', 'Дата рождения', data_[1][1])
    prgr('Normal+', 'Адрес места жительства', data_[1][2])
    prgr(
        'Normal+',
        'Сведения об освидетельствуемом лице заполнены на основании',
        data_[1][3],
    )

    spcr(1)
    prgr(
        'Normal+',
        '2. Основание для медицинского освидетельствования',
        data_[2][0],
    )
    prgr('Normal+', 'Кем направлен', data_[2][1])

    spcr(1)
    prgr(
        'Normal+',
        '3. Наименование структурного подразделения медицинской организации, '
        'в котором проводится медицинское освидетельствование',
        data_[3][0],
    )

    spcr(1)
    prgr(
        'Normal+',
        '4. Дата и точное время начала медицинского освидетельствования',
        data_[4][0],
    )

    spcr(1)
    prgr('Normal+', '5. Кем освидетельствован', data_[5][0])
    prgr(
        'Normal+',
        'Cведения о прохождении подготовки по вопросам проведения '
        'медицинского освидетельствования (наименование медицинской '
        'организации, дата выдачи документа)',
        data_[5][1],
    )

    spcr(1)
    prgr('Normal+', '6. Внешний вид освидетельствуемого', data_[6][0])

    spcr(1)
    prgr(
        'Normal+',
        '7. Жалобы освидетельствуемого на свое состояние',
        data_[7][0],
    )

    spcr(1)
    prgr(
        'Normal+',
        '8. Изменения психической деятельности освидетельствуемого',
    )
    prgr('Normal+', 'состояние сознания', data_[8][0])
    prgr('Normal+', 'поведение', data_[8][1])
    prgr('Normal+', 'ориентировка в месте, времени, ситуации', data_[8][2])
    prgr('Normal+', 'Результат пробы Шульте', data_[8][3])

    spcr(1)
    prgr('Normal+', '9. Вегетативно-сосудистые реакции освидетельствуемого')
    prgr('Normal+', 'зрачки', data_[9][0])
    prgr('Normal+', 'реакция на свет', data_[9][1])
    prgr('Normal+', 'склеры', data_[9][2])
    prgr('Normal+', 'нистагм', data_[9][3])

    spcr(1)
    prgr('Normal+', '10. Двигательная сфера освидетельствуемого')
    prgr('Normal+', 'речь', data_[10][0])
    prgr('Normal+', 'походка', data_[10][1])
    prgr('Normal+', 'устойчивость в позе Ромберга', data_[10][2])
    prgr('Normal+', 'точность выполнения координационных проб', data_[10][3])
    prgr('Normal+', 'результат пробы Ташена', data_[10][4])

    spcr(1)
    prgr(
        'Normal+',
        '11. Наличие заболеваний нервной системы, психических расстройств, '
        'перенесенных травм (со слов освидетельствуемого)',
        data_[11][0],
    )

    spcr(1)
    prgr(
        'Normal+',
        '12. Сведения о последнем употреблении алкоголя, '
        'лекарственных средств, наркотических средств и психотропных веществ '
        '(со слов освидетельствуемого)',
        data_[12][0],
    )

    spcr(1)
    prgr(
        'Normal+',
        '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого',
    )
    prgr(
        'Normal+',
        '13.1 Время первого исследования, '
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения, результат исследования',
        data_[13][0],
    )
    prgr(
        'Normal+',
        '13.2 Второе исследование через 15-20 минут: время исследования, '
        'наименование технического средства измерения, '
        'его заводской номер, дата последней поверки, '
        'погрешность технического средства измерения, результат исследования',
        data_[13][1],
    )

    spcr(1)
    prgr(
        'Normal+',
        '14. Время отбора биологического объекта '
        'у освидетельствуемого (среда)',
        data_[14][0],
    )
    prgr(
        'Normal+',
        'Результаты химико-токсикологических исследований '
        'биологических объектов (название лаборатории, методы исследований, '
        'результаты исследований, номер справки о результатах '
        'химико-токсикологических исследований)',
        data_[14][1],
    )

    spcr(1)
    prgr(
        'Normal+',
        '15. Другие данные медицинского осмотра или представленных документов',
        data_[15][0],
    )

    spcr(1)
    prgr(
        'Normal+',
        '16. Дата и точное время окончания медицинского освидетельствования',
        data_[16][0],
    )

    spcr(1)
    prgr('Normal+', '17. Медицинское заключение', data_[17][0])
    prgr('Normal+', 'дата его вынесения', data_[17][1])

    spcr(1)
    prgr('Normal+', '18. Подпись врача ______________', data_[18][0])
    prgr('Indent', 'М.П.')

    SimpleDocTemplate(
        filename, leftMargin=1.5*cm, rightMargin=1*cm,
        topMargin=1.5*cm, bottomMargin=3*cm,
    ).build(
        story,
        onFirstPage=lambda canvas, _: page_1(canvas, data_[18][0]),
        onLaterPages=lambda canvas, _: page_2(canvas),
    )
