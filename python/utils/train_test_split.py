import os
import numpy as np
from random import shuffle


def write_path(in_list, out_file_path):
    out_text_file = open(out_file_path, "w")
    max_line = len(in_list)
    i = 0
    for line in in_list:
        i += 1
        if i < max_line:
            line += '\n'

        out_text_file.write(line)
            
    out_text_file.close()

def split(path, ratio_1, ratio_2):
    train = []
    valid = []
    test = []
    ars_day = []
    ars_night = []
    detrac = []
    for file in os.listdir(path):
        file_path = '/hdd/nguyenlc/hti-traffic/object_detection/dataset/images/' + file
        if 'ARS_Day' in file:
            ars_day.append(file_path)
        elif 'ARS_Night' in file:
            ars_night.append(file_path)
        elif 'DETRAC' in file:
            detrac.append(file_path)
    
    shuffle(ars_day)
    shuffle(ars_night)
    shuffle(detrac)

    ars_day_train, ars_day_validate, ars_day_test = np.split(ars_day, [int(len(ars_day)*ratio_1), int(len(ars_day)*ratio_2)])
    ars_night_train, ars_night_validate, ars_night_test = np.split(ars_night, [int(len(ars_night)*ratio_1), int(len(ars_night)*ratio_2)])
    detrac_train, detrac_validate, detrac_test = np.split(detrac, [int(len(detrac)*ratio_1), int(len(detrac)*ratio_2)])

    train.extend(ars_day_train)
    train.extend(ars_night_train)
    train.extend(detrac_train)

    valid.extend(ars_day_validate)
    valid.extend(ars_night_validate)
    valid.extend(detrac_validate)

    test.extend(ars_day_test)
    test.extend(ars_night_test)
    test.extend(detrac_test)

    # shuffle(train)
    # shuffle(valid)
    # shuffle(test)

    print(len(train)+len(valid)+len(test)-len(ars_day)-len(ars_night)-len(detrac))
    print(any(i in valid for i in train))
    print(any(i in test for i in valid))
    print(any(i in test for i in train))

    write_path(train, '/home/nguyenlc/Documents/vehicle_detection/final_data/train.txt')
    write_path(valid, '/home/nguyenlc/Documents/vehicle_detection/final_data/valid.txt')
    write_path(valid, '/home/nguyenlc/Documents/vehicle_detection/final_data/test.txt')


if __name__ == '__main__':
    path = '/home/nguyenlc/Documents/vehicle_detection/blacked_data/images'
    ratio_1 = 0.7
    ratio_2 = 0.9
    split(path, ratio_1, ratio_2)

