import math
import datetime


def main():
    colors = ';'.join(['#112233', '#23dfee', '#ffffff'])
    print(colors)
    print(colors.split(';'))

    city = ''.join(['New', 'found', 'land'])
    print(city)

    sample_tuple = 'unforgetable'.partition('forget')
    print(sample_tuple)

    departure, separator, arrival = 'London:Edinburgh'.partition(':')
    print(departure)
    print(arrival)

    origin, _, destination = 'Seattle-Boston'.partition('-')
    print(origin)
    print(destination)

    print('The age of {0} is {1}'.format('Jim', 32))
    print("The age of {0} is {1}. {0}'s birthday is on {2}.".format('Fred', 32, 'October'))
    print('Reticulating spline {} of {}'.format(4, 23))
    print('Current position {latitude} {longitude}'.format(latitude='60N', longitude='5E'))
    print('Galactic position x={pos[0]} y={pos[1]} z={pos[2]}'.format(pos=(65.2, 23.1, 82.2)))
    print('Math constants: pi={m.pi}, e={m.e}'.format(m=math))
    print('Math constants: pi={m.pi:.3f}, e={m.e:.3f}'.format(m=math))

    value = 4 * 20
    print(f'The value is {value}')
    print(f'The current itme is {datetime.datetime.now().isoformat()}.')
    print(f'Math constants: pi={math.pi:.3f}, e={math.e:.3f}')


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
