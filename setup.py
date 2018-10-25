from setuptools import setup

setup(name='casualeffect',
      version='0.1',
      description='Python framework that measuring casual effect',
      url='https://github.com/hyun78/casualeffect',
      author='HyeonHo Song',
      author_email='hyun78@kaist.ac.kr',
      license='MIT',
      packages=['casualeffect'],
	  install_requires=[
          'pandas',
		  'gensim',
		  'scikit-learn',
      ],
      zip_safe=False)

