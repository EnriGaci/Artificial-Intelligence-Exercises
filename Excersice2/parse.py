import Stack

def parse(parseList):
    myStack = Stack.Stack()

    for symbol in parseList:
        if symbol in ['(','{','[']:
            myStack.push(symbol)
        else:
            if symbol == ')' and myStack.pop() != '(':
                return "Not Balanced"
            elif symbol == ']' and myStack.pop() != '[':
                return "Not Balanced"
            elif symbol == '}' and myStack.pop() != '{':
                return "Not Balanced"
    return "Balanced!"

def testParse():
    parseList = ['(','{','}','(',')',')']
    if parse(parseList) != "Balanced!":
        print "Failed Test 1"
    else:
        print "Passed Test 1"

    parseList = ['(','{','}','{','(',')',')']
    if parse(parseList) != "Not Balanced":
        print "Failed Test 2"
    else:
        print "Passed Test 2"

if __name__ == '__main__':
    testParse()