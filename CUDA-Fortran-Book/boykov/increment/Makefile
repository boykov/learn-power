
#
#     Copyright (c) 2017, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.
# 

OPT=-O2
FC=pgf90
F90FLAGS = $(OPT)
OBJ=o
EXE=out
RUN=
UNAME := $(shell uname -a)
ifeq ($(findstring CYGWIN_NT, $(UNAME)), CYGWIN_NT)
   OBJ=obj
   EXE=exe
endif

gf = gfortran -fopenmp -ffree-line-length-none -fPIC -O3 -funroll-loops

# Uncomment the CUDAFLAGS line if you have hardware requirements that require
# a specific compute capability
CUDAFLAGS = -Mcuda=cc60

libincrement.so: increment.o
	$(FC) $(CUDAFLAGS) $(F90FLAGS)  -fpic -shared -o libincrement.so $<

increment.o: increment.cuf
	module unload xl/13.1-15.1 && module load pgi/17.4 && $(FC) $(CUDAFLAGS) $(F90FLAGS) -c -fpic increment.cuf

inc: inc.f90 libincrement.so
	$(gf) -c inc.f90
	$(gf) -L. inc.o -lincrement -o inc

runinc: inc
	LD_LIBRARY_PATH=. ./inc

all: build run verify

build: increment.cuf
	$(FC) $(CUDAFLAGS) $(F90FLAGS) -o increment.$(EXE) $<

run: increment.$(EXE)
	$(RUN) ./increment.$(EXE)

verify:

clean:
	@echo 'Cleaning up...'
	@rm -rf increment.$(EXE) *.$(OBJ) *.mod *.dwf *.pdb prof inc *.so

