from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='gowleyes',
      version='0.0.00',
      description='A Document Converter Pipeline to prepare latex documents for Ereaders',
      author='Keith Murray',
      author_email='kmurrayis@gmail.com',
      license='MIT',
      packages=['gowleyes'],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
