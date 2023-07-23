'''
All the disks start off on the first rod in a stack. They are ordered by size, with the
largest disk on the bottom and the smallest one at the top.
The goal of this puzzle is to move all the disks from the first rod to the last rod
while following these rules:
You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on
top of another stack.
You cannot place a larger disk on top of a smaller disk.
Write a function that prints out all the steps necessary to complete the Tower of Hanoi.
You should assume that the rods are numbered, with the first rod being 1, the second
(auxiliary) rod being 2, and the last (goal) rod being 3.
For example, with n = 3, we can do this in 7 moves:
Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
'''

from typing import Optional

def towersOfHanoi(
    n: int,
    start_rod: Optional[str] = None,
    aux_rod: Optional[str] = None,
    end_rod: Optional[str] = None,
) -> None:
    
    if not start_rod:
        start_rod = "start_rod"
        print(f"\nTower of Hanoi for {n} Disks ========================================")

    if not aux_rod:
        aux_rod = "aux_rod"

    if not end_rod:
        end_rod = "end_rod"

    if n == 1:
        print(f"Move disk 1 from {start_rod} to {end_rod}.")
        return
    
    towers_of_hanoi(n - 1, start_rod, end_rod, aux_rod)
    print(f"Move disk {n} from {start_rod} to {end_rod}")
    towers_of_hanoi(n - 1, aux_rod, start_rod, end_rod)