import sys
from antlr4 import *
from oosLexer import oosLexer
from oosParser import oosParser
from oosMyListener import oosMyListener

def oos_compile(file_oos):
    # Dimiourgise to onoma tou arxeiou exodou apo to onoma tou arxeiou eisodou
    output_file = file_oos.replace('.oos', '.c')
    
    # Diavase to arxeio .oos
    input_stream = FileStream(file_oos)
    
    # Dimiourgise ton lexer gia na diaxorisei to keimeno se tokens
    lexer = oosLexer(input_stream)
    
    # Dimiourgise to stream apo tokens
    stream = CommonTokenStream(lexer)
    
    # Dimiourgise ton parser gia na analysei ta tokens
    parser = oosParser(stream)
    
    # Ktixtise to syntaktiko dentro (parse tree)
    tree = parser.startRule()
    
    # Dimiourgise ton listener me to onoma tou arxeiou exodou
    oss_listener = oosMyListener(output_filename=output_file)
    
    # Dimiourgise ton walker gia na diatrexei to dentro
    walker = ParseTreeWalker()
    
    # Diatrexe to dentro kai kalesei tous listeners
    walker.walk(oss_listener, tree)
    
    # Pare ton kodika C pou dimiourgithike
    source = oss_listener.get_oos_compiled()
    
    # Dimiourgise kai to arxeio me ti domi tou pinaka symvolon (.sym)
    oss_listener.get_symb_structure() 
    
    # Ektypwse ton kodika C
    print(source)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments for OSS compiler")
    else:
        oos_compile(sys.argv[1])