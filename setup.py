from setuptools import setup

setup(name='optobj',
      version='0.1',
      description='Python Package for Optimal Object Selection',
      author='Giuseppe Marco Randazzo',
      author_email='gmrandazzo@gmail.com',
      url='https://github.com/gmrandazzo/scikit-optobj',
      packages=['optobj'],
      license='Modified BSD License',
      install_requires=['numpy',
                        'scipy',
                        'scikit-learn'],
      platforms='Any',)
