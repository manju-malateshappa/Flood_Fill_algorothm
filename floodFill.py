
#dimension of the M * N matrix of colors
M = 8
N = 8

#method  - print_matrix
# prints the matrix
def print_matrix():
  for i in range(M): 
    for j in range(N): 
        print(image[i][j], end = ' ') 
    print()

# floodFillHelper  
# A recursive function to replace   'target_color' at '(x, y)' with  replacement_color
# and all surrounding pixels of (x, y)  
# with new color 'replacement_color' 
def floodFillHelper(image, x, y, target_color, replacement_color): 
      
    # Base cases 
    if (x < 0 or x >= M or y < 0 or 
        y >= N or image[x][y] != target_color or 
        image[x][y] == replacement_color): 
        return
  
    # Replace the color at (x, y) 
    image[x][y] = replacement_color 
  
    # Recur for north, east, south and west 
    floodFillHelper(image, x + 1, y, target_color, replacement_color) 
    floodFillHelper(image, x - 1, y, target_color, replacement_color) 
    floodFillHelper(image, x, y + 1, target_color, replacement_color) 
    floodFillHelper(image, x, y - 1, target_color, replacement_color) 

#method  - floodFill
def floodFill(image, x, y, replacement_color): 
    target_color = image[x][y] 
    floodFillHelper(image, x, y, target_color, replacement_color) 


image = [[1, 1, 1, 1, 1, 1, 2, 1],  
          [1, 1, 0, 1, 1, 1, 0, 0],  
          [1, 0, 0, 1, 1, 0, 1, 1],  
          [1, 2, 2, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 2, 2, 0],  
          [1, 1, 1, 0, 1, 2, 1, 1],  
          [2, 1, 1, 1, 1, 2, 2, 1]] 
  
# start node
x = 3
y = 3
#replacement color
replacement_color = 4
print("orginial M * N matrix of colors")
print_matrix()
floodFill(image, x, y, replacement_color)
  
print ("Updated M * N matrix of colors after call to floodFill:") 
print_matrix()
  
