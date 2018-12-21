import re
import helper as hlp
import pygraphviz as pgv

class parser():

    def __init__(self, tokens, types):
        self.nonTerminals = ['READ','WRITE','IF','REPEAT']
        self.tokens = tokens
        self.types = types
        self.t_index = 0
        self.current_token = self.tokens[self.t_index]
        self.graph = pgv.AGraph()
        self.id = 0
        self.stmt_seq()

    def drow(self):
        self.graph.draw('output.png',prog='dot')     
    
    def factor(self):
        if(self.current_token == '('):
            print(self.types[self.t_index], self.current_token)
            self.match('(')
            temp = self.simpleExp()
            print(self.types[self.t_index], self.current_token)
            self.match(')')
            return temp
        
        elif(hlp.is_num(self.current_token) or self.is_identifier()):
            print(self.types[self.t_index], self.current_token)
            parent = self.tree()
            self.match(self.current_token)
            return parent
            
    def term(self):
        temp = self.factor()
        while self.is_mulOp():
            print(self.types[self.t_index], self.current_token)
            parent = self.tree()
            self.match(self.current_token)
            leftChild = temp
            rightChild = self.factor()
            self.edge(parent, leftChild, rightChild)
            temp = parent
        return temp

    def simpleExp(self):
        temp = self.term()
        while self.is_addOp():
            parent = self.tree()
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            leftChild = temp
            rightChild = self.term()
            self.edge(parent, leftChild, rightChild)
            temp = parent
        return temp

    def stmt_seq(self):
        temp = self.statement() 
        nativeChild = temp
        while self.is_semi_column():
            print(self.types[self.t_index], self.current_token)
            self.match(self.current_token)
            leftChild = temp
            rightChild = self.statement()
            self.connectHorizontal(leftChild, rightChild)
            temp = rightChild
        return nativeChild

    def statement(self):
        if self.current_token == 'if':
            return self.if_stmt()
        elif self.is_identifier():
            return self.assign_stmt()
        elif self.current_token == 'repeat':
            return self.repeat_stmt()
        elif self.current_token == 'read':
            return self.read_stmt()
        else:
            return self.write_stmt()

    def if_stmt(self):
        print(self.types[self.t_index], self.current_token)
        parent = self.tree()
        self.match('if')
        leftChild = self.exp()
        print(self.types[self.t_index], self.current_token)
        self.match('then')
        middleChild = self.stmt_seq()
        if self.current_token == 'end':
            print(self.types[self.t_index], self.current_token)
            self.edge(parent, leftChild, middleChild)
            self.connectHorizontal(leftChild, middleChild, color='white')
            self.match('end')
        elif self.current_token == 'else':
            # print('else')
            print(self.types[self.t_index], self.current_token)
            self.match('else')
            rightChild = self.stmt_seq()
            print(self.types[self.t_index], self.current_token)
            self.edge(parent, leftChild)
            self.edge(parent, middleChild, rightChild)
            self.connectHorizontal(leftChild, middleChild, color='white')
            self.connectHorizontal(middleChild, rightChild, color='white')
            self.match('end')
        return parent
    
    def repeat_stmt(self):
        print(self.types[self.t_index], self.current_token)
        parent = self.tree()
        self.match('repeat')
        leftChild = self.stmt_seq()
        print(self.types[self.t_index], self.current_token)
        print(self.current_token)
        self.match('until')
        rightChild = self.exp()
        self.edge(parent, leftChild, rightChild)
        return parent

    def assign_stmt(self):
        print(self.types[self.t_index], self.current_token)
        parent = self.tree()
        self.match(self.current_token)
        print(self.types[self.t_index], self.current_token)
        self.match(':=')
        child = self.exp()
        self.edge(parent, child)
        return parent

    def read_stmt(self):
        print(self.types[self.t_index], self.current_token)
        self.match('read')
        print(self.types[self.t_index], self.current_token)
        label = 'READ \n'+ self.current_token
        parent = self.tree(label)
        self.match(self.current_token)
        return parent

    def write_stmt(self):
        print(self.types[self.t_index], self.current_token)
        parent = self.tree()
        self.match('write')
        child = self.exp()
        self.edge(parent, child)
        return parent
        



    def exp(self):
        temp = self.simpleExp()
        if self.is_comparisonOp():
            print(self.types[self.t_index], self.current_token)
            parent = self.tree()
            self.match(self.current_token)
            leftChild = temp
            rightChild = self.simpleExp()
            self.edge(parent, leftChild, rightChild)
            temp = parent
        return temp
        
    def connectHorizontal(self, firstNode, secondNode, color='black'):
        self.graph.subgraph(nbunch=[firstNode,secondNode],rank= 'same')
        self.graph.add_edge(firstNode,secondNode, color=color)
    
    def tree(self, label=''):
        if not label:
            label = self.current_token
        if label.__contains__('READ') or self.types[self.t_index] in self.nonTerminals:
            self.graph.add_node(self.id, label=label, shape='rectangle')
        else:
            self.graph.add_node(self.id, label=label)
        temp = self.graph.get_node(self.id)
        self.id += 1
        return temp

    def edge(self, parent, left, right=None):
        self.graph.add_edge(parent, left)
        if not right is None:
            self.graph.add_edge(parent, right)

    def match(self, expectedToken):
        if(self.current_token == expectedToken):
            self.updateCurrentToken()
        else:
            raise('Matching Error')

    def updateCurrentToken(self):
        self.t_index += 1
        if(self.t_index < len(self.tokens)):
            self.current_token = self.tokens[self.t_index]

    def is_identifier(self):
        return True if self.types[self.t_index] == 'IDENTIFIER' else  False
    
    def is_addOp(self):
        return True if self.current_token == '+' or self.current_token == '-' else  False
        print(self.current_token)
    def is_mulOp(self):
        return True if self.current_token == '*' or self.current_token == '/' else  False
    def is_comparisonOp(self):
        return True if self.current_token == '<' or self.current_token == '=' or self.current_token == '>' else  False
    def is_semi_column(self):
        return True if self.current_token == ';' else False    