from code.util import util
# --- Tirando referências -----


path = '../datasets/'

prep = util.PrepData(path)
prep.label_data('text-label.csv')
#prep.align_verses()
#prep.clean_data(get_noise(), True)


