#printing tuple records 


PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

def format_sort_record(records):
    sorted_records = sorted(records,key=lambda record: record[2])
    output_format = '{1:10} {0:10} {2:5.2f}'

    for record in sorted_records:
        print(output_format.format(*record))

format_sort_record(PEOPLE)

