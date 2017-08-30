# chardet's setup.py
from distutils.core import setup
setup(
    name = "quack-dns",
    packages = ["quack-dns"],
    version = "0.1.1",
    description = "Keeps your DuckDNS IP information updated.",
    author = "Fabio Colella",
    author_email = "fcole90@gmail.com",
    url = "https://github.com/fcole90/quack-dns",
    download_url = "https://github.com/fcole90/quack-dns",
    keywords = ["dns", "quack", "duck", "updater"],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        #"Intended Audience :: Religion" # Pray it works!
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Networking"
        ],
    long_description = """\
Keeps your DuckDNS IP information updated.
"""
)