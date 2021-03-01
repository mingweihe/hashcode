from os import path
from glob import glob
from collections import defaultdict

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

def move_one_step(car_id, incoming_street_peak, local_isp, cars_status, cars_next_street):
    pass

def solve(dataset):
    num_intersections = dataset['num_intersections']
    intersections = []
    ## navie solution: 1 second for each incoming street
    # incoming_streets = [[] for _ in xrange(num_intersections)]
    # for B, E, street_name, travel_time in dataset['streets']:
    #     incoming_streets[E].append(street_name)
    # for inter_id, streets in enumerate(incoming_streets):
    #     intersection = []
    #     street_durations = []
    #     intersection.append(inter_id)
    #     intersection.append(len(streets))
    #     for street_name in streets:
    #         street_durations.append([street_name, 1])
    #     intersection.append(street_durations)
    #     intersections.append(intersection)

    ## solution2: optimize by traffic peak
    incoming_street_peak = defaultdict(int)
    local_isp = defaultdict(int)
    cars_status = [['', 0] for _ in xrange(dataset['num_cars'])] # current street, position in the street
    cars_next_street = [[-1, -1] for _ in xrange(dataset['num_cars'])]
    incoming_streets = [[] for _ in xrange(num_intersections)]

    for B, E, street_name, travel_time in dataset['streets']:
        incoming_streets[E].append(street_name)
        
    for i in xrange(dataset['duration']):
        for car_id in xrange(dataset['num_cars']):
            move_one_step(car_id, incoming_street_peak, local_isp, cars_status, cars_next_street)

    result = {
        'num_intersections': num_intersections,
        'intersections': intersections
    }
    return result


if __name__ == '__main__':
    for filename in glob(path.join(datasets_folder, '*')):
        dataset = read(filename)
        res = solve(dataset)
        output_filename = path.join(output_folder, path.basename(filename))
        write(output_filename, res)
