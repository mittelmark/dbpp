from setuptools import setup, find_packages

setup(name='dbpp',
      version='0.2.1',
      description='Python package with code from Course Databases and Practical Programming',
      url='https://github.com/mittelmark/dbpp',
      author='Detlef Groth',
      author_email='dgroth@uni-potsdam.de',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
        package_data={'': ['data/*.tab','tcllibs*/*.*']})
