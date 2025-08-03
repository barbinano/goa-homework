import multiprocessing
import math
import time
import os


def cpu_stress():
    while True:
        for i in range(10**7):
            math.sqrt(i)


def ram_stress():
    big_list = []
    while True:
        big_list.append("goga" * 10**6)  # massive strings


def disk_stress():
    i = 0
    while True:
        with open(f"disk_spam_{i}.txt", "w") as f:
            f.write("goga" * 10**7)
        i += 1

if __name__ == "__main__":
    cpu_processes = []
    for _ in range(multiprocessing.cpu_count()):  # Use all CPU cores
        p = multiprocessing.Process(target=cpu_stress)
        cpu_processes.append(p)
        p.start()

    ram_proc = multiprocessing.Process(target=ram_stress)
    ram_proc.start()

    disk_proc = multiprocessing.Process(target=disk_stress)
    disk_proc.start()

    for p in cpu_processes:
        p.join()
    ram_proc.join()
    disk_proc.join()