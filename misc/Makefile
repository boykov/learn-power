mm:
	module rm xl/13.1-15.1 spectrum_mpi && \
        module load pgi/17.4 openmpi/pgi/1.10.2/17.4 && \
        pgfortran -acc -Mcuda=cc60 -Minfo=accel mm.f90 -o mm_acc
	./mm_acc

clean:
	rm fort.11 mm_acc 
