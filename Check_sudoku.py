def check_sudoku(sudo):
    
    n = len(sudo)
    
    for i in sudo:
       # print(len(i))
        #print(i)
        if len(i) != n :
            print ("Matrix is not square")
            return False
        for n in i:
            if type(n) != int: 
                print(" Matrix not contain Integers")
     
    a= list(range(1,n+1))
    for i in sudo:
      print(i)
      print(a)
      a = list(range(1,n+1))
      for n in i:
          if n in a:
              print(n)
              print(a)
              print(a.index(n))
              a.pop(a.index(n))
          #else:
           #    False
    print ("Sudoku Completed")


test1 = [[2,1,3],[2,3,1],[3,1,2]]
test2 = [[1,2,3,4],  
             [2,3,1,3], 
             [3,1,2,3],
             [4,4,4,4]]

test3 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

test4 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

test5 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

test6 = [ [1, 1.5],
               [1.5, 1]]
    
check_sudoku(test1)

#ujcheck_sudoku(test2)
#check_sudoku(test3)
#check_sudoku(test4)
#check_sudoku(test5)
#check_sudoku(test6)

