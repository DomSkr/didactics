#!/usr/bin/ENV python
import numpy
from mpi4py import MPI

NUMARRAYS = 100
ARRAYSIZE = 10000

ASK_FOR_WORK_TAG = 1
WORK_TAG = 2
WORK_DONE_TAG = 3
DIE_TAG = 4

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()

# Master
if rank == 0:
    data = numpy.empty(ARRAYSIZE, dtype=numpy.int32)
    sorted_data = numpy.empty([NUMARRAYS, ARRAYSIZE], dtype=numpy.int32)
    sorted_arrays = 0
    dead_workers = 0

    while dead_workers < size - 1:
        print("[Master] Probing")
        comm.Recv([data, ARRAYSIZE, MPI.INT], source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        print("[Master] Probed")

        dest = status.Get_source()
        if status.Get_tag() == ASK_FOR_WORK_TAG:
            if sorted_arrays <= NUMARRAYS - 1:
                print("[Master] got request for work from worker %d" % dest)
                data = numpy.random.random_integers(0, ARRAYSIZE, ARRAYSIZE).astype(numpy.int32)
                print("[Master] sending work to Worker %d" % dest)
                comm.Send([data, ARRAYSIZE, MPI.INT], dest=dest, tag=WORK_TAG)
                print("[Master] sent work to Worker %d" % dest)
            else:
                # Someone did more work than they should have
                print("[Master] Telling worker %d to DIE" % dest)
                comm.Send([data, ARRAYSIZE, MPI.INT], dest=dest, tag=DIE_TAG)
                dead_workers += 1
                print("[Master] Already killed %d workers" % dead_workers)

        elif status.Get_tag() == WORK_DONE_TAG:
            if sorted_arrays <= NUMARRAYS - 1:
                print("[Master] got results from Worker %d. Storing in line %d" % (status.Get_source(), sorted_arrays))
                sorted_data[sorted_arrays] = numpy.copy(data)
                with open("result.txt", "a") as result:
                    numpy.savetxt(result, data, newline=" ", fmt="%d")
                    result.write("\n")
                sorted_arrays += 1
# Slave
else:
    # Ask for work
    data = numpy.empty(ARRAYSIZE, dtype=numpy.int32)
    while True:
        print("[Worker %d] asking for work" % rank)
        comm.Send([data, ARRAYSIZE, MPI.INT], dest=0, tag=ASK_FOR_WORK_TAG)
        print("[Worker %d] sent request for work" % rank)

        comm.Recv([data, ARRAYSIZE, MPI.INT], source=0, tag=MPI.ANY_TAG, status=status)

        if status.Get_tag() == WORK_TAG:
            print("[Worker %d] got work" % rank)
            print("[Worker %d] is sorting the array" % rank)
            data.sort()
            print("[Worker %d] finished work. Sending it back" % rank)
            comm.Send([data, ARRAYSIZE, MPI.INT], dest=0, tag=WORK_DONE_TAG)
        elif status.Get_tag() == DIE_TAG:
            print("[Worker %d] DIE" % rank)
            break
        else:
            print("[Worker %d] Doesn't know what to do with tag %d right now" % (rank, status.Get_tag()))
