from setuptools import setup, find_packages

setup(
    name="hyperxar",
    version="0.1.0",
    author="Calvin Ronksley",
    author_email="youremail@example.com",
    description="Ein Python3 Modul zum Kopieren, Komprimieren und ISO erstellen mit Fortschrittsanzeige.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/deinusername/hyperxar",
    packages=find_packages(),
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
