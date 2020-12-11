from turing_machine import TuringMachine

def main():

    custom_TM = TuringMachine(
     {
         ('q0', '#'): ('End', '#', 'R'),
         ('End', ''): ('qa', '', 'R'),

         ('q0', '0'): ('q1', 'X', 'R'),
         ('q1', '#'): ('Check0', '#', 'R'),
         ('Check0', '0'): ('FindLeftmost', 'X', 'L'),

         ('q0', '1'): ('q2', 'X', 'R'),
         ('q2', '#'): ('Check1', '#', 'R'),
         ('Check1', '1'): ('FindLeftmost', 'X', 'L'),

         ('FindLeftmost', '0'): ('FindLeftmost', '0', 'L'),
         ('FindLeftmost', '1'): ('FindLeftmost', '1', 'L'),
         ('FindLeftmost', 'X'): ('FindLeftmost', 'X', 'L'),
         ('FindLeftmost', '#'): ('FindLeftmost', '#', 'L'),
         ('FindLeftmost', ''): ('FindNext', '', 'R'),

         ('FindNext', 'X'): ('FindNext', 'X', 'R'),
         ('FindNext', '0'): ('q1', 'X', 'R'),
         ('FindNext', '1'): ('q2', 'X', 'R'),
         ('FindNext', '#'): ('End', '#', 'R'),

         ('q1', '0'): ('q1', '0', 'R'),
         ('q1', '1'): ('q1', '1', 'R'),
         ('q2', '0'): ('q2', '0', 'R'),
         ('q2', '1'): ('q2', '1', 'R'),

         ('Check0', 'X'): ('Check0', 'X', 'R'),
         ('Check1', 'X'): ('Check1', 'X', 'R'),

        ('End', 'X'): ('End', 'X', 'R'),
     }
 )
    
    user_input = str(input("Enter a word : "))


    finish = False # use to check if the machine has reached a final state


    execution = custom_TM.run(user_input)

    while finish != True :
        context = next(execution)
        info =context[1]
        print("state : {0}".format(info["state"]))

        if(context[0] == "Reject" or context[0] == "Accept" ):
            finish = True

    print("\n***** Results *****")
    print("w = {0} ({1})".format(user_input,context[0] ))
    print("state : {0}".format(info["state"]))
    return 0






main()