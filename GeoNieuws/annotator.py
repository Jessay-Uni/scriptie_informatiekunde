from tkinter import *
import csv
import os

# IMPROV
# Treeview maken van ann_box
# als je op <a> klikt annoteer je
# geonames



#def main_window():
#    m_window = Tk()

#    m_window.title("Annotator")
#    m_window.geometry("700x800")
#    m_window.configure(background='white')

#    return m_window


#def left_frame(m_window, files):
#    l_frame = Frame(m_window)
#    l_frame.pack(side=LEFT, fill=BOTH)

#    Label(l_frame, text = "Files", font=( "Calibri", 14 )).pack( side=TOP )

#   file_box = file_view(l_frame, files)

#    read_btn = Button( l_frame, text = "annotate", font=( "Calibri", 12 ), command=lambda : open_file( file_box, m_window ))
#    read_btn.pack( side=BOTTOM, fill=BOTH )

#    file_box.pack( padx=( 5, 5 ) )


#def find_matches(text, term, first_index, last_index):
#    match_st = text.search(term, last_index, "end")
#    t_len = int(last_index.split(".")[1]) - int(first_index.split(".")[1])
#
#    decimals = len(match_st.split(".")[1])
#    divider = "1" + ("0" * decimals)
#    exact_match = "0." + ("0" * (decimals - 1)) + "1"
#
#    t_len = t_len / int(divider)
#
#    match_end = float(match_st) + t_len
#    exact_match = match_end + float(exact_match)
#
#    match_end = "{:.{}f}".format(match_end, decimals)
#
#    #if text.get(match_end, exact_match) in " .":
#    text.tag_add("annotation", match_st, match_end)
#
#    if text.search(term, match_end, "end"):
#        find_matches(text, term, match_st, match_end)


#
#def highlight(text):
#    if not "annotation" in text.tag_names("sel.first"):
#        text.tag_add("annotation", "sel.first", "sel.last")
#
#        term = text.get("sel.first", "sel.last")
#
#        if text.search(term, text.index("sel.last"), "end"):
#            find_matches(text, term, text.index("sel.first"), text.index("sel.last"))
#
#    else:
#        text.tag_remove("annotation", "sel.first", "sel.last")
#
#    text.tag_configure("annotation", foreground='blue')
#
#    #file_text.tag_ranges("sel")     #selected text indices
#    #print(file_text.get("sel.first", "sel.last")) #selected text values


#def done(text, id, f_window):
#    tags = (len(text.tag_ranges("annotation")) // 2)
#
#    beg = 0
#    end = 1
#    listie = []
#
#    kakje = str(text.tag_ranges("annotation")[0])
#
#    for tag in range(tags):
#        lostie = [id, text.get(text.tag_ranges("annotation")[beg], text.tag_ranges("annotation")[end]), '\t']
#
#        line_n = str(text.tag_ranges("annotation")[beg])
#
#        if line_n.startswith('1'):
#            lostie.append('1')
#        else:
#            lostie.append('0')
#
#        listie.append(lostie)
#
#        beg += 2
#        end += 2
#
#    with open("annotations.tsv", 'a') as infile:
#        for list in listie:
#            infile.write("\t".join(list) + '\n')
#
#
#    f_window.destroy()

# VOLGORDE KLOPT AL - maakt niet uit of je later een woord eerder in de tekst annoteert.


#    [
#     [article_id, string, geotag, title]
#     [article_id, ...
#    ]


#def open_file(listbox, m_window):
#    cur_file = listbox.get( ACTIVE )
#
#    file_id = cur_file.split("_")[1].replace(".txt", "")
#
#
#
#    f_window = Toplevel( m_window, bg='white' )
#    f_window.title( cur_file )
#
#    f_window.geometry( "600x650" )
#
#    file_text = Text( f_window, height=700, font=( "Calibri", 14 ), bd=0, wrap=WORD, highlightthickness=0, spacing2=4 )
#
#    Button(f_window, text="highlight", font=( "Calibri", 12 ), command=lambda : highlight(file_text)).pack(side=BOTTOM, fill=BOTH)
#    Button(f_window, text="done", font=( "Calibri", 12 ), command=lambda : done(file_text, file_id, f_window)).pack(side=BOTTOM, fill=BOTH)
#    #file_text.bind('a', done, file_text, file_id, f_window)
#
#    file_text.pack( fill=BOTH, padx=( 50, 50 ), pady=( 10, 5 ))
#
#    with open( cur_file ) as file:
#        text = file.read()
#
#        file_text.insert( END, text )
#
#    file_text.tag_add("title", '1.0', '1.end')
#    file_text.tag_configure( "title", font=( "Calibri", 14, 'bold' ) )
#
#    file_text['state'] = 'disabled'


#        print(file_text.get('1.0', '1.end')) # to get title line


#def right_frame(m_window):
#    r_frame = Frame( m_window )
#    r_frame.pack( side=RIGHT, fill=BOTH )
#
#    Label( r_frame, text = "Annotations", font=( "Calibri", 14 )).pack(side=TOP)
#
#    ann_box = annotations_view(r_frame)
#    #update_btn = Button(r_frame, text = "update", command=lambda : update_annotations(r_frame, m_window))
#
##    update_btn.pack(side=BOTTOM, fill=BOTH)
#    ann_box.pack(padx=( 5, 5 ))
#
#    ann_box.selection_clear(0, "end")
#    ann_box.see("end")
##    ann_box.selection_set("end")
#
#    r_frame.after(3000, ann_update, ann_box, r_frame)
#
#
#def annotations_view(r_frame):
#    ann_box = Listbox( r_frame, height=500, width = 200, font=("Calibri", 12), selectmode=SINGLE )
#
#    with open("annotations.tsv") as file:
#        text = csv.reader(file, delimiter="\t")
#
#        l_count = 1
#
#        for line in text:
#            rm_count = line.count("")
#
#            for i in range(rm_count):
#                line.remove("")
#
#            ann_box.insert(l_count, " ".join(line))
#            l_count += 1
#
#    return ann_box

#
#def ann_update(ann_box, r_frame):
#    ann_box.delete(0, "end")
#
#    with open("annotations.tsv") as file:
#        text = csv.reader(file, delimiter="\t")
#
#        l_count = 1
#
#        for line in text:
#            rm_count = line.count("")
#
#            for i in range(rm_count):
#                line.remove("")
#
#            ann_box.insert(l_count, " ".join(line))
#            l_count += 1
#
#    ann_box.selection_clear(0, "end")
#    ann_box.see("end")
# #   ann_box.selection_set("end")
#
#    r_frame.after(3000, ann_update, ann_box, r_frame)



#def sortfiles(files):
#    return sorted(files, key=lambda x: int(x.split("_")[0]))
#
#
#def file_list():
#    files = os.listdir()
#
#    for file in files:
#        print(file)
#
#        if not ".txt" in file:
#            files.remove(file)
#
#    return files
#

#def file_view(window, files):
#    file_box = Listbox(window, height=500, font=("Calibri", 12), selectmode=SINGLE)
#
#    f_count = 1
#
#    for file in files:
#        file_box.insert(f_count, file)
#        f_count += 1
#
#    return file_box


#def main():
#    m_window = main_window()

#    files = file_list()
#    files = sortfiles(files)

#    left_frame(m_window, files)
#    r_frame = right_frame(m_window)

    #m_window.after(1000, right_frame, m_window)

#    m_window.mainloop()

#if __name__ == '__main__':
#    main()

