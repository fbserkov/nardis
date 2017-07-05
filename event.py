from func import *


def bind_entries_events(entries):

    entries[1][1].bind('<KeyRelease>',  key_release_date)
    entries[4][0].bind('<KeyRelease>',  key_release_date)
    entries[4][1].bind('<KeyRelease>',  key_release_time)
    entries[13][0].bind('<KeyRelease>', key_release_time)
    entries[13][1].bind('<KeyRelease>', key_release_result)
    entries[13][2].bind('<KeyRelease>', key_release_time)
    entries[13][3].bind('<KeyRelease>', key_release_result)
    entries[14][0].bind('<KeyRelease>', key_release_time)
    entries[16][0].bind('<KeyRelease>', key_release_date)
    entries[16][1].bind('<KeyRelease>', key_release_time)
    entries[17][1].bind('<KeyRelease>', key_release_date)


def bind_smart_labels_events(smart_labels, entries, entries_default):

    smart_labels[1][0].bind(
        '<Button-1>', lambda e: add(entries[1][2], e.widget))
    smart_labels[1][1].bind(
        '<Button-1>', lambda e: add(entries[1][2], e.widget))
    smart_labels[1][2].bind(
        '<Button-1>', lambda e: add(entries[1][2], e.widget))

    smart_labels[1][3].bind(
        '<Button-1>', lambda e: replace(entries[1][3], e.widget))
    smart_labels[1][4].bind(
        '<Button-1>', lambda e: replace(entries[1][3], e.widget))
    smart_labels[1][5].bind(
        '<Button-1>', lambda e: replace(entries[1][3], e.widget))
    smart_labels[2][0].bind(
        '<Button-1>', lambda e: replace(entries[2][0], e.widget))
    smart_labels[2][1].bind(
        '<Button-1>', lambda e: replace(entries[2][0], e.widget))
    smart_labels[2][2].bind(
        '<Button-1>', lambda e: replace(entries[2][0], e.widget))
    smart_labels[8][0].bind(
        '<Button-1>', lambda e: replace(entries[8][0], e.widget))
    smart_labels[8][1].bind(
        '<Button-1>', lambda e: replace(entries[8][0], e.widget))
    smart_labels[8][2].bind(
        '<Button-1>', lambda e: replace(entries[8][0], e.widget))
    smart_labels[8][3].bind(
        '<Button-1>', lambda e: replace(entries[8][0], e.widget))
    smart_labels[8][15].bind(
        '<Button-1>', lambda e: replace(entries[8][2], e.widget))
    smart_labels[8][16].bind(
        '<Button-1>', lambda e: replace(entries[8][2], e.widget))
    smart_labels[8][17].bind(
        '<Button-1>', lambda e: replace(entries[8][2], e.widget))
    smart_labels[12][0].bind(
        '<Button-1>', lambda e: replace(entries[12][0], e.widget))
    smart_labels[12][1].bind(
        '<Button-1>', lambda e: replace(entries[12][0], e.widget))

    smart_labels[17][0].bind(
        '<Button-1>', lambda e: replace_plus(
            entries[17][0], e.widget, entries[17][1]))
    smart_labels[17][1].bind(
        '<Button-1>', lambda e: replace_plus(
            entries[17][0], e.widget, entries[17][1]))
    smart_labels[17][2].bind(
        '<Button-1>', lambda e: replace_plus(
            entries[17][0], e.widget, entries[17][1]))

    smart_labels[8][4].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][5].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][6].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][7].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][8].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][9].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][10].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][11].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][12].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][13].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[8][14].bind(
        '<Button-1>', lambda e: smart_add(
            entries[8][1], e.widget, entries_default[8][1]))
    smart_labels[10][0].bind(
        '<Button-1>', lambda e: smart_add(
            entries[10][0], e.widget, entries_default[10][0]))
    smart_labels[10][1].bind(
        '<Button-1>', lambda e: smart_add(
            entries[10][0], e.widget, entries_default[10][0]))
    smart_labels[10][2].bind(
        '<Button-1>', lambda e: smart_add(
            entries[10][0], e.widget, entries_default[10][0]))
    smart_labels[10][3].bind(
        '<Button-1>', lambda e: smart_add(
            entries[10][1], e.widget, entries_default[10][1]))
    smart_labels[10][4].bind(
        '<Button-1>', lambda e: smart_add(
            entries[10][1], e.widget, entries_default[10][1]))

    smart_labels[9][0].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[9][0], e.widget, entries_default[9][0]))
    smart_labels[9][1].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[9][0], e.widget, entries_default[9][0]))
    smart_labels[9][2].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[9][1], e.widget, entries_default[9][1]))
    smart_labels[9][3].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[9][2], e.widget, entries_default[9][2]))
    smart_labels[9][4].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[9][3], e.widget, entries_default[9][3]))
    smart_labels[10][5].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[10][2], e.widget, entries_default[10][2]))
    smart_labels[10][6].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[10][2], e.widget, entries_default[10][2]))
    smart_labels[10][7].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[10][2], e.widget, entries_default[10][2]))
    smart_labels[10][8].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[10][3], e.widget, entries_default[10][3]))
    smart_labels[10][9].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[10][3], e.widget, entries_default[10][3]))
    smart_labels[10][10].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[10][3], e.widget, entries_default[10][3]))
    smart_labels[14][0].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][1], e.widget, entries_default[14][1]))
    smart_labels[14][1].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][3], e.widget, entries_default[14][3]))
    smart_labels[14][2].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][3], e.widget, entries_default[14][3]))
    smart_labels[14][3].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][4], e.widget, entries_default[14][4]))
    smart_labels[14][4].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][4], e.widget, entries_default[14][4]))
    smart_labels[14][5].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][5], e.widget, entries_default[14][5]))
    smart_labels[14][6].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][5], e.widget, entries_default[14][5]))
    smart_labels[14][7].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][6], e.widget, entries_default[14][6]))
    smart_labels[14][8].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][6], e.widget, entries_default[14][6]))
    smart_labels[14][9].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][7], e.widget, entries_default[14][7]))
    smart_labels[14][10].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][7], e.widget, entries_default[14][7]))
    smart_labels[14][11].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][8], e.widget, entries_default[14][8]))
    smart_labels[14][12].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][8], e.widget, entries_default[14][8]))
    smart_labels[14][13].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][9], e.widget, entries_default[14][9]))
    smart_labels[14][14].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][9], e.widget, entries_default[14][9]))
    smart_labels[14][15].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][10], e.widget, entries_default[14][10]))
    smart_labels[14][16].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][10], e.widget, entries_default[14][10]))
    smart_labels[14][17].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][11], e.widget, entries_default[14][11]))
    smart_labels[14][18].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][11], e.widget, entries_default[14][11]))
    smart_labels[14][19].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][12], e.widget, entries_default[14][12]))
    smart_labels[14][20].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][12], e.widget, entries_default[14][12]))
    smart_labels[14][21].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][13], e.widget, entries_default[14][13]))
    smart_labels[14][22].bind(
        '<Button-1>', lambda e: smart_replace(
            entries[14][13], e.widget, entries_default[14][13]))
