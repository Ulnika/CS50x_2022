from fpdf import FPDF

class PDF(FPDF):
    def header(self):

        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 60, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def tshirt(self, name):
        self.set_font("helvetica", "", 30)
        self.set_text_color(255)
        self.cell(0, 210, f"{name} took CS50", align="C")






pdf = PDF()

pdf.add_page(format=(210, 297))
pdf.image("shirtificate.png", 0, 80)

name = input("Name: ")

pdf.tshirt(name)
pdf.output("shirtificate.pdf")