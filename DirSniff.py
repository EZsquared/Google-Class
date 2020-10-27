import os
import csv


sample_dict = [{'Name': 'Eric', 'Color': 'Yellow', 'Game': 'Warzone'}, {'Name': 'Amanda', 'Color': 'Green', 'Game': 'MarioKart'}]
keys = ['Name', 'Color', 'Game']



def directory_sniff(find_dir, sample_dict, keys):
    desk_dir = False
    while desk_dir == False:
        if os.path.exists(os.path.abspath(os.path.join(os.getcwd(), find_dir))):
            os.chdir(find_dir)
            with open('Testsy.csv', 'w') as testy:
                writer = csv.DictWriter(testy, fieldnames=keys)
                writer.writeheader()
                writer.writerows(sample_dict)
                print ("Success!")
            desk_dir = True
            # print(os.getcwd())
        else:
            os.chdir(os.pardir)

directory_sniff('Desktop', sample_dict, keys)