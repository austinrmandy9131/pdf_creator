from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    
    #Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10,21,200,21)
    
    pdf.ln(258)
    
    #Footer
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(270)
        
        #Footer for other pages per Topic
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")



pdf.output("output.pdf")