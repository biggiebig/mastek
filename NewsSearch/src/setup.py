from setuptools import setup, find_packages

setup(
    name='hscic_newssearch',
    version='0.1',
    author='Gurdeep Atwal',
    author_email='depsi.a@gmail.com',
    description='hscicSearchCLI Search is a utility to search news articles',
    license='GPLv3+',
    packages= ['hscic'],
    url='https://github.com/biggiebig/mastek/',
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        hscicsearch = hscic.hscicsearchcli:SearchArticles
    '''
)
