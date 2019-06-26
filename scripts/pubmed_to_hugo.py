from unidecode import unidecode

import pathlib
import csv
import toml
import sys

sys.path.insert(0, '../../pymed')
import pymed

tool = 'lab_website'
email = 'radus@scripps.edu'

pubmed_ids = [
    31209349, 31127001, 30911178, 30885957, 
    30879861, 30829483, 30720278, 30702848, 
    30609444, 30479271, 30421483, 30420694, 
    30420476, 30301768, 30221923, 30195729, 
    30171986, 30114402, 30051485, 29937983, 
    29894184, 29748627, 29736714, 29731364, 
    29727668, 29719702, 29540562, 29528965, 
    29481079, 29443976, 29296668, 29278326, 
    29265822, 29170371, 29168484, 29100630, 
    28970359, 28660730
]

OUTPUT_PATH = pathlib.Path('output')

def main():
    pubmed = pymed.PubMed(tool=tool, email=email)
    q = pubmed.query(' '.join(map(str, pubmed_ids)) + '[PMID]')

    abbrevs = get_abbrevs()

    for article in l:
        pages_el = article.xml.find('.//Pagination/MedlinePgn')
        volume_el = article.xml.find('.//JournalIssue/Volume')
        publication_date = article.journal_publication_date or article.publication_date

        year = publication_date.year

        abbrev = abbrevs.get(article.journal, article.journal)
        abbrev = abbrev.rstrip('.').replace('.', '_').replace(' ', '').lower()

        article_info = {
            'title': article.title.rstrip('.'),
            'authors': ', '.join([f"{a['lastname']} {a['initials']}" for a in article.authors]),
            'link': f'https://dx.doi.org/{article.doi}',
            'journal': article.journal,
            'volume': volume_el.text if volume_el is not None else '',
            'pages': pages_el.text if pages_el is not None else '',
            'year': year,
            'publish_date': publication_date,
            'image': '',
            'doi': article.doi
        }

        path = OUTPUT_PATH.joinpath(str(year))
        path.mkdir(exist_ok=True, parents=True)

        filename = '{}_{}_{}.md'.format(
            unidecode(article.authors[0]['lastname'].replace(' ', '_')),
            abbrev,
            publication_date.strftime('%Y%m')
        ).lower()

        with path.joinpath(filename).open('w') as f:
            f.write('+++\n' + toml.dumps(article_info) + '+++')


def get_abbrevs():
    filename = 'jrnl_abbrevs.txt'
    num_comment_rows = 3

    with open(filename) as f:
        reader = csv.reader(f, delimiter='\t')
        data = [r for r in reader][num_comment_rows:]

    return dict(data)


if __name__ == '__main__':
    main()
