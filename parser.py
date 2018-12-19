import re
import helper as hlp
import testcase as tc
import pygraphviz as pgv
# Graph.add_node(2,label = 'temp')

class parser():

    def __init__(self):
        self.tokens = tc.tokens
        self.types = tc.types
        self.t_index = 0
        self.current_token = self.tokens[self.t_index]
        self.graph = pgv.AGraph()
        self.graph.add_node('m')

    def drow(self):
        self.graph.draw('file1.png',prog='dot')     
    
    def factor(self):
        if(self.current_token == '('):
            print(self.types[self.t_index], self.current_token)
            self.match('(')
            self.expression()
            print(self.types[self.t_index], self.current_token)
            self.match(')')
        
        elif(hlp.is_num(self.current_token)):
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            self.graph.add_node(self.current_token)
            return self.graph.get_node(self.current_token)

        elif(self.is_identifier()):
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            self.graph.add_node(self.current_token)
            return self.graph.get_node(self.current_token)
            
            
    def expression(self):
        child = self.term()
        while self.is_addOp():
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            self.term()

    def program(self):
        self.stmt_seq()

    def stmt_seq(self):
        self.statement()    
        while self.is_semi_column():
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            self.statement()

    def statement(self):
        if self.current_token == 'if':
            self.if_stmt()
        elif self.is_identifier():
            self.assign_stmt()
        elif self.current_token == 'repeat':
            self.repeat_stmt()
        elif self.current_token == 'read':
            self.read_stmt()
        else:
            self.write_stmt()

    def if_stmt(self):
        print(self.types[self.t_index], self.current_token)
        self.match('if')
        self.bigExpression()
        print(self.types[self.t_index], self.current_token)
        self.match('then')
        self.stmt_seq()
        if self.current_token == 'end':
            print('End')
            print(self.types[self.t_index], self.current_token)
            self.match('end')
        elif self.current_token == 'else':
            print('else')
            print(self.types[self.t_index], self.current_token)
            self.match('else')
            self.stmt_seq()
            print(self.types[self.t_index], self.current_token)
            self.match('end')

    
    def repeat_stmt(self):
        print(self.types[self.t_index], self.current_token)
        self.match('repeat')
        self.stmt_seq()
        print(self.types[self.t_index], self.current_token)
        self.match('until')
        self.bigExpression()

    def assign_stmt(self):
        print(self.types[self.t_index], self.current_token)
        self.match(self.current_token)
        print(self.types[self.t_index], self.current_token)
        self.match(':=')
        self.bigExpression()

    def read_stmt(self):
        print(self.types[self.t_index], self.current_token)
        self.match('read')
        if self.is_identifier():
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)

    
    def write_stmt(self):
        print(self.types[self.t_index], self.current_token)
        self.match('write')
        self.bigExpression()
        



    def bigExpression(self):
        self.expression()
        if self.is_comparisonOp():
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            self.expression()

        
    def term(self):
        child = self.factor()
        while self.is_mulOp():
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            self.factor()
        return child
    
    def writeStmnt(self):
        print(self.types[self.t_index], self.current_token)
        self.match(self.current_token)
        self.bigExpression()


    # def assign():
    #     expression()        
    #     while (token == ':='):
    #         None
#def stmt(self):
#switch(){

#    }


    def match(self, expectedToken):
        if(self.current_token == expectedToken):
            self.updateCurrentToken()
        else:
            print('errrooooooooooooooooooooooooooooor')

    def updateCurrentToken(self):
        self.t_index += 1
        # print(self.t_index)
        # print(len(self.tokens))
        if(self.t_index < len(self.tokens)):
            self.current_token = self.tokens[self.t_index]

    def is_identifier(self):
        return True if self.types[self.t_index] == 'identifier' else  False
    
    def is_addOp(self):
        return True if self.current_token == '+' or self.current_token == '-' else  False
        print(self.current_token)
    def is_mulOp(self):
        return True if self.current_token == '*' or self.current_token == '/' else  False
    def is_comparisonOp(self):
        return True if self.current_token == '<' or self.current_token == '=' else  False
    def is_semi_column(self):
        return True if self.current_token == ';' else False    