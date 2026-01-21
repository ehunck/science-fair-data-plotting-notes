from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
)


def build_table(data):
    table = Table(data, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
                ("TOPPADDING", (0, 0), (-1, 0), 6),
            ]
        )
    )
    return table


def main():
    doc = SimpleDocTemplate(
        "practice_handout.pdf",
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        spaceAfter=12,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=11,
        spaceAfter=10,
    )
    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        spaceBefore=10,
        spaceAfter=8,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=11,
        leading=14,
    )

    story = []
    story.append(Paragraph("Mini Practice: Graphing and Variables", title_style))
    story.append(Paragraph("Name: ________________________________   Date: ____________________", subtitle_style))
    story.append(Paragraph(
        "Use the datasets below to practice choosing the right graph and identifying variables.",
        body_style,
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Practice dataset 1: Ice cube melting", heading_style))
    table_1 = build_table(
        [
            ["Time (min)", "Mass of ice (g)"],
            ["0", "50"],
            ["2", "45"],
            ["4", "40"],
            ["6", "35"],
            ["8", "30"],
            ["10", "26"],
        ]
    )
    story.append(table_1)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Practice dataset 2: Bean sprouting by soil type", heading_style))
    table_2 = build_table(
        [
            ["Soil type", "Seeds sprouted (out of 10)"],
            ["Potting soil", "8"],
            ["Sand", "3"],
            ["Clay", "4"],
            ["Compost", "9"],
        ]
    )
    story.append(table_2)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Your tasks", heading_style))
    tasks = ListFlowable(
        [
            ListItem(Paragraph("Identify the manipulated, responding, and controlled variables.", body_style)),
            ListItem(Paragraph("Pick the best graph type.", body_style)),
            ListItem(Paragraph("Explain why in one sentence.", body_style)),
        ],
        bulletType="1",
        leftIndent=18,
    )
    story.append(tasks)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Space for notes", heading_style))
    for _ in range(4):
        story.append(Paragraph("______________________________________________________________________________", body_style))
        story.append(Spacer(1, 8))

    doc.build(story)


if __name__ == "__main__":
    main()
