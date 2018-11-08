import math
SHORTEST_ROUT = 100

def tsp_berechner(CITY_POSITION, VIS_CITY, index):
    global SHORTEST_ROUT
    CITY_POSITION = CITY_POSITION.copy()
    VIS_CITY = VIS_CITY.copy()

    VIS_CITY.append(CITY_POSITION[index])
    CITY_POSITION.pop(index)

    if not CITY_POSITION:
        totalrout = 0
        for i in range(len(VIS_CITY)-1):
            totalrout += distance(VIS_CITY[i], VIS_CITY[i+1])

        totalrout += distance(VIS_CITY[0], VIS_CITY[len(VIS_CITY)-1])

        if totalrout < SHORTEST_ROUT:
            SHORTEST_ROUT = totalrout

        return SHORTEST_ROUT

    for i in range(len(CITY_POSITION)):
        tsp_berechner(CITY_POSITION, VIS_CITY, i)

def distance(pos1, pos2):
    patha = pos1[0] - pos2[0]
    pathb = pos1[1] - pos2[1]

    dis = math.sqrt(patha**2 + pathb**2)
    return dis

if __name__ == "__main__":
    CITY_POSITION = [(0.010319427306382911, 0.8956251389386756),
                     (0.6999898714299346, 0.42254500074835377),
                     (0.4294574582950912, 0.4568408794115657),
                     (0.6005454852683483, 0.9295407203370832),
                     (0.9590226056623925, 0.581453646599427),
                     (0.748521134122647, 0.5437775417153159),
                     (0.7571232013282426, 0.606435031856663),
                     (0.07528757443413125, 0.07854082131763074),
                     (0.32346175150639334, 0.7291706487873425)]

    VIS_CITY = []
    tsp_berechner(CITY_POSITION, VIS_CITY, 0)
    print(SHORTEST_ROUT)
    