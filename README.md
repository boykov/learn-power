Learn OpenPOWER
===============

See [jupiter](http://jupiter.febras.net/ganglia/) and [OpenPOWER cluster](http://lits.ccfebras.ru/index/oborudovanie/sistemyi-vyisokoproizvoditelnyix-vyichislenij/gibridnogo-vyichislitelnogo-klastera-na-baze-arxitekturyi-openpower.html)

CUDA Fortran Book
-----------------

    cd CUDA-Fortran-Book
    module unload xl/13.1-15.1 && module load pgi/17.4 && make all

Shared library
--------------

Add PGI Fortran shared library to GNU Fortran program.

    cd CUDA-Fortran-Book/boykov/increment
	make runinc
