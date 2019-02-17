from setuptools import setup

# Function to open the README file.
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Jevents',
      version='1.1.3',
      description='Simple to use Utilities package for creating EventEmitters and implementing data observers.',
	  long_description=readme(),
	  long_description_content_type='text/markdown',
      classifiers=[
		# Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
		# Define intended audience for package to be developers
        'Intended Audience :: Developers',
		'Environment :: Console',
        'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		# Specify the pyhton versions that are supported
        'Programming Language :: Python :: 3.7',
		'Topic :: Utilities'
      ],
	  keywords='data_observer EventEmitters events observers watch',
      url='https://github.com/Jaimeloeuf/Jevents',
      author='Jaime Loeuf',
      author_email='jaimeloeuf@gmail.com',
      license='MIT',
      packages=['Jevents'],
	  # Do not copy over non-code files when package is installed
      include_package_data=False,
	  # Just to be safe, do not run this package from a Zipped dir.
      zip_safe=False)