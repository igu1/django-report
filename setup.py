from setuptools import setup, find_packages

setup(
    name="django-report",
    version="0.2.0",
    description="A Python package for simplifying the Report Generation process in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Eza",
    author_email="eesaard@gmail.com",
    url="https://github.com/igu1/django-report",
    packages=find_packages(),
    install_requires=["jinja2", "qrcode", 'wkhtmltopdf', 'flask', "pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
