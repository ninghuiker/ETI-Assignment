#Read and Load Function 
def Read_Load():
    print('Option [1] Read and load maze from file')
    print('')
    userinput = input('Enter the name of the data file:')
    file = open(userinput)
    row = len(file.readlines())
    print('Number of lines reads:', str(row))
    mainMenu()

