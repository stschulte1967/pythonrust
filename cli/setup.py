from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='blkpy-demo',
    description='demo python CLI tool to list block devices',
    packages=find_packages(),
    author='Alfredo Deza',
    entry_points="""
    [console_scripts]
    blkpy=blkpy.main:main 
    """,
    install_requires=install_requires,
    version='0.0.1',
    url='https://github.com/alfredodeza/pythion-cli-example'
)
