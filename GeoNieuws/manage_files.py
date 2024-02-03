import os

def sortfiles(files):
    return sorted(files, key=lambda x: int(x.split("_")[0]))


def file_list():
    all_files = os.listdir()
    files = []


    for file in all_files:
        if ".txt" in file:
            files.append(file)

    return files


#def file_view(window, files):
#    file_box = Listbox(window, height=500, font=("Calibri", 12), selectmode=SINGLE)

#    f_count = 1

#    for file in files:
#        file_box.insert(f_count, file)
#        f_count += 1

#    return file_box
