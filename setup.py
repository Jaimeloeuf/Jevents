from setuptools import setup

# Function to open the README file.
def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='Jevents',
      version='1.1.3',
      description='Simple to use Utilities package for creating EventEmitters and implementing data observers.',
	  long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
		'Environment :: Console',
        'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
		'Topic :: Utilities'
      ],
	  keywords='data_observer EventEmitters events observers',
      url='http://github.com/jaimeloeuf',
      author='Jaime Loeuf',
      author_email='jaimeloeuf@gmail.com',
      license='MIT',
      packages=['Jevents'],
	  include_package_data=True,
      zip_safe=False)