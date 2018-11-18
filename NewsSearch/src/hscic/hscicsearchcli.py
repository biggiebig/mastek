"""
    Search utility to find articles in hscic
"""
import os
import sys
import click
from hscic.newssearch import ArticleManager

@click.command()
@click.option('--searchtext', required=True,
	help="Text to search within article")
@click.option('--searchtype',required=True, type=click.Choice(['OR', 'AND']),
	help = "Type of search to conduct on the article valid inputs are AND,OR")
def SearchArticles(searchtext, searchtype):
    """
    	CLI to Searchs news articles.
    	Returns article names that match search criterion
    """
    am = ArticleManager()
    articles_found = am.search_articles(searchtext,searchtype)
    if articles_found:
    	click.echo('Following article(s) were found: {}'.format(articles_found))
    else:
    	click.echo('No Articles Found')

if __name__ == '__main__':
    SearchArticles()
