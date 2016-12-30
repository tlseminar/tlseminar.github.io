###
### tm.py - super simple Turing machine simulator
###

from collections import namedtuple

TuringMachine = namedtuple('TuringMachine', ['rules', 'q_0', 'q_accepting'])

def simulate(tm, starttape):
    ### Simulates tm = (S, T, q_0, q_accept) running on starttape.
    ### Returns True if tm ends in an accepting state, False if it 
    ### terminates in another state.

    tape = starttape
    headpos = 0
    currentstate = tm.q_0
    step = 0

    while True:
        step += 1
        print ("Step " + str(step) + ", State: " + str(currentstate) + "\t " + ''.join(tape[:headpos]) + "*" 
               + ''.join(tape[headpos:]))

        readsym = tape[headpos]
        if (currentstate, readsym) in tm.rules:
            (nextstate, writesym, dir) = tm.rules[(currentstate, readsym)]
            tape[headpos] = writesym
            currentstate = nextstate
        else:
            print("Warning: no rule for " + str(currentstate) + ", " + str(readsym) + " [Halting]")
            dir = 'Halt'
            return False

        if dir == 'L':
            headpos -= 1
            if headpos < 0: 
                headpos = 0 # don't fall off left end of tape
        elif dir == 'R':
            headpos += 1
            if len(tape) <= headpos:
                tape.append('_') # blank symbol
        else:
            assert dir == 'Halt'
            return currentstate in tm.q_accepting
            
def xor_machine(input):
    tm = TuringMachine(rules = { ('S', '0'): ('R0', '-', 'R'),
                                 ('S', '1'): ('R1', '-', 'R'),
                                 ('S', '+'): ('C', '+', 'R'),
                                 ('R0', '0'): ('R0', '0', 'R'),
                                 ('R0', '1'): ('R0', '1', 'R'),
                                 ('R1', '0'): ('R1', '0', 'R'),
                                 ('R1', '1'): ('R1', '1', 'R'),
                                 ('R0', '+'): ('X0', '+', 'R'),
                                 ('R1', '+'): ('X1', '+', 'R'),
                                 ('X0', 'X'): ('X0', 'X', 'R'),
                                 ('X1', 'X'): ('X1', 'X', 'R'),
                                 ('X0', 'X'): ('X0', 'X', 'R'),
                                 ('X0', '0'): ('Y0', 'X', 'R'),
                                 ('X0', '1'): ('Y1', 'X', 'R'),
                                 ('X1', '0'): ('Y1', 'X', 'R'),
                                 ('X1', '1'): ('Y0', 'X', 'R'),
                                 ('Y0', '0'): ('Y0', '0', 'R'),
                                 ('Y0', '1'): ('Y0', '1', 'R'),
                                 ('Y1', '0'): ('Y1', '0', 'R'),
                                 ('Y1', '1'): ('Y1', '1', 'R'),
                                 ('Y0', '='): ('Z0', '=', 'R'),
                                 ('Y1', '='): ('Z1', '=', 'R'),
                                 ('Z0', 'X'): ('Z0', 'X', 'R'),
                                 ('Z1', 'X'): ('Z1', 'X', 'R'),
                                 ('Z0', '0'): ('B', 'X', 'L'),  # 'B' - move all the way back to the '-'
                                 ('Z1', '1'): ('B', 'X', 'L'),
                                 ('B', '0'): ('B', '0', 'L'),
                                 ('B', '1'): ('B', '1', 'L'),
                                 ('B', '+'): ('B', '+', 'L'),
                                 ('B', 'X'): ('B', 'X', 'L'),
                                 ('B', '='): ('B', '=', 'L'),
                                 ('B', '-'): ('S', '-', 'R'),
                                 ('C', 'X'): ('C', 'X', 'R'), # 'C' - check everything is crossed off
                                 ('C', '='): ('C', '=', 'R'), 
                                 ('C', '$'): ('Accept', '$', 'Halt') },
                       q_0 = 'S',
                       q_accepting = { 'Accept' })
    
    return simulate(tm, input)

if __name__ == "__main__":
    assert(xor_machine(list("0+1=1$")))
    assert(not(xor_machine(list("0+1=10$"))))
    assert(xor_machine(list("00+10=10$")))
    assert(not(xor_machine(list("0101010+10101010=11111111$"))))
    print("All assertions passed!")

    
