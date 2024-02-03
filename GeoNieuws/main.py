import annotator
import manage_files as man_file
import gui
import annotate

def main():
    m_window = gui.main_window()

    files = man_file.file_list()
    files = man_file.sortfiles(files)

    gui.left_frame(m_window, files)
    r_frame = gui.right_frame(m_window)

    m_window.mainloop()

if __name__ == '__main__':
    main()
