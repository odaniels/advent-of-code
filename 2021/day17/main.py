def main(input):
    #numbers = [list(map(int, line.strip())) for line in input.readlines()]
    xrange = range(269, 292 + 1)
    yrange = range(44, 68 + 1)

    max_y = 0
    results = set()
    for i in range(-100, 200):
        for j in range(0, 300):
            x, y, vx, vy = 0, 0, 0, 0
            vy = i
            vx = j
            local_max_y = 0
            for _ in range(300):
                x += vx
                y += vy
                vx -= vx / abs(vx) if vx else 0
                vy -= 1
                #print(x,y,vx,vy)
                if -y in yrange and x in xrange:
                    #print(x,y,vx,vy)
                    results.add((i,j))
                    print((j,i))
                    break
                else:
                    continue
        #if is_too_far:
        #    break
    print(len(results))

    result1 = None
    result2 = None

    return result1, result2


TEST_EXPECTED = None, None
PUZZLE_EXPECTED = None, None