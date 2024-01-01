
class Matrixer:

    def __init__(self):
        self.matrix_list = dict()

    
    def new_matrix(self,name = None, row = 1, col = 1):
        """
        creating a new mtrix in No of row and column
        if no col and row specified, defaultly take 1 as row and col
        """

        # handling if the matrix name is not specified and already exists a matrix in the name name
        if name is None:
            raise Exception("a name for the matrix must be specified")
        elif name in self.matrix_list:
            raise Exception("A matrix already exists in this name")

        # new matrix as ints elements are None
        new_mtx = [[None for c in range(col)] for r in range(row)]
        self.matrix_list.update({name : new_mtx})
        
        return new_mtx
    
    def add_values(self, name = None ,values=[]):
        """
        matrix value is added from the list of the values is provided
        """

        # if matris name is not specified
        if name is None:
            raise Exception("Name for the matrix must be specified")
        
        # if any any matrix is found in the name
        matx = self.matrix_list.get(name)
        if matx is None:
            raise Exception("Matrix not found: %s" % name)

        # if matrix is found, match the elements of matrix is equal to the values are given in the list
        matrix_len = len(matx) * len(matx[0])       # number of elemens is = len of matrix(row) * len of first row(column)
        values_len = len(values)                    # number of values        
        if matrix_len != values_len:
            raise Exception("Provided values lengths do not match with this matrix elements length")

        # add values to the matrix
        pointer = 0
        for row in matx:
            for i in range(len(row)):
                row[i] = values[pointer]
                pointer += 1
        
        return matx
    
    def get_matrix(self, name=None):
        """
        Returns specified named matrix
        if name is not passed, returns all matirix
        if there is no matrix found returns None
        """
        if name:
            matx = self.matrix_list.get(name)
            if matx is None:
                return None
            return matx
        else:
            return self.matrix_list

    def add_matrix(self, *args):
        """
        matrix name is passes as an args
        because it contains multiple matrices
        """
        if len(args) <= 1:
            raise Exception("for addition atleast two matrix names muxt be provided")
        
        # validating all the passed matrix are valied
        mx_row_length_list = set()
        mx_col_length_list = set()

        for mx in args:
            if mx not in self.matrix_list:
                raise Exception("Matrix not found: %s" % mx)
            
            mx_row_length_list.add(len(self.matrix_list.get(mx)))
            mx_col_length_list.add(len(self.matrix_list.get(mx)[0]))
        
        if len(mx_row_length_list) > 1 or len(mx_col_length_list) > 1:
            """
            all the matrix order is added to the mx_col_length_list and mx_row_length_list
            if any of the matrix length is different the mx_length_list set length will be grate that 1
            it means the matrix is not in the same length and order, it agains the matrix addition
            """
            raise Exception("Matrxi shoud be same length and order to perform addition")
        
        row_len = list(mx_row_length_list)
        col_len = list(mx_col_length_list)

        # matrix addition
        resultant_matrix = list()
        matrices = [self.matrix_list[mat] for mat in args]
        

        for i in range(row_len[0]):
            resultant_row = []
            for j in range(col_len[0]):
                
                # finding each positions total and store in value
                # then append to resultant fow
                value = 0
                for matx in matrices:
                    value += matx[i][j]
                resultant_row.append(value)
            
            # after row addition is over, the row is appended to the resultant matrix
            resultant_matrix.append(resultant_row)
        
        return resultant_matrix



    def substract_matrix(self):
        pass
    

    def multiply_with_scalar(self, name = None, scalar = None):
        """
        multiply with given scalar
        """

        # rise exception if scalar is not passed
        if name is None:
            raise Exception('Name must not be None')
        if scalar is None:
            raise Exception("Scalar not provided")
        
        matx = self.matrix_list.get(name)
        if matx is None:
            raise Exception("No matrix found")
        
        # multiply with scalar
        for row in matx:
            for i in range(len(row)):
                row[i] *= scalar

        return matx
    

    def matrix_multiply(self, mat1, mat2):
        """
        accepting two matrix names and validate it, for multiplications
        """

        # if no matrix is found, raise exception
        if mat1 not in self.matrix_list or mat2 not in self.matrix_list:
            raise Exception("Matrix not found")

        matx1 = self.matrix_list[mat1]
        matx2 = self.matrix_list[mat2]

        # checking matrix multiplication rules
        if len(matx1[0]) != len(matx2):
            raise Exception("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
        
        resultant_matrix = []
        
        # Multiplication Logic
        for i in range(len(matx1)):
            
            temp_row = []
            
            for j in range(len(matx2[0])):
                
                mat_elmnt_sum = 0

                for k in range(len(matx1[0])):
                    
                    mat_elmnt_sum += matx1[i][k] * matx2[k][j]
                
                temp_row.append(mat_elmnt_sum)
            
            resultant_matrix.append(temp_row)

        
        return resultant_matrix
    



d = None




        
    
                
