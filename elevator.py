"""
elevator program

takes parameters: 
1. capacity of a single elevator
2. time of day
3. length of elevator journey

returns: 
1. wait time based on time of day
2. recommended number of elevators for building
"""

import math
import random
import csv
import sqlite3

ELEV_CAPACITY = 4
BUSY_WEIGHT = 2
DEAD_WEIGHT = 0.1
JOURNEY_TIME = 15
MAX_WAIT_TIME = 2

arrival_time_weights = {0: DEAD_WEIGHT, 1: DEAD_WEIGHT, 2: DEAD_WEIGHT, 3: DEAD_WEIGHT, 4: DEAD_WEIGHT, 7: BUSY_WEIGHT, 8: BUSY_WEIGHT, 11: BUSY_WEIGHT, 12: BUSY_WEIGHT}

def calc_ppl_arrived(time):
    ppl_arrived = random.randint(0,20)
    """
    to test, replace the above line with:
    ppl_arrived = 2
    """
    if arrival_time_weights.get(time):
        ppl_arrived *= arrival_time_weights[time]
        ppl_arrived = math.ceil(ppl_arrived)
    else:
        pass
    return ppl_arrived

def test_calc_ppl_arrived():
    assert calc_ppl_arrived(0) == 1
    assert calc_ppl_arrived(7) == 10
    assert calc_ppl_arrived(9) == 2

def calc_elev_avail(rec_elevators):
    elev_avail = random.randint(0, rec_elevators)
    """
    to test, replace the above line with:
    elev_avail == 5
    """
    return elev_avail

def test_calc_elev_avail():
    assert calc_elev_avail(10) == 5

def elevators_needed(ppl_arrived, ELEV_CAPACITY):
    elev_needed = math.ceil(ppl_arrived / ELEV_CAPACITY)
    return elev_needed

def test_elevators_needed():
    assert elevators_needed(4, 3) == 2

def wait_time(elev_needed, elev_avail):
    if elev_needed > elev_avail:
        waiting_time = (elev_needed - elev_avail) * JOURNEY_TIME
    else:
        waiting_time = 0
    return waiting_time

def test_wait_time():
    assert wait_time(5, 2) == 10
    assert wait_time(5, 4) == 5
    assert wait_time(5, 6) == 0
    
def main():
    with open("/mnt/c/Users/emmar/Documents/data/elevator_capacity/prod/elevator_data.csv", 'w') as elevator_data:
        elevator_writer = csv.writer(elevator_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        elevator_writer.writerow(['Elevator Simulation Report'])
        elevator_writer.writerow(['This model predicts the recommended number of elevators for a 50-story building by analyzing the elevator wait time in the lobby.'])
        elevator_writer.writerow([])
        elevator_writer.writerow(['run', 'trial', 'time', 'line_length', 'elev_needed', 'elev_avail', 'wait_time', 'total_wait_today', 'avg_wait_today', 'recommended_elev'])

        run_number = 0

        while run_number < 5:
            run_number += 1
            rec_elevators = 9
            avg_wait_time = 20
            trial = 0

            while avg_wait_time > MAX_WAIT_TIME:
                rec_elevators += 1
                trial += 1
                total_wait_time = 0
                for time_now in range(0,13):
                    ppl_arrived = calc_ppl_arrived(time_now)
                    elev_needed = elevators_needed(ppl_arrived, ELEV_CAPACITY)
                    elev_avail = calc_elev_avail(rec_elevators)
                    waiting_time = wait_time(elev_needed, elev_avail)
                    total_wait_time += waiting_time
                    avg_wait_time = total_wait_time / (time_now + 1)
                    elevator_writer.writerow([run_number, trial, time_now, ppl_arrived, elev_needed, elev_avail, waiting_time, total_wait_time, avg_wait_time])

            elevator_writer.writerow([run_number, '', '', '', '', '', '', '', '', rec_elevators])

if __name__ == "__main__":
    main()