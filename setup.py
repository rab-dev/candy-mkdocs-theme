from setuptools import setup, find_packages

VERSION = '0.3.3'

setup(
  name="mkdocs-shine",
  version=VERSION,
  url='https://github.com/rab-dev/shine-mkdocs-theme',
  license='Proprietary',
  description='Elegant theme for MkDocs',
  author='rab',
  author_email='rab@oxyio.com',
  packages=find_packages(),
  include_package_data=True,
  entry_points={
    'mkdocs.themes': [
      'shine = shine_theme',
    ]
  },
  zip_safe=False
)
