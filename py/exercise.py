#!/usr/bin/env python

import tkMessageBox
from datetime import date, timedelta
from geom import find_ratio
from pseudo import transpose_dict
from math import floor

def count(total):
    zero = date(2011, 1, 16)
    then = date(2011, 12, 31)
    a_day = timedelta(1)
    ratio = find_ratio(date.toordinal(then) - date.toordinal(zero) + 2, total + 1)
    count = 0
    days = []
    increment = ratio
    for i in range(total + 1):
        days.append(increment)
        increment *= ratio
    intdays = []
    for i in range(total + 1):
        intdays.append(int(floor(sum(days[:i+1])))-int(floor(sum(days[:i]))))
    sortdays = sorted(intdays)
    sortdays.reverse()
    exercise_reps = {}
    the_day = zero
    interval = sortdays.pop()
    while the_day < then:
        the_day += a_day
        if date.toordinal(the_day) - date.toordinal(zero) >= interval:
            count += 1
            zero = the_day
            interval = sortdays.pop()
        exercise_reps[the_day] = count
    return exercise_reps

def all_counts():
    reps = {}
    reps['Ranger clap'] = count(150)
    reps['Sit-up'] = count(100)
    reps['Squat'] = count(75)
    reps['Push-up'] = count(50)
    reps['Calf-raise'] = count(25)
    reps['Dip'] = count(25)
    reps['Pull-up'] = count(15)
    reps['Chin-up'] = count(10)
    return transpose_dict(reps)

def today_counts(reps):
    order = ['Pull-up', 'Push-up', 'Squat', 'Ranger clap', 'Sit-up', 'Calf-raise', 'Dip','Chin-up']
    message = ''
    for exercise in order:
        message += exercise+' '+str(reps[exercise])+'\n'
    return message

if __name__ == '__main__':
    tkMessageBox.showinfo('', today_counts(all_counts()[date.today()]))
