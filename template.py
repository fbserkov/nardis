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


class Doc:
    def __init__(self, filename, doctor):
        self.doctor, self._story = doctor, _story
        self.doc = SimpleDocTemplate(
            join('acts', filename),
            leftMargin=1.5*cm, rightMargin=1*cm,
            topMargin=1.5*cm, bottomMargin=3*cm,
        )

    def add_table(self, organization, form):
        self._story.append(
            Table(
                data=[[organization, form]],
                style=TableStyle([
                    ('FONTNAME', (0, 0), (1, 0), 'Arial'),
                    ('ALIGN', (0, 0), (1, 0), 'CENTER'),
                    ('SIZE', (0, 0), (1, 0), SIZE),
                    ('LEADING', (0, 0), (1, 0), LEADING),
                ])
            )
        )

    def build(self):
        self.doc.build(
            _story,  # TODO do not need lambda (5.2)
            onFirstPage=lambda canvas, _: _page_1(
                canvas, '/ ' + self.doctor + ' /'),
            onLaterPages=lambda canvas, _: _page_2(canvas),
        )


class PDF:
    def __init__(self, db):
        year, number = db.select(0, 'year'), db.select(0, 'number')
        full_name, doctor = db.select(1, 'full_name'), db.select(5, 'doctor')
        filename = f'{year}_{number:04} {full_name}.pdf'
        self.db, self.doc = db, Doc(filename, doctor)

    def _item_0(self):
        self.doc.add_table(
            self.db.select(0, 'organization'),
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
        number, year = self.db.select(0, 'number'), self.db.select(0, 'year')
        _liner('№', str(number) + '/' + str(year), is_centered=True)
        _spacer(2)
        datetime = self.db.select(4, 'datetime')
        _liner('', datetime.strftime(f'"{datetime.day}" %B %Y г.'))

    def _item_1(self):
        _spacer(1)
        _liner('1. Сведения об освидетельствуемом лице:')
        _liner('Фамилия, имя, отчество', self.db.select(1, 'full_name'))
        _liner('Дата рождения', date2str(self.db.select(1, 'date')))
        _liner('Адрес места жительства', self.db.select(1, 'address'))
        _liner(
            'Сведения об освидетельствуемом лице заполнены на основании',
            self.db.select(1, 'document'),
        )

    def _item_2(self):
        _spacer(1)
        _liner(
            '2. Основание для медицинского освидетельствования',
            self.db.select(2, 'document'),
        )
        _liner('Кем направлен', self.db.select(2, 'full_name'))

    def _item_3(self):
        _spacer(1)
        _liner(
            '3. Наименование структурного подразделения медицинской '
            'организации, в котором проводится медицинское '
            'освидетельствование', self.db.select(3, 'subdivision'),
        )

    def _item_4(self):
        _spacer(1)
        _liner(
            '4. Дата и точное время начала медицинского освидетельствования',
            datetime2str(self.db.select(4, 'datetime')),
        )

    def _item_5(self):
        _spacer(1)
        _liner('5. Кем освидетельствован', self.db.select(5, 'doctor'))
        _liner(
            'Cведения о прохождении подготовки по вопросам проведения '
            'медицинского освидетельствования (наименование медицинской '
            'организации, дата выдачи документа)',
            self.db.select(5, 'training'),
        )

    def _item_6(self):
        _spacer(1)
        _liner(
            '6. Внешний вид освидетельствуемого',
            self.db.select(6, 'appearance'),
        )

    def _item_7(self):
        _spacer(1)
        _liner(
            '7. Жалобы освидетельствуемого на свое состояние',
            self.db.select(7, 'complaints'),
        )

    def _item_8(self):
        _spacer(1)
        _liner('8. Изменения психической деятельности освидетельствуемого')
        _liner('состояние сознания', self.db.select(8, 'consciousness'))
        _liner('поведение', self.db.select(8, 'behavior'))
        _liner(
            'ориентировка в месте, времени, ситуации',
            self.db.select(8, 'orientation'))
        _liner('Результат пробы Шульте', self.db.select(8, 'schulte'))

    def _item_9(self):
        _spacer(1)
        _liner('9. Вегетативно-сосудистые реакции освидетельствуемого')
        _liner('зрачки', self.db.select(9, 'pupils'))
        _liner('реакция на свет', self.db.select(9, 'reaction'))
        _liner('склеры', self.db.select(9, 'scleras'))
        _liner('нистагм', self.db.select(9, 'nystagmus'))

    def _item_10(self):
        _spacer(1)
        _liner('10. Двигательная сфера освидетельствуемого')
        _liner('речь', self.db.select(10, 'speech'))
        _liner('походка', self.db.select(10, 'gait'))
        _liner('устойчивость в позе Ромберга', self.db.select(10, 'romberg'))
        _liner(
            'точность выполнения координационных проб',
            self.db.select(10, 'coordination'),
        )
        _liner('результат пробы Ташена', self.db.select(10, 'tashen'))

    def _item_11(self):
        _spacer(1)
        _liner(
            '11. Наличие заболеваний нервной системы, '
            'психических расстройств, перенесенных травм '
            '(со слов освидетельствуемого)', self.db.select(11, 'comorbidity'),
        )

    def _item_12(self):
        _spacer(1)
        _liner(
            '12. Сведения о последнем употреблении алкоголя, лекарственных '
            'средств, наркотических средств и психотропных веществ '
            '(со слов освидетельствуемого)', self.db.select(12, 'drug_use'),
        )

    def _item_13(self):
        _spacer(1)
        _liner('13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого')
        _liner(
            '13.1 Время первого исследования',
            datetime2str_time(self.db.select(13, 'datetime_1')),
        )
        _liner(
            'наименование технического средства измерения, '
            'его заводской номер, дата последней поверки, '
            'погрешность технического средства измерения',
            self.db.select(13, 'device_1'),
        )
        _liner('результат исследования', self.db.select(13, 'result_1'))
        _liner(
            '13.2 Второе исследование через 15-20 минут: время исследования',
            datetime2str_time(self.db.select(13, 'datetime_2')),
        )
        _liner(
            'наименование технического средства измерения, '
            'его заводской номер, дата последней поверки, '
            'погрешность технического средства измерения',
            self.db.select(13, 'device_2'),
        )
        _liner('результат исследования', self.db.select(13, 'result_2'))

    def _item_14(self):
        _spacer(1)
        time = time2str(self.db.select(14, 'time'))
        material = self.db.select(14, 'material')
        _liner(
            '14. Время отбора биологического объекта '
            'у освидетельствуемого (среда)',
            time + (' (' + material + ')' if time else ''),
        )
        _liner(
            'Результаты химико-токсикологических '
            'исследований биологических объектов'
        )
        _liner('название лаборатории', self.db.select(14, 'laboratory'))
        _liner('методы исследований', self.db.select(14, 'method'))
        result = self.db.select(14, 'result')
        _liner(
            'результаты исследований',
            ', '.join(k + ' ' + v for k, v in result.items())
            if type(result) is dict else result,
        )
        _liner(
            'номер справки о результатах химико-токсикологических '
            'исследований', self.db.select(14, 'number'),
        )

    def _item_15(self):
        _spacer(1)
        _liner(
            '15. Другие данные медицинского осмотра или '
            'представленных документов', self.db.select(15, 'other'),
        )

    def _item_16(self):
        _spacer(1)
        _liner(
            '16. Дата и точное время окончания '
            'медицинского освидетельствования',
            datetime2str(self.db.select(16, 'datetime')),
        )

    def _item_17(self):
        _spacer(1)
        _liner('17. Медицинское заключение', self.db.select(17, 'opinion'))
        _liner('дата его вынесения', date2str(self.db.select(17, 'date')))

    def _item_18(self):
        _spacer(1)
        doctor = self.db.select(5, 'doctor')
        _liner('18. Подпись врача ______________', '/ ' + doctor + ' /')
        _liner('М.П.', is_indented=True)

    def create(self):
        for i in range(19):
            name = '_item_' + str(i)
            bound_method = self.__getattribute__(name)
            bound_method()
        self.doc.build()
