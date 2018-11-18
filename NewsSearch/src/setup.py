from setuptools import setup, find_packages

setup(
    name='hscic_newssearch',
    version='0.32',
    author='Gurdeep Atwal',
    author_email='depsi.a@gmail.com',
    description='hscicSearchCLI Search is a utility to search news articles',
    license='GPLv3+',
    packages= ['hscic'],
    url='',
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        hscicsearch = hscic.hscicsearchcli:SearchArticles
    '''
)
