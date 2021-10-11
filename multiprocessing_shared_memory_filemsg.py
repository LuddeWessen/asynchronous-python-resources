import multiprocessing
import time
import math
import random
import json
import os

def Json2Dict(fname):
    with open(fname, "r") as read_content:
        v_dict = json.load(read_content)

    os.remove(fname)

    return v_dict

def Var2Json(var_dict, fname):
    with open(fname, "w") as file:
        json.dump(var_dict, file)


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
            should_recalculate.value = 2

def heavyload_loop(looping_time, should_recalculate, var_names, fname):

    v_dict = {}
    for name in var_names:
        v_dict[name] = [0,1,2]

    random.seed()
    while(True):
        t1 = time.time()
        if should_recalculate.value > 1:
            heavyload(looping_time)
            for name in var_names:
                if random.randint(0, 101) < 20:
                    t_ind = random.randint(0, 2)
                    v_dict[name][t_ind] = v_dict[name][t_ind]+1

            t1 = time.time()
            no_rw_times = 10000
            for i_ in range(no_rw_times):
                Var2Json(v_dict, fname)
                Json2Dict(fname)
            Var2Json(v_dict, fname)
            print("Write/read per rw: ", (time.time()-t1)/no_rw_times)

            should_recalculate.value = 1 # just re-calculated, but it hasn't been picked up yet
            print("Done re-calculating")

        time.sleep(1.0)

def lightload_loop(delay, should_recalculate, var_names, fname):

    while(True):
        t1 = time.time()
        if should_recalculate.value > 0:
            print("Sleep")
            if should_recalculate.value == 1:
                print(Json2Dict(fname))
                should_recalculate.value = 0 # value is picked up
        else:
            print("Walk")

        time.sleep(delay)

def recalculate_loop(delay, should_recalculate):
    while(True):
        change_state(should_recalculate)
        time.sleep(delay)


if __name__ == "__main__":
    var_names = ["task", "a_location", "duration"]
    fname = "var_val_dump.json"

    should_recalculate = multiprocessing.Value('i')
    should_recalculate.value = 2 # Start with the need for re-calculation

    heavyload_t = 2.0/5
    recalc_sample_time = 2.5/5
    inner_loop_sample_time = 0.3/5

    # creating new process
    inner_p = multiprocessing.Process(target=lightload_loop, args=(inner_loop_sample_time, should_recalculate, var_names, fname))
    outer_p = multiprocessing.Process(target=heavyload_loop, args=(heavyload_t, should_recalculate, var_names, fname))
    env_p = multiprocessing.Process(target=recalculate_loop, args=(recalc_sample_time, should_recalculate))

    # starting process
    inner_p.start()
    outer_p.start()
    env_p.start()

    inner_p.join()
    outer_p.join()
    env_p.join()

    # print result array
    print("Done!")
