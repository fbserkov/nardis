from os.path import join

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import ttfonts
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

from convert import date2str, datetime2str, datetime2str_time, time2str


def font_registration():
    registerFont(ttfonts.TTFont('Arial', join('fonts', 'ArialMT.ttf')))
    registerFont(ttfonts.TTFont('ArialBd', join('fonts', 'Arial-BoldMT.ttf')))
    registerFontFamily('Arial', normal='Arial', bold='ArialBd')


class Doc:
    def __init__(self, filename, doctor):
        font_registration()
        self._story, self.doctor = [], doctor
        self.width, self.size, self.leading = A4[0], 12, 14

        self.doc = SimpleDocTemplate(
            join('acts', filename),
            leftMargin=1.5 * cm, rightMargin=1 * cm,
            topMargin=1.5 * cm, bottomMargin=3 * cm,
        )
        self.doc.author, self.doc.creator = 2 * ('Fedor Serkov',)
        self.doc.subject, self.doc.title = 'narcology', 'nardis'

    def _page_1(self, canvas, _):
        canvas.setFont('Arial', self.size)
        canvas.drawString(
            2.5 * cm, 1 * cm + 2 * self.leading,
            'Подпись врача ______________',
        )
        canvas.drawString(14 * cm, 1 * cm + self.leading, 'М.П.')
        canvas.drawRightString(self.width - 1 * cm, 1 * cm, 'Страница 1 из 2')
        canvas.setFont('ArialBd', self.size)
        canvas.drawString(
            9.0 * cm, 1 * cm + 2 * self.leading, '/ ' + self.doctor + ' /')

    def _page_2(self, canvas, _):
        canvas.setFont('Arial', self.size)
        canvas.drawRightString(self.width - 1 * cm, 1 * cm, 'Страница 2 из 2')

    def add_paragraph(
            self, text, bold='', is_centered=False, is_indented=False):
        if bold:
            text += ' ' + f'<b>{bold}</b>'
        attributes = f'fontName=Arial fontSize={self.size}'
        attributes += f' leading={self.leading}'
        if is_centered:
            attributes += ' alignment=center'
        if is_indented:
            attributes += f' leftIndent={12.5 * cm}'
        self._story.append(
            Paragraph(f'<para {attributes}>' + text + '</para>'))

    def add_spacer(self, n):
        for i in range(n):
            self._story.append(Spacer(1, self.leading))

    def add_table(self, organization, form):
        self._story.append(
            Table(
                data=[[organization, form]],
                style=TableStyle([
                    ('FONTNAME', (0, 0), (1, 0), 'Arial'),
                    ('ALIGN', (0, 0), (1, 0), 'CENTER'),
                    ('SIZE', (0, 0), (1, 0), self.size),
                    ('LEADING', (0, 0), (1, 0), self.leading),
                ])
            )
        )

    def build(self):
        self.doc.build(
            self._story, onFirstPage=self._page_1, onLaterPages=self._page_2)


class PDF:
    def __init__(self, db):
        year, number = db.select(0, 'year'), db.select(0, 'number')
        full_name, doctor = db.select(1, 'full_name'), db.select(5, 'doctor')
        filename = f'{year}_{number:04} {full_name}.pdf'
        self.db, self.doc = db, Doc(filename, doctor)
        self._d_ap = self.doc.add_paragraph

    def _item_0(self):
        self.doc.add_table(
            self.db.select(0, 'organization'),
            'Медицинская документация\nУчетная форма № 307/у-05\n'
            'Утверждена приказом Министерства\nздравоохранения '
            'Российской Федерации\nот 18 декабря 2015 г. № 933н',
        )
        self.doc.add_spacer(3)
        self._d_ap('АКТ', is_centered=True)
        self._d_ap(
            'медицинского освидетельствования на состояние опьянения',
            is_centered=True,
        )
        self._d_ap(
            '(алкогольного, наркотического или иного токсического)',
            is_centered=True,
        )
        number, year = self.db.select(0, 'number'), self.db.select(0, 'year')
        self._d_ap('№', str(number) + '/' + str(year), is_centered=True)
        self.doc.add_spacer(2)
        datetime = self.db.select(4, 'datetime')
        self._d_ap('', datetime.strftime(f'"{datetime.day}" %B %Y г.'))

    def _item_1(self):
        self.doc.add_spacer(1)
        self._d_ap('1. Сведения об освидетельствуемом лице:')
        self._d_ap('Фамилия, имя, отчество', self.db.select(1, 'full_name'))
        self._d_ap('Дата рождения', date2str(self.db.select(1, 'date')))
        self._d_ap('Адрес места жительства', self.db.select(1, 'address'))
        self._d_ap(
            'Сведения об освидетельствуемом лице заполнены на основании',
            self.db.select(1, 'document'),
        )

    def _item_2(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '2. Основание для медицинского освидетельствования',
            self.db.select(2, 'document'),
        )
        self._d_ap('Кем направлен', self.db.select(2, 'full_name'))

    def _item_3(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '3. Наименование структурного подразделения медицинской '
            'организации, в котором проводится медицинское '
            'освидетельствование', self.db.select(3, 'subdivision'),
        )

    def _item_4(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '4. Дата и точное время начала медицинского освидетельствования',
            datetime2str(self.db.select(4, 'datetime')),
        )

    def _item_5(self):
        self.doc.add_spacer(1)
        self._d_ap('5. Кем освидетельствован', self.db.select(5, 'doctor'))
        self._d_ap(
            'Cведения о прохождении подготовки по вопросам проведения '
            'медицинского освидетельствования (наименование медицинской '
            'организации, дата выдачи документа)',
            self.db.select(5, 'training'),
        )

    def _item_6(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '6. Внешний вид освидетельствуемого',
            self.db.select(6, 'appearance'),
        )

    def _item_7(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '7. Жалобы освидетельствуемого на свое состояние',
            self.db.select(7, 'complaints'),
        )

    def _item_8(self):
        self.doc.add_spacer(1)
        self._d_ap('8. Изменения психической деятельности освидетельствуемого')
        self._d_ap('состояние сознания', self.db.select(8, 'consciousness'))
        self._d_ap('поведение', self.db.select(8, 'behavior'))
        self._d_ap(
            'ориентировка в месте, времени, ситуации',
            self.db.select(8, 'orientation'))
        self._d_ap('Результат пробы Шульте', self.db.select(8, 'schulte'))

    def _item_9(self):
        self.doc.add_spacer(1)
        self._d_ap('9. Вегетативно-сосудистые реакции освидетельствуемого')
        self._d_ap('зрачки', self.db.select(9, 'pupils'))
        self._d_ap('реакция на свет', self.db.select(9, 'reaction'))
        self._d_ap('склеры', self.db.select(9, 'scleras'))
        self._d_ap('нистагм', self.db.select(9, 'nystagmus'))

    def _item_10(self):
        self.doc.add_spacer(1)
        self._d_ap('10. Двигательная сфера освидетельствуемого')
        self._d_ap('речь', self.db.select(10, 'speech'))
        self._d_ap('походка', self.db.select(10, 'gait'))
        self._d_ap(
            'устойчивость в позе Ромберга', self.db.select(10, 'romberg'))
        self._d_ap(
            'точность выполнения координационных проб',
            self.db.select(10, 'coordination'),
        )
        self._d_ap('результат пробы Ташена', self.db.select(10, 'tashen'))

    def _item_11(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '11. Наличие заболеваний нервной системы, '
            'психических расстройств, перенесенных травм '
            '(со слов освидетельствуемого)', self.db.select(11, 'comorbidity'),
        )

    def _item_12(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '12. Сведения о последнем употреблении алкоголя, лекарственных '
            'средств, наркотических средств и психотропных веществ '
            '(со слов освидетельствуемого)', self.db.select(12, 'drug_use'),
        )

    def _item_13(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого')
        self._d_ap(
            '13.1 Время первого исследования',
            datetime2str_time(self.db.select(13, 'datetime_1')),
        )
        self._d_ap(
            'наименование технического средства измерения, '
            'его заводской номер, дата последней поверки, '
            'погрешность технического средства измерения',
            self.db.select(13, 'device_1'),
        )
        self._d_ap('результат исследования', self.db.select(13, 'result_1'))
        self._d_ap(
            '13.2 Второе исследование через 15-20 минут: время исследования',
            datetime2str_time(self.db.select(13, 'datetime_2')),
        )
        self._d_ap(
            'наименование технического средства измерения, '
            'его заводской номер, дата последней поверки, '
            'погрешность технического средства измерения',
            self.db.select(13, 'device_2'),
        )
        self._d_ap('результат исследования', self.db.select(13, 'result_2'))

    def _item_14(self):
        self.doc.add_spacer(1)
        time = time2str(self.db.select(14, 'time'))
        material = self.db.select(14, 'material')
        self._d_ap(
            '14. Время отбора биологического объекта '
            'у освидетельствуемого (среда)',
            time + (' (' + material + ')' if time else ''),
        )
        self._d_ap(
            'Результаты химико-токсикологических '
            'исследований биологических объектов'
        )
        self._d_ap('название лаборатории', self.db.select(14, 'laboratory'))
        self._d_ap('методы исследований', self.db.select(14, 'method'))
        result = self.db.select(14, 'result')
        self._d_ap(
            'результаты исследований',
            ', '.join(k + ' ' + v for k, v in result.items())
            if type(result) is dict else result,
        )
        self._d_ap(
            'номер справки о результатах химико-токсикологических '
            'исследований', self.db.select(14, 'number'),
        )

    def _item_15(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '15. Другие данные медицинского осмотра или '
            'представленных документов', self.db.select(15, 'other'),
        )

    def _item_16(self):
        self.doc.add_spacer(1)
        self._d_ap(
            '16. Дата и точное время окончания '
            'медицинского освидетельствования',
            datetime2str(self.db.select(16, 'datetime')),
        )

    def _item_17(self):
        self.doc.add_spacer(1)
        self._d_ap('17. Медицинское заключение', self.db.select(17, 'opinion'))
        self._d_ap('дата его вынесения', date2str(self.db.select(17, 'date')))

    def _item_18(self):
        self.doc.add_spacer(1)
        doctor = self.db.select(5, 'doctor')
        self._d_ap('18. Подпись врача ______________', '/ ' + doctor + ' /')
        self._d_ap('М.П.', is_indented=True)

    def create(self):
        for i in range(19):
            name = '_item_' + str(i)
            bound_method = self.__getattribute__(name)
            bound_method()
        self.doc.build()
