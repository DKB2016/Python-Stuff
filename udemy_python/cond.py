#
#
#
#

import random

def main():
    asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]
     
    for asteroid in asteroids:
        if asteroid == 9617:
            print("Grahamchapman")
        elif asteroid == 9618:
            print("Johncleese")
        elif asteroid == 9619:
            print("Terrygilliam")
            break
        elif asteroid == 9620:
            print("Ericidle")
        elif asteroid == 9621:
            print("Michaelpalin")
        else:
            print("Terryjones")
    else:
        print("MontyPython")
        
    for x in range(30):
        if x % 3 == 0 or x % 5 == 0:
            continue
        print(x)

if __name__ == '__main__':
    main()