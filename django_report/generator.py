import os
import subprocess
from typing import Dict
from jinja2 import Environment, FileSystemLoader
from flask import Flask, send_file, request, jsonify

class PDFGenerator:
    def __init__(self, output_path: str, template_dir: str, template_name: str, wk_params: Dict[str, str] = None):
        self.output_path = output_path
        self.template_dir = template_dir
        self.template_name = template_name
        self.custom_params = wk_params
        os.makedirs(self.output_path, exist_ok=True)
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def render_pdf_from_html(self, context):
        template = self.env.get_template(self.template_name)
        html_content = template.render(context)
        temp_html_path = os.path.join(self.output_path, 'temp.html')
        output_pdf_path = os.path.join(self.output_path, 'output.pdf')

        with open(temp_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        cmd = ['wkhtmltopdf', '--quiet', temp_html_path, output_pdf_path]
        
        if self.custom_params:
            cmd.extend(self.custom_params)
            
        try:
            subprocess.run(cmd, check=True)
            return output_pdf_path
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"PDF generation failed: {e}")
        finally:
            os.remove(temp_html_path)

    def generate_pdf_response(self, context: Dict[str, str], file_name: str, as_attachment=False) -> str:
        pdf_data = self.render_pdf_from_html(context)
        return send_file(pdf_data, mimetype='application/pdf', as_attachment=as_attachment, download_name=file_name)
    
    def generate_pdf_file(self, context: Dict[str, str]) -> str:
        return self.render_pdf_from_html(context)