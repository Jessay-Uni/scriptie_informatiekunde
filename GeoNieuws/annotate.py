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


def highlight(text):
    if not "annotation" in text.tag_names("sel.first"):
        text.tag_add("annotation", "sel.first", "sel.last")

        term = text.get("sel.first", "sel.last")

        if text.search(term, text.index("sel.last"), "end"):
            find_matches(text, term, text.index("sel.first"), text.index("sel.last"))

    else:
        text.tag_remove("annotation", "sel.first", "sel.last")

    text.tag_configure("annotation", foreground='blue')

    #file_text.tag_ranges("sel")     #selected text indices
    #print(file_text.get("sel.first", "sel.last")) #selected text values



def find_matches(text, term, first_index, last_index):
    match_st = text.search(term, last_index, "end")
    t_len = int(last_index.split(".")[1]) - int(first_index.split(".")[1])

    decimals = len(match_st.split(".")[1])
    divider = "1" + ("0" * decimals)
    exact_match = "0." + ("0" * (decimals - 1)) + "1"

    t_len = t_len / int(divider)

    match_end = float(match_st) + t_len
    exact_match = match_end + float(exact_match)

    match_end = "{:.{}f}".format(match_end, decimals)

    #if text.get(match_end, exact_match) in " .":
    text.tag_add("annotation", match_st, match_end)

    if text.search(term, match_end, "end"):
        find_matches(text, term, match_st, match_end)

# tags toevoegen, id_list
def done(text, id, f_window, id_list):
    tags = (len(text.tag_ranges("annotation")) // 2)

    beg = 0
    end = 1
    full_list = []

    kakje = str(text.tag_ranges("annotation")[0])

    for tag in range(tags):
        lostie = [id, text.get(text.tag_ranges("annotation")[beg], text.tag_ranges("annotation")[end])]

        # voeg geo_id toe
        lostie.append(id_list[tag])

        line_n = str(text.tag_ranges("annotation")[beg])

        if line_n.startswith('1'):
            lostie.append('1')
        else:
            lostie.append('0')

        full_list.append(lostie)

        beg += 2
        end += 2

    with open("annotations.tsv", 'a') as infile:
        for list in full_list:
            infile.write("\t".join(list) + '\n')


    f_window.destroy()
