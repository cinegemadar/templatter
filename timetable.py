from report.report import Report
from datamodel.data_source import ExcelDataSource
from reportmodel.report_generator import ReportGenerator
from reportmodel.template import Template
from environment import environment
from pathlib import Path


def create_report(out_folder:str) -> None:
    timetable_data = ExcelDataSource("./res/timetable.xlsx")
    timetable_template = Template(
        template_folder=Path("./res/"),
        template_file="timetable.html")
    timetable_generator = ReportGenerator(
        logo=Path("./res/templatte_logo.png"),
        style=Path("./res/style.css"),
        template=timetable_template
    )
    timetable = Report(timetable_data, timetable_generator)
    timetable.create(lambda _: f"./{out_folder}/timetable.pdf")

def main():
    out_folder = "./report/demo/out/timetable"
    create_report(out_folder)


if __name__ == "__main__":
    main()