#!/usr/bin/env python
# -*- coding: utf8 -*-
# Bib sourcing script


def referencer():
        author_company = input(r'Author/Company: ').strip()
        publish_date = input(r'Publication Date (Year, Mon Day): ').strip()
        article_title = input(r'Title: ').strip()
        url_page = input(r'URL: ' ).strip()
        bib = author_company + '. (' + publish_date + '). ' + article_title + ' <' + url_page + '>'
        
        print('\n' + bib + '\n')
        this_file = 'here-is-your-reference.txt'
        with open(this_file, 'w') as into_this_file:
                into_this_file.write(bib)
                this_file.close()


if __name__ == "__main__":
        referencer()
        input('Press any key to close...')
