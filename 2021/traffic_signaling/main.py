from sys import path


datasets_folder = './datasets'
output_folder = './output'


def read(filename):
    with open(filename) as f:
        D, I, S, V, F = map(int, f.readline().split())
        streets = []
        for _ in xrange(S):
            B, E, street_name, travel_time = f.readline().split()
            B, E, travel_time = int(B), int(E), int(travel_time)
            streets.append([B, E, street_name, travel_time])
        cars = []
        for _ in xrange(V):
            line = f.readline().split()
            # num_street = int(line[0])
            path_list = line[1:]
            cars.append(path_list)

    data = {
        'duration': D,
        'num_intersections': I,
        'num_streets': S,
        'num_cars': V,
        'bonus': F,
        'streets': streets,
        'cars': cars
    }

    return data


def write(filename, result):
    with open(filename, 'w') as f:
        A = result['num_intersections']
        f.write('{}\n'.format(A))
        for intersection in result['intersections']:
            idx = intersection[0]
            f.write('{}\n'.format(idx))
            num_income = intersection[1]
            f.write('{}\n'.format(num_income))
            for street, duration in intersection[2]:
                f.write('{} {}\n'.format(street, duration))


def score():
    pass


def solve(dataset):
    result = {
        'num_intersections': 0,
        'intersections': []
    }
    return result


if __name__ == '__main__':
    dataset = read(path.join(datasets_folder, 'sampleA.txt'))
    res = solve(dataset)
    write(path.join(output_folder, 'sampleA.out'), res)
