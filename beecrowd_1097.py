# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=9
# I=3 J=8
# I=3 J=7

# ...
# I=9 J=15
# I=9 J=14
# I=9 J=13

def main():
    for I in range(1, 10, 2):
        for J in range(I+6, I+3, -1):
            print(f"I={I} J={J}")

main()