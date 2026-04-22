import os
from tools.report_writer import write_report

def test_report():
    write_report("outputs/test.md", "hello")
    assert os.path.exists("outputs/test.md")