########################################
# matrix_multiply example: http://www.bu.edu/tech/support/research/software-and-programming/programming/multiprocessor/gpu-computing/openacc-fortran/

mm-acc:
	module rm xl/13.1-15.1 spectrum_mpi && \
        module load pgi/17.4 openmpi/pgi/1.10.2/17.4 && \
        pgfortran -acc -Mcuda=cc60 -Mpreprocess -Minfo=accel mm.f90 -o mm_acc
	./mm_acc

mm-mp:
	module rm xl/13.1-15.1 spectrum_mpi && \
        module load pgi/17.4 openmpi/pgi/1.10.2/17.4 && \
        pgfortran -mp -Mpreprocess mm.f90 -o mm_omp
	OMP_NUM_THREADS=20 OMP_PLACES=cores ./mm_omp

########################################

clean:
	rm -f wallclocktime mm_acc mm_omp
