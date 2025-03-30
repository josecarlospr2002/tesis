import io
import json
from typing import List

from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseServerError
from django_reportbroD.models import ReportDefinition
from reportbro import Report, ReportBroError

from ..models import *


def custom_export_report_by_name(template_name, data, file="reporte", ):
    """Export a report using its name"""

    report = ReportDefinition.objects.filter(name=template_name).first()

    if not report:
        return HttpResponseServerError("Este reporte no se encuentra disponible")

    # if extension.lower() == "xlsx":
    #     return reportXLSX(report.report_definition, data, file)

    return customReportPDF(
        report.report_definition, data, file, template_name
    )


def customReportPDF(
    report_definition, data, file="reporte", nombre_reporte=None
):
    """Prints a pdf file with the available data and optionally sends it as an email attachment."""

    try:
        report_inst = Report(json.loads(report_definition), data)

        if report_inst.errors:
            raise ReportBroError(report_inst.errors[0])

        pdf_report = report_inst.generate_pdf()

        
        response = HttpResponse(bytes(pdf_report), content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="{filename}"'.format(
            filename=f"{file}.pdf"
        )

        return response
    except Exception as e:
        # Handle any exceptions or errors that may occur during the process
        print(f"An error occurred: {str(e)}")
        return HttpResponse("An error occurred while processing the report")
