import sys
import Tokenizer2

class Analyzer:
    def __init__(self, file):
        self.x = Tokenizer2(file)
        self.parse(file)

    def parse(self):    
        type = ''
        token = ''

        # write to .xml file
        sys.stdout = open(input.split('.')[0] + 'T.xml', 'wt')
    
        # use Tokenizer functions to print out xml line by line
        print('<tokens>')
        while Tokenizer2.hasMoreTokens():
            type = Tokenizer2.tokenType()
            token = Tokenizer2.token()
            print('<' + type + '> ' + token + ' </' + type + '>')
            Tokenizer2.advance()
        print('</tokens>')

def main():
    input = sys.argv[1]
    file = open(input, 'r') 
    
    testing = Analyzer(file)

if __name__ == "__main__":
    main()

    