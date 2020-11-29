from os.path import join

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

registerFont(TTFont('Arial', join('fonts', 'ArialMT.ttf')))
registerFont(TTFont('ArialBd', join('fonts', 'Arial-BoldMT.ttf')))
registerFontFamily('Arial', normal='Arial', bold='ArialBd')


class Doc:
    def __init__(self, filename, doctor):
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
