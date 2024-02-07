# sorting records 

from operator import itemgetter

email_book = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'}, {'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'} ]

def sorter(collection):
    return sorted(collection,key=itemgetter('first','last'))

processed_email_book = sorter(email_book)

for book in email_book:
    print(book)

print('\n')

for book in processed_email_book:
    print(book)