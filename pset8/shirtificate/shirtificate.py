from fpdf import FPDF

# Prompts user for name
name = input("Name: ")

# Creates an A4 PDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Prints the PNG Image
pdf.image("shirtificate.png", x=1.25, y=60)

# Prints the title
pdf.set_font('helvetica', '', 50)
pdf.cell(190, 50, 'CS50 Shirtificate', align='C')

# Prints the body
pdf.set_font('helvetica', '', 26)
pdf.set_text_color(255,255,255)
pdf.cell(-190, 250, f'{name} took CS50', align='C')

# Outputs the PDF Shirtificate
pdf.output("shirtificate.pdf")