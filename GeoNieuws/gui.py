from tkinter import *
from tkinter import ttk
import csv
from annotate import done
from annotate import highlight
import requests



# SELECTEREN EN GEO-ID OPSLAAN !!!
# GEO-ID EXPORTEREN !!!
# FOCUS OP TEXT: kan later


def predictGeoId(placeName):
    URL = "http://api.geonames.org/searchJSON?q=" + placeName + "&maxRows=10&username=jessay"
    response = requests.get(URL)
    data = response.json()['geonames']

    return data


def gen_table(tree, listie=''):
    if isinstance(listie, list):
        opts = predictGeoId(listie[0])
    else:
        opts = predictGeoId(listie)


    for opt in range(len(opts)):
        try:
            tree.insert('', 'end', values=(opts[opt]['toponymName'], opts[opt]['fclName'], opts[opt]['countryName'],
                opts[opt]['adminName1'], opts[opt]['fcodeName'], opts[opt]['geonameId']), tags=('larger'))
        except KeyError:
            tree.insert('', 'end', text='')

        tree.tag_configure('larger', font=( "Calibri", 11 ))


def term_counter(g_frame_b, cur_count, counter):
    count_label = Label(g_frame_b, text=(str(cur_count) + "/" + str(counter)))
    count_label.pack(side=BOTTOM)

    return count_label


def geo_window(text, f_window, file_id):
    if len(text.tag_ranges("annotation")) == 0:
        f_window.destroy()

    else:

        tags = (len(text.tag_ranges("annotation")) // 2)

        beg = 0
        end = 1

        listie = []

        for tag in range(tags):
            listie.append(text.get(text.tag_ranges("annotation")[beg], text.tag_ranges("annotation")[end]))

            beg += 2
            end += 2


        g_window = Toplevel( f_window, bg='light grey' )
        g_window.title( listie[0] )
        g_window.geometry( "900x300" )

        g_frame = Frame(g_window)
        g_frame.pack(fill=BOTH, side=TOP)
        g_frame_b = Frame(g_window)
        g_frame_b.pack(side=BOTTOM, fill=BOTH)


        tree = ttk.Treeview(g_frame, columns=('0', '1', '2', '3', '4', '5'), show='headings', height=10, selectmode='browse')
        tree.heading('0', text='Name')
        tree.heading('1', text='Category')
        tree.heading('2', text='Country')
        tree.heading('3', text='Part of')
        tree.heading('4', text='Division')
        tree.heading('5', text='GeoID')
        tree.column('1', width=150, anchor='center')
        tree.column('2', width=150)
        tree.column('3', width=100, anchor='center')
        tree.column('5', width=75)
        tree.pack(fill=BOTH)


        counter = len(listie)
        cur_count = 1

        search_bar = Entry(g_frame)
        #search_bar.insert(0, listie[0])
        search_bar.pack(anchor='w', side=RIGHT, expand=True)

        search_button = Button(g_frame, text="Search", command=lambda : search_btn(search_bar, tree))
        search_button.pack(anchor='e', side=LEFT, expand=True)

        next = Button(g_frame_b, text = "Skip", font=( "Calibri", 12 ), command=lambda : next_btn(g_window, g_frame, g_frame_b, cur_count, counter, count_label, id_list, listie, text, f_window, file_id, tree, next))
        next.pack()

        count_label = term_counter(g_frame_b, cur_count, counter)

        id_list = []

        gen_table(tree, listie)

        tree.bind('<ButtonRelease-1>', lambda event: get_id(event, tree, g_window, g_frame, g_frame_b, cur_count, counter, count_label, id_list, listie, text, f_window, file_id, next))




def search_btn(search_bar, tree):
    tree.delete(*tree.get_children())

    gen_table(tree, search_bar.get())


def get_id(event, tree, g_window, g_frame, g_frame_b, cur_count, counter, count_label, id_list, listie, text, f_window, file_id, next):
    bap = tree.item(tree.focus())

    geo_id = str(bap['values'][-1])

    next_btn(g_window, g_frame, g_frame_b, cur_count, counter, count_label, id_list, listie, text, f_window, file_id, tree, next, geo_id)



def next_btn(g_window, g_frame, g_frame_b, cur_count, counter, count_label, id_list, listie, text, f_window, file_id, tree, next, geo_id=""):

    id_list.append(geo_id)


    if cur_count < counter:
        cur_count += 1

        tree.delete(*tree.get_children())

        preds = predictGeoId(listie[cur_count - 1])


        for pred in range(len(preds)):
            try:
                tree.insert('', 'end', values=(preds[pred]['toponymName'], preds[pred]['fclName'], preds[pred]['countryName'],
                    preds[pred]['adminName1'], preds[pred]['fcodeName'], preds[pred]['geonameId']), tags=('larger'))
            except KeyError:
                tree.insert('', 'end', text='')

        tree.tag_configure('larger', font=( "Calibri", 11 ))

        tree.pack(fill=BOTH)

        tree.bind('<ButtonRelease-1>', lambda event: get_id(event, tree, g_window, g_frame, g_frame_b, cur_count, counter, count_label, id_list, listie, text, f_window, file_id, next))

        next.destroy()
        next = Button(g_frame_b, text = "Skip", font=( "Calibri", 12 ), command=lambda : next_btn(g_window, g_frame, g_frame_b, cur_count, counter, count_label, id_list, listie, text, f_window, file_id, tree, next))
        next.pack()

        count_label.destroy()
        count_label = term_counter(g_frame_b, cur_count, counter)

        g_window.title(listie[cur_count - 1])


    else:
        done(text, file_id, f_window, id_list)
        g_window.destroy()




def main_window():
    m_window = Tk()

    m_window.title("Annotator")
    m_window.geometry("700x800")
    m_window.configure(background='white')

    return m_window


def left_frame(m_window, files):
    l_frame = Frame(m_window)
    l_frame.pack(side=LEFT, fill=BOTH)
    Label(l_frame, text = "Files", font=( "Calibri", 14 )).pack( side=TOP )

    file_box = file_view(l_frame, files)

    read_btn = Button( l_frame, text = "annotate", font=( "Calibri", 12 ), command=lambda : open_file( file_box, m_window ))
    read_btn.pack( side=BOTTOM, fill=BOTH )

    file_box.pack( padx=( 5, 5 ) )


def file_view(window, files):
    file_box = Listbox(window, height=500, font=("Calibri", 12), selectmode=SINGLE)

    f_count = 1

    for file in files:
        file_box.insert(f_count, file)
        f_count += 1

    return file_box


def open_file(listbox, m_window):
    cur_file = listbox.get( ACTIVE )

    file_id = cur_file.split("_")[1].replace(".txt", "")

    f_window = Toplevel( m_window, bg='white' )
    f_window.title( cur_file )

    f_window.geometry( "600x650" )

    file_text = Text( f_window, height=700, font=( "Calibri", 14 ), bd=0, wrap=WORD, highlightthickness=0, spacing2=4 )

    Button(f_window, text="done", font=( "Calibri", 12 ), command=lambda : geo_window(file_text, f_window, file_id)).pack(side=BOTTOM, fill=BOTH)
    Button(f_window, text="highlight", font=( "Calibri", 12 ), command=lambda : highlight(file_text)).pack(side=BOTTOM, fill=BOTH)

    file_text.pack( fill=BOTH, padx=( 50, 50 ), pady=( 10, 5 ))

    with open( cur_file ) as file:
        text = file.read()

        file_text.insert( END, text )

    file_text.tag_add("title", '1.0', '1.end')
    file_text.tag_configure( "title", font=( "Calibri", 14, 'bold' ) )

    file_text['state'] = 'disabled'


def right_frame(m_window):
    r_frame = Frame( m_window )
    r_frame.pack( side=RIGHT, fill=BOTH )

    Label( r_frame, text = "Annotations", font=( "Calibri", 14 )).pack(side=TOP)

    ann_box = annotations_view(r_frame)

    ann_box.pack(padx=( 5, 5 ))

    ann_box.selection_clear(0, "end")
    ann_box.see("end")

    r_frame.after(3000, ann_update, ann_box, r_frame)


def annotations_view(r_frame):
    ann_box = Listbox( r_frame, height=500, width = 200, font=("Calibri", 12), selectmode=SINGLE )

    with open("annotations.tsv") as file:
        text = csv.reader(file, delimiter="\t")

        l_count = 1

        for line in text:
            rm_count = line.count("")

            for i in range(rm_count):
                line.remove("")

            ann_box.insert(l_count, " ".join(line))
            l_count += 1

    return ann_box

def ann_update(ann_box, r_frame):
    ann_box.delete(0, "end")

    with open("annotations.tsv") as file:
        text = csv.reader(file, delimiter="\t")

        l_count = 1

        for line in text:
            rm_count = line.count("")

            for i in range(rm_count):
                line.remove("")

            ann_box.insert(l_count, " ".join(line))
            l_count += 1

    ann_box.selection_clear(0, "end")
    ann_box.see("end")
 #   ann_box.selection_set("end")

    r_frame.after(1000, ann_update, ann_box, r_frame)
