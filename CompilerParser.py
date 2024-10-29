from ParseTree import *

class CompilerParser :

    def __init__(self,tokens):
        """
        Constructor for the CompilerParser
        @param tokens A list of tokens to be parsed
        """
        self.tokens = tokens
        self.current_token = tokens[0]
        self.tokens_index = 0
        pass
    

    def compileProgram(self):
        """
        Generates a parse tree for a single program
        @return a ParseTree that represents the program
        """
        # init tree if keyword is class
        if not self.have("keyword", "class"): 
            raise ParseException("the program doesnot begin with a class")
        tree = ParseTree("class", "")
        tree.addChild(ParseTree("keyword", "class"))
        self.next()

        # identifier
        if not self.current_token.getType() == "identifier": raise ParseException("expected Identifier")
        tree.addChild(ParseTree("identifier", self.current_token.getValue()))
        self.next()

        # {
        if not self.have("symbol", "{"): raise ParseException("expected {")
        tree.addChild(ParseTree("symbol", "{"))
        self.next()

        # class variables
        while not self.have("symbol", "}"):
            if self.current_token.getValue() in ["static" , "field"]:
                tree.addChild(self.compileClassVarDec())
                self.next()

            elif self.current_token.getValue() in ["constructor" , "function", "method"]:
                tree.addChild(self.compileSubroutine())
                self.next()
            
            else:
                raise ParseException("current token is not a variable decleration or a subroutine")
        
        # }
        if not self.have("symbol", "}"): raise ParseException("expected }")
        tree.addChild(ParseTree("symbol", "}"))
        self.next()

        return tree
    
    
    def compileClass(self):
        """
        Generates a parse tree for a single class
        @return a ParseTree that represents a class
        """
        # init tree if keyword is class
        if not self.have("keyword", "class"): raise ParseException("Expected Keyword - class")
        tree = ParseTree("class", "")
        tree.addChild(ParseTree("keyword", "class"))
        self.next()

        # identifier
        if not self.current_token.getType() == "identifier": raise ParseException("expected Identifier")
        tree.addChild(ParseTree("identifier", self.current_token.getValue()))
        self.next()

        # {
        if not self.have("symbol", "{"): raise ParseException("expected {")
        tree.addChild(ParseTree("symbol", "{"))
        self.next()

        # class variables
        while not self.have("symbol", "}"):
            if self.current_token.getValue() in ["static" , "field"]:
                tree.addChild(self.compileClassVarDec())
                self.next()

            elif self.current_token.getValue() in ["constructor" , "function", "method"]:
                tree.addChild(self.compileSubroutine())
                self.next()
            
            else:
                raise ParseException("current token is not a variable decleration or a subroutine")
        
        # }
        if not self.have("symbol", "}"): raise ParseException("expected }")
        tree.addChild(ParseTree("symbol", "}"))
        self.next()

        return tree
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """

        tree = ParseTree("classVarDec","")
        if not (self.have("keyword", "static") or self.have("keyword", "field")): raise ParseException("expected keyword to be field or static")
    
        # static_or_field = self.current_token.getType()

        tree.addChild(ParseTree(self.current_token.getType(), self.current_token.getValue()))
        self.next()

        # must be primitive or class data type
        if self.current_token.getType() != "identifier" and not (self.current_token.getType() == "keyword" and self.current_token.getValue() in ["int", "char", "boolean"]): raise ParseException("Expected token type to be an int, char, boolean or identifier")
        # variable_token_type = self.current_token.getType()
        # variable_token_value = self.current_token.getValue()
        tree.addChild(ParseTree(self.current_token.getType(), self.current_token.getValue()))
        self.next()
        
        #variable name
        if self.current_token.getType() != "identifier": raise ParseException("Expected token type to be an identifier")
        tree.addChild(ParseTree("identifier", self.current_token.getValue()))
        self.next()

        # more name
        while self.have("symbol", ","):
            

            #seperate trees
                # self.next()
                # if self.current_token.getType() != "identifier": raise ParseException("Expected token type to be an identifier")
                # tree.addChild(ParseTree("keyword", static_or_field))
                # tree.addChild(ParseTree(variable_token_type, variable_token_value))
                # tree.addChild(ParseTree("identifier", self.current_token.getValue()))
                # self.next()

            # , seperated
            tree.addChild(ParseTree("symbol", ","))
            self.next()
            if self.current_token.getType() != "identifier": raise ParseException("Expected token type to be an identifier")
            tree.addChild(ParseTree("identifier", self.current_token.getValue()))
            self.next()
        

        #;
        if not self.have("symbol", ";"): return ParseException("Expected ;")
        tree.addChild(ParseTree("symbol", ";"))

        return tree
    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        return None 
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        return None 
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        return None 
    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """
        return None 
    

    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """
        return None 
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        return None 

    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        return None 


    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        return None 


    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        return None 


    def next(self):
        """
        Advance to the next token
        """
        if self.tokens_index >= len(self.tokens) - 1: return 
        self.tokens_index += 1
        self.current_token =  self.tokens[self.tokens_index]
        return


    def current(self):
        """
        Return the current token
        @return the token
        """
        return self.current_token

    def have(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        @return True if a match, False otherwise
        """

        return (self.current_token.getType() == expectedType and self.current_token.getValue() == expectedValue)


    def mustBe(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        If so, advance to the next token, returning the current token, otherwise throw/raise a ParseException.
        @return token that was current prior to advancing.
        """
        cur = self.current_token
        if self.have(expectedType, expectedValue): self.next(); return cur

        raise ParseException('current token doesn\'t match expected type and/or value')
    

if __name__ == "__main__":


    """ 
    Tokens for:
        class MyClass {
        
        }
    """
    tokens = []
    tokens.append(Token("keyword","class"))
    tokens.append(Token("identifier","MyClass"))
    tokens.append(Token("symbol","{"))
    tokens.append(Token("symbol","}"))

    parser = CompilerParser(tokens)
    try:
        result = parser.compileProgram()
        print(result)
    except ParseException:
        print("Error Parsing!")
