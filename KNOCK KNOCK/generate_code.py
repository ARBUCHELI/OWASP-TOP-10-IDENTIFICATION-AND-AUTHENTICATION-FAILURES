import random
import time


def generate_code():
    input_time = input("Enter a time, or leave blank to use the current time for seed value: ")
    if len(input_time)==0:
        time_seed = time.time()
        time_seed = int(time_seed)
    else:
        time_seed = int(input_time)

    random.seed(time_seed)

    code = (random.random())

    print("Code:", code)

    return code

def main():
    generate_code()

if __name__ == '__main__':
    main()