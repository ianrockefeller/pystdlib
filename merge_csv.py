import sys
import csv


def merge_csv(fn_list, output_fn = 'merged.csv'):
    write_header = True
    with open(output_fn, 'w', newline='') as f:
        writer = csv.writer(f)
        for fn in fn_list:
            with open(fn) as f2:
                reader = csv.reader(f2)
                header = reader.__next__()
                if write_header:
                    write_header = False
                    writer.writerow(header)
                writer.writerows(reader)


if __name__ == '__main__':
    try:
        fn_list = sys.argv[1].strip().split(',')
    except:
        print('please include a comma separated list of filenames')

    try: output_fn = sys.argv[2].strip()
    except: output_fn = 'merged.csv'

    merge_csv(fn_list, output_fn)
