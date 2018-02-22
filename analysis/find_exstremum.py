STEP = 0.01
MAX_X = 1000


def find_extremum(f):
    extremums = []
    search_steps = [x * STEP for x in range(-1 * int(MAX_X / STEP), int(MAX_X / STEP))]
    for x in search_steps:
        if (f(x) is None) or (f(x - STEP) is None) or (f(x - 2 * STEP) is None):
            continue 
        if f(x - STEP) < f(x) \
            and f(x - STEP) < f(x - STEP * 2):
            extremums += [x - STEP]
        elif f(x - STEP) > f(x) \
            and f(x - STEP) > f(x - STEP * 2):
            extremums += [x - STEP]
    return extremums   