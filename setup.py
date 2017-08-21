# coding=utf-8

from distutils.core import setup

files = ["__init__.py",
         "const.py",
         "utilities.py",
         "tags.py"
         ]

setup(name="pyid3tagger",
      version="0",
      description="pyid3tagger is a pure Python library to read, write and delete ID3 tags.",
      author="Peter Klassen",
      author_email='peter@mediadock.org',
      url="https://github.com/pkla6/pyid3tagger",
      packages=['pyid3tagger'],
      package_data={'pyid3tagger': files},
      license="MIT"
      )
