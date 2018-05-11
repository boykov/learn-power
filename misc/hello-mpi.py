#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Installation:
# Check module with mpi.h
module list # => for e.g. spectrum_mpi
pip install --user mpi4py

mpirun -n 4 python hello-mpi.py
"""
import sys
import os
from mpi4py import MPI

comm = MPI.COMM_WORLD

id = comm.Get_rank()

p = comm.Get_size()

if ( id == 0 ):
  print ""
  print "HELLO_MPI:"
  print "  P", id, ":  There are ", p, " MPI processes running."

print "  P", id, ":  Hello, world!"
os.system("hostname")
