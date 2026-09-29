from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

def generate_cv_pdf():
    # Create the PDF document
    doc = SimpleDocTemplate("f:/pagina alcobendas/proyecto/cv.pdf", pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.darkblue,
        borderWidth=1,
        borderColor=colors.lightgrey,
        borderPadding=5
    )
    
    normal_style = styles['Normal']
    bold_style = ParagraphStyle(
        'Bold',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black
    )
    
    # Title
    title = Paragraph("Curriculum Vitae", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Personal Information
    personal_info = [
        ["Nombre:", "Ing. Jonny Eduardo Vasco Barreno"],
        ["Título:", "Ingeniero en Sistemas y Computación (Graduado en Ecuador)"],
        ["Correo:", "vasco3s2009@gmail.com"],
        ["Teléfono/WhatsApp:", "+34 612492967"],
        ["Dirección:", "Calle Triana #2, 1º A, Alcobendas, Madrid"]
    ]
    
    personal_table = Table(personal_info, colWidths=[2*inch, 4*inch])
    personal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(Paragraph("Información Personal", heading_style))
    elements.append(personal_table)
    elements.append(Spacer(1, 20))
    
    # Profile
    profile_text = """
    Perfil proactivo y versátil con enfoque en roles de Soporte Informático, Mantenimiento Técnico, 
    Cableado Estructurado de Redes, Mantenimiento General de Instalaciones o Soldadura (MIG / Electrodo). 
    Comprometido con la calidad, la resolución eficiente de problemas técnicos y la adaptación a entornos 
    diversos. Disponibilidad inmediata y total.
    """
    elements.append(Paragraph("Perfil Profesional", heading_style))
    elements.append(Paragraph(profile_text.strip(), normal_style))
    elements.append(Spacer(1, 20))
    
    # Technical Skills
    elements.append(Paragraph("Competencias Técnicas", heading_style))
    
    skills_data = [
        ["Soporte y Reparación de Hardware/Software", "Redes e Instalación de Cableado Estructurado"],
        ["Soldadura MIG y Electrodo", "Mantenimiento General de Instalaciones"],
        ["Diagnóstico y Configuración de Sistemas", "Seguridad y Limpieza de Malware"]
    ]
    
    skills_table = Table(skills_data, colWidths=[3*inch, 3*inch])
    skills_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black)
    ]))
    
    elements.append(skills_table)
    elements.append(Spacer(1, 20))
    
    # Footer
    footer_text = "CV generado el 25/09/2026 para Vasco Tech Alcobendas"
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(footer_text, ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER
    )))
    
    # Build PDF
    doc.build(elements)
    print("CV PDF generado exitosamente")

if __name__ == "__main__":
    generate_cv_pdf()