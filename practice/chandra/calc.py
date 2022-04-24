

class Calculator:

    def __init__(self):
        self.x=10
        self.y=20

    def sum(self, x,y,*z, **p):
        print("x = ",x)
        print("y = ",y)
        print("z =", *z)
        print("call of method : ",p['methodname'])
        j=0
        for i in z:
            j+=i      # j=j+i
        return x+y+j

    def sub(self, x=0,y=0):
        return x-y

    def mult(self, x=0,y=0):
        return x*y

    def div(self, x=0,y=0):
        return x/y

    def sqlQuery(self, dbname, tablename, *col_name):
        col_names=str(col_name)
        print(col_names)
        col_names=col_names.replace('(','')
        col_names=col_names.replace(')','')
        col_names=col_names.replace("'",'')

        # for i in col_name:
        #     col_names = ''.join(i)

        query=f"select {col_names} from {dbname}.{tablename}"
        return query



obj = Calculator()
# print("sum is =  ",obj.sum(1,8,2,3,4,5,6, name='Chandra', methodname='sum'))
print(obj.sqlQuery("l1schema", '''mtg_arrg''', "crd_arrg_dim"))



# variable no. of params
#*args
#**kwargs