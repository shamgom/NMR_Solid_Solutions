!*******************************************************************************
!    Copyright (c) 2014 Ricardo Grau-Crespo, Said Hamad
!    Versión completa: z=0-6, espectro global y suma total
!*******************************************************************************

PROGRAM sod_broadening 
  IMPLICIT NONE

  INTEGER,PARAMETER :: NMAX=10000
  INTEGER :: iconf, ipeak, nconfs, npeaks, npoints, z, z_values(7) = [0,1,2,3,4,5,6]
  REAL(kind=8)  :: x, xmin, xmax, sigma, range, step, spectrum, total_spectrum(NMAX)
  INTEGER :: i, j, current_z
  REAL(kind=8),DIMENSION(NMAX,NMAX) :: peaks
  INTEGER,DIMENSION(NMAX,NMAX) :: neighbours
  CHARACTER(len=1000) :: line, filename
  INTEGER :: ios, count
  real :: rdummy(17)
  logical :: valid

  ! Abrir archivos de entrada
  open(10, FILE='INBROAD', STATUS='OLD')
  open(14, file='neighbours_list.txt', status='old', action='read')
  open(16, file='PEAKS.txt', status='old', action='read')

  ! Leer parámetros
  read(10,*) 
  read(10,*) npeaks
  read(10,*) 
  read(10,*) xmin
  read(10,*) 
  read(10,*) xmax
  read(10,*) 
  read(10,*) npoints
  read(10,*) 
  read(10,*) sigma

  ! -------------------------------
  ! Procesar archivos base
  ! -------------------------------
  open(15, file='NEIGHBOURS', status='replace')
  nconfs = 0
  do
    read(14, '(A)', iostat=ios) line
    if (ios /= 0) exit
    
    valid = .false.
    read(line, *, iostat=ios) rdummy(1:npeaks)
    if (ios == 0) then
      read(line, *, iostat=ios) rdummy(1:npeaks+1)
      if (ios /= 0) valid = .true.
    endif
    
    if (valid) then
      write(15, '(A)') trim(line)
      nconfs = nconfs + 1
    endif
  enddo
  close(14)
  close(15)

  open(17, file='PEAKS', status='replace')
  do
    read(16, '(A)', iostat=ios) line
    if (ios /= 0) exit
    
    valid = .false.
    read(line, *, iostat=ios) rdummy(1:npeaks)
    if (ios == 0) then
      read(line, *, iostat=ios) rdummy(1:npeaks+1)
      if (ios /= 0) valid = .true.
    endif
    
    if (valid) write(17, '(A)') trim(line)
  enddo
  close(16)
  close(17)
END PROGRAM sod_broadening
