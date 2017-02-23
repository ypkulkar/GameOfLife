## prog6.py
## yashodhan kulkarni
## 10 march 2016
##
##
"""life() - takes in no agreements. Tells us what lives and what dies based on
the rules of Conway's Game of Life."""
def life():
    while True:
        file = input("Enter input file name: ")
        try:
            infile = open(file,"r")
            break
        except:
            print("No such file. Try again.")



    newlist = []
    for line in infile:
        line = line.replace("\n","")
        line = [int(i) for i in line]
        line.append(0)
        line.insert(0,0)
        newlist.append(line)
    zerorow = [0 for x in newlist[0]]
    newlist.append(zerorow)
    newlist.insert(0,zerorow)
    

   

    n = 1
    while True:
        try:
            limit = int(input("How many new generations would you like to print?  "))
            break
        except:
            print("Not a valid number.")
        
    outlist = newlist
    print("Generation:",0)
    for row in range(1,len(outlist)-1):
        for item in range(1,len(outlist[row])-1):
            if outlist[row][item] == 0:
                print(".",end = " ")
            if outlist[row][item] == 1:
                print("*",end = " ")
        print(" ")

    while n <= limit:
        print("Generation:",n)
        outlist = nextGen(outlist)
        for row in range(1,len(outlist)-1):
            for item in range(1,len(outlist[row])-1):
                if outlist[row][item] == 0:
                    print(".",end = " ")
                if outlist[row][item] == 1:
                    print("*",end = " ")
            print(" ")
        
        n = n+1
    infile.close()    
    print(" ")



    option = input("Would you like to save the latest generation? ('y' to save): ")
    if option != "y":
        print("End of program.")
    elif option == "y":
        while True:
            newname = input("Enter destination file name: ")
            try:
                savedfile = open(newname,"r")
                savedfile.close()
                xy = input("Do you want to overwrite that file? ('y' to continue): ")
                if xy != 'y':
                    newname = input("Enter destination file name: ")
                    savedfile = open(newname,"w")
                    for i in range(1,len(outlist)-1):
                        emptystr = ""
                        for j in range(1,len(outlist[0])-1):
                            emptystr = emptystr + str(outlist[i][j]) 
    
                        savedfile.write(emptystr + '\n')
                  
                    break
                elif xy == 'y':
                    savedfile = open(newname,'w')
                    for i in range(1,len(outlist)-1):
                        emptystr = ""
                        for j in range(1,len(outlist[0])-1):
                            emptystr = emptystr + str(outlist[i][j]) 
                        savedfile.write(emptystr + '\n')
                        
                    break
                    
                
                
                    
                    
                    
                    

            except:
                savedfile = open(newname,"w")
                for i in range(1,len(outlist)-1):
                    emptystr = ""
                    for j in range(1,len(outlist[0])-1):
                        emptystr = emptystr + str(outlist[i][j]) 
    
                    savedfile.write(emptystr + '\n')
                    
                break
            
        print(" ")
        print("Saving data to",newname)
        print(" ")
        print("End of program.")
                    
                        
                
        





            
           
    
        
        
 











def createGrid(rows,cols):
    """createGrid(rows,cols) - Takes in two agreements. Makes a new grid
    such that all elements are zero. Helps us to change any element easily"""
    cgrid = []
    for rows in range(0,rows):
        cgrid.append([])
        for column in range(0,cols):
            cgrid[rows].append(0)

    return cgrid


def nextGen(grid):
    """nextGen(grid) - Takes in a grid as an agreement. Applies Conway's Game
    of Life rules. Dead cells are 0 and alive are 1."""
    
    m = len(grid)
    n = len(grid[1])
    cgrid = createGrid(m,n)
    
    i = 1
    j = 1
    neighbour1 = 0
    neighbour0 = 0

    while i < m-1:
        
        while j < n-1:
            
            if grid[i][j] == 0:
                if grid[i-1][j-1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i-1][j-1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i-1][j] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i-1][j] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i-1][j+1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i-1][j+1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i][j-1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i][j-1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i][j+1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i][j+1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i+1][j-1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i+1][j-1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i+1][j] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i+1][j] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i+1][j+1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i+1][j+1] == 0:
                    neighbour0 = neighbour0 + 1
                if neighbour1 == 3:
                    cgrid[i][j] = 1
                neighbour1 = 0
                neighbour0 = 0





            if grid[i][j] == 1:
                if grid[i-1][j-1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i-1][j-1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i-1][j] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i-1][j] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i-1][j+1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i-1][j+1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i][j-1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i][j-1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i][j+1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i][j+1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i+1][j-1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i+1][j-1] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i+1][j] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i+1][j] == 0:
                    neighbour0 = neighbour0 + 1
                if grid[i+1][j+1] == 1:
                    neighbour1 = neighbour1 + 1
                if grid[i+1][j+1] == 0:
                    neighbour0 = neighbour0 + 1
                if neighbour1 >= 4:
                    cgrid[i][j] = 0
                if neighbour1 == 2 or neighbour1 == 3:
                    cgrid[i][j] = 1
 
                if neighbour1 <= 1:
                    cgrid[i][j] = 0
                neighbour1 = 0
                neighbour0 = 0
            j = j+1
            
        i = i+1
        j = 1
 
 

    return cgrid