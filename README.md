# PDFGenerator

`PDFGenerator` is a Python package that allows you to generate PDFs from HTML templates using `wkhtmltopdf`. It utilizes Jinja2 for HTML templating and supports custom configuration for controlling the PDF output.

## Features

- Render HTML content using Jinja2 templates.
- Convert HTML to PDF using `wkhtmltopdf`.
- Support for custom parameters to control PDF generation.
- Save the generated PDF to a specified output directory.
- Easy-to-use API for generating PDFs with dynamic data.

## Requirements

- Python 3.6+
- `wkhtmltopdf` (make sure it's installed on your system)
- Jinja2

## Installation

Install the required Python dependencies with:

```bash
pip install jinja2
