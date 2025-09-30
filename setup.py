from setuptools import setup, find_packages

setup(
    name="hyperxar",  # Name des Moduls auf PyPI
    version="0.2.0",  # Versionsnummer
    author="Calvin Ronksley",
    author_email="ronksleycalvin0@gmail.com",
    description="Python3 Modul zum Kopieren, Komprimieren, Extrahieren und ISO-Erstellen mit Fortschrittsanzeige",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MultiCodexz/hyperxar",  # Link zu GitHub
    packages=find_packages(),  # findet automatisch das Paket hyperxar
    install_requires=[
        "tqdm",
        "py7zr"
    ],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
