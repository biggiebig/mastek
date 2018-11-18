# Search Articles

This is a CLI tool that searches ISIC News articles in a file called articles.txt.
The tool accepts the search text and type of search (AND/OR) and returns any matching article reference numbers.

### Running
To install following commands:

 1. python3 -m pip install
 2. pip3 install dist/hscic_newssearch-0.32-py3-none-any.whl
 3. Ensure the file articles.txt is in the root of directory  when running the CLI.

### License
Feel free to use

### Features

Supports only one default option which is to search news articles in articles.txt

**Usage**
--searchtext (required) Search Text to search within article
--searchtype (required) Type of search to conduct on the article valid inputs are AND,OR

*example*

hscicsearch --searchtext='Care Quality Commission' --searchtype='OR'
