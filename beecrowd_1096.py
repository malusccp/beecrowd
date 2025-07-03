	
# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=7
# I=3 J=6
# I=3 J=5
# ...
# I=9 J=7
# I=9 J=6
# I=9 J=5

def main():
    for I in range(1, 10, 2):
        for J in range(7, 4, -1):
            print(f"I={I} J={J}")

main()