STEP = 0.01
MAX_X = 1000


def find_extremum(f):
    extremums = []
    search_steps = [x * STEP for x in range(-1 * int(MAX_X / STEP), int(MAX_X / STEP))]
    for x in search_steps:
        if f.x(x - STEP) < f.x(x) \
            and f.x(x - STEP) < f.x(x - 2 * STEP):
            extremums += [x-STEP]
        elif f.x(x - STEP) > f.x(x) \
            and f.x(x - STEP) > f.x(x - 2 * STEP):
            extremums += [x-STEP]
    return extremums   