def tower_of_hanoi(n, source, helper, target,moves):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        moves[0] += 1
        return
    tower_of_hanoi(n - 1, source, target, helper,moves)
    moves[0] += 1
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, helper, source, target,moves)

n = int(input("Give the value of n : "))
moves = [0]
tower_of_hanoi(n, 'A', 'B', 'C',moves)
print("No. of moves :",moves[0])
