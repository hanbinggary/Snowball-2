from setuptools import setup, find_packages
import versioneer

def readme():
    with open('README.md') as f:
        contents = f.read()
    return contents


setup(
    name='Snowball',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Hong Junhyoung',
    author_email='bellus77@gmail.com',
    desription='Investment backtest tool',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/HongJunhyoung/Snowball',
    packages=find_packages(include=["snowball", "snowball.*"]),
    include_package_data=True,
    install_requires=['numpy>=1.18.4', 'pandas>=1.0.3', 'tqdm>=4.45.0', 'plotly>=4.7.1', 'scipy>=1.4.1'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
