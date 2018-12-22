"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

SPECIFIC_LINES = [
    '5x5:mwggsbSgmssssbwbmgmbwwwmg',
    '6x7:mmgsbbgmgssbwsmmsgmwwgbsswbbwwwgmbwggSmbbs',
    '10x5:bwmmgwsgwmmgbwgswmgsmbmwgssggwmsbbsmbmSbwsgswwbgbs',
    '10x8:ssgwwgwggsmmsswmsswsmwgmbSgssggmbsbwggmmwgbssbwmswbwbbgwwmmmmwggsgmsbmmgbwbbbbbw',
    '10x8:wmwmsmsgmmsbgbbbwbgbSmbmmwgggbswmbsgsbwmbsmwmbmgwswwggbssswmmgsgbwsmwswwgwggsgsb',
    '10x8:gsggbwssbsmwwsbgsmgsbmswgsswgwwgbbmgmwgSmgbgbgsbsbssmbwbmwmgmssgmmwmbmbgwbmwwwwm',
    '11x12:wbbwmgggwmwbsmsswswbgbmsgsgssgbgmmwsmmmssmwmwsmwbwssbwbbggwswwgbmgbbmgmswgmsggbgmmmsgmmsggbswsbbbwmsbbggbSmbwbbwgbwswmmgbbwswgwsswmg',
    '15x12:Sgwbbmgbbmmbwwmsgbwmwbbwwgsgsgbwgbgmmwbwmggmwbbsgsgwbwbwsbgwgwmmggwmmgsbmsmgwsmwwgbsmwsmmssgbgmmsbssgbgwwswbggbbmwwwsbsmgbswsgmmmmsmgmbmmsbgswbmwwbgssswbbmbgmmwswgssgswwbgmssgssgbs',
    '15x12:mmwgssswwmmgbbsgswsmgSwmmwbmmwgbwwbwwbmbmswwbwgsggsbsbmbgbgmbsmgwwwwsbgwsmmwgmgbgmmsggwgmbsbmbgbsssbmmwmmswssbmbwbgsgbggwgwwsbmwgwgmmbgbggsmmbgsgsswbmmsswwmbsgssgwbbwbsmbbgggmsssww',
    '15x12:mwbgbswbbmsmggsgggwbgwmwwbgsggmwgmmwsmmmbsmwbswsbswwgsmgsggggwbgwmgmbsbmsgmgsgmsbbssbbsbwssswssbbwgmmbgwmwggbmwwmsmswswbmbbmbbmgwswgmwsbmbbmbsbmgsgmSgbmbwbwwwsgwbgssmwwwmssggmsmgww',
    '17x15:bmbmgggbgbwwbbbwswbmmwgbsmgmbgmgbbsmsSmbgmsgbbsmswbsgsbssbswswsbggsmmssmmggswsgwmsmgmgmbwwsbbggbbgmggmmswbwmbmmwmbwwwwssswssbsmwwsgswmgmmgbwmbssmwwbwsmgsmgwsbwgwsbmgsgmgmgmgmssbgbbswgsswssgwwwswggmmbsbgbswbbgbbmmggbmwgwmgmbmwwwmwsbgwggwgwmmwbsmwsgwgwbbwbs',
    '20x16:mmsmssmgwwmswbmswsmwmsgbbssmgswbsmgbbwgbwmgmgmbmbsgggbgbsggwmssmmgwgsmsswmwbbggbgssmwwmwwmgwbmbgssbbsgssggwsmwgmmbmgwswsmbsmbgbmmswgwsggmwwwswbbsgwsbwsbwmwwmsmmmsSswmwsgwwmggmmsbmbbbmgggbbbmmmsmmbbbbbbgmsgwssgbbmmsmwmsswwgwgbwbwgbsswwsgsbgmbwsbsmggmmswwgbmmmgbggwwbgbwgbssbgwbbwwwssbwwgwswbgwgbsbggsmbmbgswgbsggmwsbmggww',
    '20x16:mwssmssggwgssggsbwssggmggbbmmbmgsgbswgswwsswsggbwmbwwbbgmssbwgmsmbgwmwssbmgmwgggbgmbgmmbmwggwsgmmgbsgwssbgwbgwmbmwsbbsbgswmbsmwbssbbmsbwsbwmgwgbbbmsgwmmsbsbSwmbgbssgwggssbswgwwbbbmsbggmbmwmsmsggmwmbgmgwsssggwwgsmbwsmwbmwssgmsbwswmwwmwgwbmwmgmgwmgbmwmwmmssbwgbmwbwsmwmmwwbwsmggswmbsgbssgbbwwmgwmwwbgwsbgmbmmgbbbgbsbmmwgss',
    '20x16:mmwgmbwbmbwmbmmwgwmwswgbbwwwmgsbwswbgmgsmsbbsgswgbsgbbsbmsbgsmmgbbwbgmgsbswsmbssmbmgsswmgggbsmwgbgbwwmmgbmssssbwwmbbbmsmwbbgssgwmwmbwggbmgmgwmbwmwmgbmgwbmwgbsmwbggbmswsmwsbswggsgmgwgmgbssgbwgbgmggbmwbssmgbggsmswsgsmswsgwbmwwmswgswsssgbmsbgwmgbgwwswwbgsmwbssgbwwwwgSgsmmmmswswmsswsmgwsmgwsbwbwggssgwbgmgbbmsgmsmmbmbmbwbwb',
    '20x16:sswgssbwsmwwswggsgmsmgwbgbwgsswbbmbbbsmbmbbwmgwwmsgbwwmsgbmwgwswgbwwbbwbwssmmsggsmmmgwmbmssbmbgbmgwgwbmgwgmbswmsbSgmbwmsbmggbbwmswssbwgssmsbwwwbggmwgsmgbsbbwwmmwsbwbbbssmbgsbgsbmbwmmmwbbsmbmmbswwmbmgggsmmgmmsgwsbbgwmwgswbwbmsbgmsgmwmmgbmsgsgsbgmwmwbgssgwmsmgmssgbgwwswgsgggwwbwwwwgsgwgsmbmbsbbgmgwgwsgssgsggsbwwmggmbsmsm',
    '30x20:wgsmggmgsmwggbmbbbmgsbgsgwwwbsgwwgbmbsmsgwbwsssggbsbbmbbwsmbsmswmwsgwsmsbsggsgsmmgwwgsgwwmbgwmbwbswbsmgbbmsmgggmsbssbwsmwwswgmbwswsggwgwmmwsgsmwgmbgwgsbgsmgbmgbbbgmswbsbwwgbmwswggwwmbwbsmwmswbsbwwswgswbsgmgsmssgmbbsbmsbwsgwgsbsmwsgbswsssmmggssggswmwbmwmssmgwsmmwwbwgmbggmmbgsgbmgwgmgmmsgmbgwggmgsssbggswsgsmbsmwgsmmgbbbmsmgsbbbmmmwmmwwbwgwbsgmssbgwmgwmgwgmwbmbgwswbgsswbwmmgbswbggbbbwwmmmmgsmwbmwsbwwmbsswwmmwsswbgssbmbbgmsswsgmwwssmbgsggmmwbwggSbsssgbmwmbggwmbbmgsssbmmwmbbbbwggmgmbbbwggwbggmbwmwmbbsmgbbbggwwsgssmgbgsswwmsbswwwbsswgmgsbbgwggwswmmwgwmmbbmsgmmwsbwwggbmmwbbwwwsbbmgbmmbsmbsmwbbwmswmgb',
    '50x50:bsgwwmwsmmswmbmsbsbmmmmggswgssmmwgsssbwsgggbmmbbbsgbsbwbbbwwgwwbwwswwwgbswgssbmsssbmmbbmsbwbggwggswbwgmbwwbwgsgwwswggswgggbwsbwmmmsgbmssggwsbmgssgwmgbwswgwmgmssgmmmgwmbsgsswswbwbmwggmwbbgmsbsmmbmsmwmmgbwbwmwsgwmwwwsmmbbmwgbbgggsmwssbwgssswwgsgsbswwbmsbswgmggbwbmmggsmmmmsgbgmwgmsgmbgwgbbgsswsgbsbwsmmgbsmgsbwbgmsmwsmswbbbggbwggwsmbwsgbmsggmbgbsgbbwgbsgmgwbwmgmbbbgbmwwsmswmwggmgbbbmwwwwbbsgsggggsgwsgbwgbsbsmsgsbsmwwgbmggmgmbbmsbmbwssgsswbgbwmggggmwbgbsmssmwgmwbsmwswggmwgggsmgbmbsmwssmbbwgwbmmwsmwmbswwbssmggbwbggmgmwgsgwsbmwbwbbmwgwsmwgsgwwgwwsmwgmmwgwgwwmwgwwsbsbgwwgwwswwbggsmssmbggwswgbmmwswssmbsggswmmmwbmwsmgwbssbswmbwmssgbgwwwsbssmgmbwmmwsmbbmbmsssbbgswmwbwmwmgsgbmwbwmgwbwgssmmsgmwgbbmbsmgbmmbsbmwgbgbwmswgwbmwbmmwbgwgbmmgwbsgwbgssgbbbgwwggbmsmmbwwwsggmmmbbgsgssssgssmwbmwwsgbgssswbwgsbmmmsbwbsbgmgwwwgwbgmgwsbssgswgbgswmwbmgwmgwgwgbggbbwbmggswsgswgswsbbwgwbmbmgbsssbwwmmswwwbssmsggwgggsmmbwmmggggsmbmgmmgmbsbgwbgmggmgsgbgwmsgmsmmsmsbwbwsbwmwmbswggmmmwwsmbsswsgbwsbwwmwbbbgwgmbmbgmwbbsmgwgbgwsmwmbbmwsbwbsssmwmwbgmgsssggbbmbbgbmsbwmwbsgmggmsgbggsswsmgssbbgbggsgsgmgbwwbmsmwbwsssmgwmmwssbsbsssbgwsgggsmbgwgmgbwwwwgwwmwmwmbmggswmbbswmswsmbwgwmsggwggswbgwgbmsmggbmsggwsmwbwwgsmsgwgbwmwwsgmwssswbwwggmwsswbmgggwgmgwwgsgmbmwgsmwsgwbmgwgbmwmgwswmbbwgmwsbgmwmsmwmgbmmssmgmwggbmsbmssmbbwbwmsggmmsbbmwbsswggmssgmwswwssbmmsbssgmbmgbmmwbwmbbsgwswbssbmsmmmggbgsgmbsmgmgswgbmwwmwbbmsbmsgsbmggwmmmwwggbsmsbmbwsbsgmsbmsmsgsmmsggmwgwwsmbgbssbgbsmbgwbsgssgsgbwsgsssgbwmwwbgssmwmsmswsgsgbssbbgwwwmwgswswbmbmggmwbbmmgbsgbbmbwssbbmwssmbwgsswgwbbsbbgbggwwsswmssbwsbsbmbwbbgswbmsbmbsgsmsbwmgwwwmbsswwbgsgwsmsbgmbbbbmwgmmbgsgsmwbmgwmgsmwmwswwbwwbggmmmswwsmgwgwsggswgwbmbbwswwbmwgmmbswwmwmgsbsmbmswggbmbsbmwgwgsmmwsbgbmbbSwwbgwbmbsmwbwmwbwmbsgsgwbswgswsmsmmsssgsgmwwggmmmssgsmgbwmmbmwgbswbwbmgmswmwwwwgbmmgbgbswgmbmwgmgbmgsswbbmmsbsbmssmmwggmwwmmgbwbwbgswwsmmggbwbwmwbbgwgbmbbwsbbbbwbmmgbmsgmggbbmgswsgwmwbggsgwssgggwwgmgbbmmsmmmbmmwgsgssssgbsmgmsgsgbgmmsgsswwggsmwggbwgbgmmbbbsbmbbbmbmwgwsbwbmbsgmwbgsbgwmgwwswswgmbmsmbsggwsgmwmbbbgggbwsbmwggbswgwgwsmgsmbbgmbssmswmbbgsmgswwsmmbsgwwmwwbmmwwsgsbwggswbsbwbmwbmsmbsmwgbmbgmmbgmgswgwswbgmgbbbgmmmgswmbbmgsgbsbgbwbgbwbmsbmwbgwswsgswssgwsbmbmgbggbggggmbwgsmmmbwmbswbswmgsmmmwbwmmmbsgsmmbggssmsbsbwmwsbbgsbwbbmbmgswsggmswmwwsbgwsbmwbgwwwsgwbsgsssmmssswwbggmbbwggsgmbswggssbbsgwmgbwwbggmsbbsgbbmsmsbswwbsggwwbbmwsggsgswwbsgbwsgsmmsbgggswsmmswmmwmmgmwmwsbswgbmmmsgbbbsbsmwbmgswmsgsmsbwbswbsgbgsssswbmbmwsgmswbbwmsmswsmggmmbbmbbbmwsbgbbmbwmwbwwmmwsbbsmwbmwmbmsmbgmbssgbggwbm',
    ]

items = _, ROUGH, *_, PLAYER = '$. X*P'
table = str.maketrans('gsbwmS', items)

def specific_line_to_grid(line):
    dim, line = line.split(':')
    nb_cols, nb_rows = map(int, dim.split('x'))
    rows = (line[i * nb_cols : (i + 1) * nb_cols] for i in range(nb_rows))
    grid = [row.translate(table) for row in rows]
    x, _ = start = next((i, j) for i, row in enumerate(grid)
                               for j, cell in enumerate(row) if cell == PLAYER)
    grid[x] = grid[x].replace(PLAYER, ROUGH)
    return nb_cols * nb_rows, (tuple(grid), start)

TESTS = {"Basics": [], "Extra": []}

for nb_boxes, args in map(specific_line_to_grid, SPECIFIC_LINES):
    category = ("Basics", "Extra")[nb_boxes > 50]
    TESTS[category].append({"input": args, "answer": args})