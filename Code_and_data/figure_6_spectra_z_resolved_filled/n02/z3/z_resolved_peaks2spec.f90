!*******************************************************************************
!    Copyright (c) 2014 Ricardo Grau-Crespo, Said Hamad
!
!    This file is part of the SOD package.
!
!    SOD is free software: you can redistribute it and/or modify
!    it under the terms of the GNU General Public License as published by
!    the Free Software Foundation, either version 3 of the License, or
!    (at your option) any later version.
!
!    SOD is distributed in the hope that it will be useful,
!    but WITHOUT ANY WARRANTY; without even the implied warranty of
!    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!    GNU General Public License for more details.
!
!    You should have received a copy of the GNU General Public License
!    along with SOD.  If not, see <http://www.gnu.org/licenses/>.
!
!******************************************************************************

       PROGRAM sod_broadening 

       IMPLICIT NONE

       INTEGER,PARAMETER :: NMAX=10000
       INTEGER :: iconf, ipeak, nconfs, npeaks, npoints
       REAL (kind=8)  :: x, xmin, xmax, sigma, range, step, spectrum
       INTEGER :: h, i, j, k
       REAL (kind=8),DIMENSION(NMAX) :: w, y
       REAL (kind=8),DIMENSION(NMAX,NMAX) :: peaks, spectra
       INTEGER,DIMENSION(NMAX,NMAX) :: nnn
       INTEGER :: num, ios, z
       CHARACTER(len=1000) :: line
       INTEGER :: a, b, c, d, iostat, count
       REAL (kind=8) :: delta  ! Added delta variable
       open (10, FILE='INBROAD', STATUS='OLD')
       open (11, FILE='PEAKS', STATUS='OLD')
       open (12, FILE='SPECTRA')
       open (13, FILE='XSPEC')
       open (14, FILE='NEIGHBOURS', STATUS='OLD', ACTION='read')

!INPUT:

!#PEAKS
!#p1 ..... p14
!#p1 ..... p14
!#p1 ..... p14
!
!OUTPUT:

!#DATA
!#1000
!#Ixmin .... Ixmax (conf 1)
!#Ixmin .... Ixmax (conf 2)
!#Ixmin .... Ixmax (conf 3)

       read(10,*) 
       read(10,*) z
       read(10,*) 
       read(10,*) nconfs
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
  ! Load data 
  ! -------------------------------
       read(11, *)  ((peaks(ipeak, iconf), ipeak = 1, npeaks), iconf = 1, nconfs)               
       read(14, *)  ((nnn(ipeak, iconf), ipeak = 1, npeaks), iconf = 1, nconfs)  ! Corrected unit and variable
       close(11)
       close(14)


  ! -------------------------------
  ! Create spectra 
  ! -------------------------------
       range=xmax-xmin
       step=range/(npoints-1)
       write(*,*) "The initial x is:",x
       x = xmin
       do i=1,npoints
          write(*,*)
          write(*,*) 'npoints=',i,'x=',x
          do iconf=1,nconfs
             spectrum=0.0d0
             do ipeak=1,npeaks
                ! Calculate delta based on z and neighbours
                if (z == -1 .or. nnn(ipeak, iconf) == z) then
                    delta = 1.0d0
                else
                    delta = 0.0d0
                endif
                spectrum = spectrum + delta * (1.0d0/(sigma*sqrt(2.0d0*3.141592653589793d0)) * &
                           exp(-(x - peaks(ipeak,iconf))**2/(2.0d0*sigma**2)))
             enddo
             spectra(i,iconf) = spectrum
             write(*,*) 'x=',x,'xcalc=',REAL(xmin+i*step),'iconf=',iconf,'spectra=',spectra(i,iconf)
          enddo
          x=x+step
       enddo

       write(12,*) npoints
       do iconf=1,nconfs
          write(12,*) (spectra(i,iconf), i = 1, npoints)
       enddo

 100   format(f8.1)
       do i=0,npoints-1
          write(13,100) xmin+step*i
       enddo

stop 
end
