# sorting records 

from operator import itemgetter

email_book = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'}, {'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'} ]

for record in email_book:
    print(record)

x = itemgetter('first')(email_book[0])
print(x)