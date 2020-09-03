def offset_cell(cell: (int, int), step: (int, int)):
    return cell[0] + step[0], cell[1] + step[1]

def offset_gen(cells: list, step: (int, int)):
    return [offset_cell(c, step) for c in cells]
