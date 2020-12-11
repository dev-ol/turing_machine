from turing_machine import TuringMachine

def main():

    w_hash_w = TuringMachine(
     {
         ('q0', '#'): ('End', '#', 'R'),
         ('End', ''): ('qa', '', 'R'),

         ('q0', '0'): ('FindDelimiter0', 'X', 'R'),
         ('FindDelimiter0', '#'): ('Check0', '#', 'R'),
         ('Check0', '0'): ('FindLeftmost', 'X', 'L'),

         ('q0', '1'): ('FindDelimiter1', 'X', 'R'),
         ('FindDelimiter1', '#'): ('Check1', '#', 'R'),
         ('Check1', '1'): ('FindLeftmost', 'X', 'L'),

         ('FindLeftmost', '0'): ('FindLeftmost', '0', 'L'),
         ('FindLeftmost', '1'): ('FindLeftmost', '1', 'L'),
         ('FindLeftmost', 'X'): ('FindLeftmost', 'X', 'L'),
         ('FindLeftmost', '#'): ('FindLeftmost', '#', 'L'),
         ('FindLeftmost', ''): ('FindNext', '', 'R'),

         ('FindNext', 'X'): ('FindNext', 'X', 'R'),
         ('FindNext', '0'): ('FindDelimiter0', 'X', 'R'),
         ('FindNext', '1'): ('FindDelimiter1', 'X', 'R'),
         ('FindNext', '#'): ('End', '#', 'R'),

         ('FindDelimiter0', '0'): ('FindDelimiter0', '0', 'R'),
         ('FindDelimiter0', '1'): ('FindDelimiter0', '1', 'R'),
         ('FindDelimiter1', '0'): ('FindDelimiter1', '0', 'R'),
         ('FindDelimiter1', '1'): ('FindDelimiter1', '1', 'R'),

         ('Check0', 'X'): ('Check0', 'X', 'R'),
         ('Check1', 'X'): ('Check1', 'X', 'R'),

        ('End', 'X'): ('End', 'X', 'R'),
     }
 )
    
    user_input = str(input())


    finish = False


    execution = w_hash_w.run(user_input)

    while finish != True :
        context = next(execution)
       # print(context[0])
        info =context[1]
        print("state : {0}".format(info["state"]))

        if(context[0] == "Reject" or context[0] == "Accept" ):
            finish = True

    print("\n***** Results *****")
    print("w = {0} ({1})".format(user_input,context[0] ))
    print("state : {0}".format(info["state"]))
    return 0






main()