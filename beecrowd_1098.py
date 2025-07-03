	
# I=0 J=1
# I=0 J=2
# I=0 J=3
# I=0.2 J=1.2
# I=0.2 J=2.2
# I=0.2 J=3.2
# .....
# I=2 J=?
# I=2 J=?
# I=2 J=?

def main():
    for i in range(0, 20+1, 2):
        I = i / 10
        for k in range(1, 3+1):
            J = k + I
            i_str = int(I) if I == int(I) else I
            j_str = int(J) if J == int(J) else J
            print(f'I={i_str} J={j_str}')

main()