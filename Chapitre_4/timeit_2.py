#!/usr/bin/env python3
import timeit
import doctest_1

executions = 5
executions_par_test = 1000
range_mul = 1000

def timeit_int_fois_deux():
    for i in range(range_mul):
        doctest_1.int_fois_deux(i)

def timeit_int_fois_deux_op():
    for i in range(range_mul):
        doctest_1.int_fois_deux_op(i)

def affiche_resultats(temps):
    for e, secondes in enumerate(temps):
        execution = e + 1
        print('Execution #{0} => {1} sec'.format(execution, secondes))

def chronometre(main, setup):
    t = timeit.Timer(main, setup)
    resultats = t.repeat(executions, executions_par_test)
    print('Avec ' + main)
    affiche_resultats(resultats)

if __name__ == '__main__':
    setup = 'from __main__ import timeit_int_fois_deux, timeit_int_fois_deux_op'
    main = 'timeit_int_fois_deux()'
    chronometre(main, setup)

    main = 'timeit_int_fois_deux_op()'
    chronometre(main, setup)
