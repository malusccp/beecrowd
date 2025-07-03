# I=1 J=60
# I=4 J=55
# I=7 J=50
# ...
# I=? J=0

def main():
    I = 1
    J = 60
    while J >= 0:
        print(f'I={I} J={J}')
        I += 3
        J -= 5

main()