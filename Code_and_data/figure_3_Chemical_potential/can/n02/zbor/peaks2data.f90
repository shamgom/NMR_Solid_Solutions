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

       INTEGER,PARAMETER :: NMAX=1000
       INTEGER :: h, i, npeaks, npoints, k
       REAL (kind=8)  :: sigma, wa, range, step, fw, freq
       REAL (kind=8),DIMENSION(NMAX) :: w, y
       open (10, FILE='sod_broadening_in.dat', STATUS='OLD')
       open (11, FILE='sod_broadening_out.dat')

       sigma=40.0
       npoints=9000
       wa=0.1D0
       !wini=
       !wfin=

       h=1
 1     continue
       read(10,*,end=10) w(h),y(h)
       h=h+1
       goto 1
  10   continue
       npeaks=h-1

!       write(*,*) "There are",npeaks,"peaks"
       range=(w(npeaks)-w(1))*(1.0D0+3*wa)
!       write(*,*) "The range is:",range
       step=range/npoints
!       write(*,*) "The step is:",step

           freq=w(1)-wa*range
!       write(*,*) "The initial freq is:",freq
       do i=1,npoints
          freq=freq+step*(1.0D0-wa/2.0D0)
          fw=0.0D0
          do k=1,npeaks
             fw=fw+(y(k)/sigma)*exp(-(freq-w(k))**2/(2*sigma**2)) 
          enddo
          write(*,*) freq,fw
          write(11,*) freq,fw
       enddo

       stop
       end
