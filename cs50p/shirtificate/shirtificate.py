from fpdf import FPDF

def main():
    name = input("Name")
    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png")
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, name, align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()