import multiprocessing
import time
import math
import random

def heavyload(looping_time):
    t1 = time.time()
    num = 1.99
    no_iter = 0
    while(time.time() - t1 < looping_time):
        for _ in range(1000):
            num = (num*num)
            num = num/0.25
            num = math.sqrt(num)
            num = num/2.0

        no_iter += 1000

    print("after %   iter num is %   instead of 2" % (no_iter, num))

    return no_iter

def lightload(iter_ind, delay):
    time.sleep(delay)
    print("At iter % " % (iter_ind))

    return iter_ind

"""
 If we should _not_ re-calclate, this function randomly switches to that we
 _should_ re-calculate
"""
def change_state(should_recalculate):
    if should_recalculate.value == 0:
        random.seed()
        if random.randint(0, 101) < 20:
            print("The world is a-changin!\n")
            should_recalculate.value = 1

def heavyload_loop(looping_time, sim_time, should_recalculate):

    t1 = time.time()
    while(time.time() - t1 < sim_time):
        print(time.time() - t1)
        t1 = time.time()
        if should_recalculate.value > 0:
            heavyload(looping_time)
            should_recalculate.value = 0
            print("Done re-calculating at ", time.time() - t1)

        time.sleep(1.0)

def lightload_loop(delay, sim_time, should_recalculate):

    t1 = time.time()
    while(time.time() - t1 < sim_time):
        if should_recalculate.value > 0:
            print("Sleep")
        else:
            print("Walk")

        time.sleep(delay)

def recalculate_loop(delay, sim_time, should_recalculate):
    t1 = time.time()
    while(time.time() - t1 < sim_time):
        change_state(should_recalculate)
        time.sleep(delay)


if __name__ == "__main__":

    should_recalculate = multiprocessing.Value('i')
    should_recalculate.value = 1 # Start with the need for re-calculation

    heavyload_t = 2.0
    recalc_sample_time = 2.5
    inner_loop_sample_time = 0.3

    tot_sim_time = 10.0

    # creating new process
    inner_p = multiprocessing.Process(target=lightload_loop, args=(inner_loop_sample_time, tot_sim_time, should_recalculate))
    outer_p = multiprocessing.Process(target=heavyload_loop, args=(heavyload_t, tot_sim_time, should_recalculate))
    env_p = multiprocessing.Process(target=recalculate_loop, args=(recalc_sample_time, tot_sim_time, should_recalculate))

    # starting process
    inner_p.start()
    outer_p.start()
    env_p.start()

    inner_p.join()
    outer_p.join()
    env_p.join()

    # print result array
    print("Done!")
