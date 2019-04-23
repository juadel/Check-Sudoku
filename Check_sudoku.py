def check_sudoku(sudo):
    
    # Checking if matrix is valid
    columns = len(sudo)
    print(sudo)
    for i in sudo:
        if len(i) != columns :
            print ("Matrix is not square")
            return False
        for num in i:
            if type(num) != int: 
                print(" Matrix not contain Integers")
                return False
     
    # Checking numbers in order per row
    
    for each_row in sudo:
      a = list(range(1,columns+1))
      for digit in each_row:
          if digit in a:
             a.pop(a.index(digit))
          else:
              print(" Sudoku is not Correct ") 
              return False
   
     # Checking numbers in order per columns  
    a= list(range(1,columns+1))
    num2 =0
    while num2 != columns-1:
        num = 0
        num2 +=1
        a= list(range(1,columns+1))
        while num != columns-1:
            
            if sudo[num][num2] in a:
                
                a.pop(a.index(sudo[num][num2]))
                num += 1
                
            else:
                print(" Sudoku is not Correct ") 
                return False
      

    print ("Sudoku is Correct")
    return True


test1 = [[2,1,3,4],[1,3,1,4],[3,1,2,4],[4,4,3,1]]
test2 = [[1,2,3,4],  
             [2,3,1,3], 
             [3,1,2,3],
             [4,4,4,4]]

test3 = [[1,2,3,4],
             [2,3,4,1],
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

check_sudoku(test2)
check_sudoku(test3)
check_sudoku(test4)
check_sudoku(test5)
check_sudoku(test6)

