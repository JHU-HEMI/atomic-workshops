program read_numbers
      implicit none
      integer :: nnn, kkk
      real :: fff
      OPEN(10, file='test_numbers.txt')
      read(10,'(I4)') nnn
      print*, nnn
      read(10,'(f3.1)') fff
      print*, fff
      read(10,*) nnn
      print*, nnn
      read(10,'(2I3)') nnn,kkk
      print*, nnn,kkk
      read(10,*) nnn
      print*, nnn
      read(10,*) nnn
      print*, nnn
      read(10,*) nnn
      print*, nnn

end program read_numbers