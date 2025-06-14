import sys
from behave.__main__ import main as behave_main

if __name__ == '__main__':
    sys.exit(behave_main([
        "features",
        "--define", "browser=chrome",
        "--format", "behave_html_formatter:HTMLFormatter",
        "--outfile", "reports/report.html",
    ]))
