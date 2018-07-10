from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name = 'jup2jek',
      version = '0.0.0',
      author = 'Matt Pewsey',
      description = 'Convert Jupyter notebooks to markdown for Jekyll websites such as GitHub Pages.',
      long_description = long_description,
      url = 'https://github.com/line-mind/jup2jek',
      license = '',
      packages = find_packages(),
      include_package_data = True,
      install_requires = [],
      dependency_links = [],
      keywords = ['gh-pages', 'convert-jupyter-notebooks', 'jupyter-notebook',
                  'jupyter', 'jekyll', 'jekyll-posts'],
      classifiers = ['Programming Language :: Python :: 3',
                     'Operating System :: OS Independent',
                     'License :: OSI Approved :: BSD License'],
      python_requires = '')
