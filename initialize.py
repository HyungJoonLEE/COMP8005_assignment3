import port_scanner as input_1
import syn_flood_attack as input_2


def initialize_program():
    while 1:
        number = input("\n\n\n\n\n==========Assignment3===========\n"
                       "1. port scanner\n"
                       "2. SYN flood attack\n"
                       "3. Christmas Tree attack\n"
                       "4. Perform another attack\n"
                       "Choose the option to run the program: ")

        if number < "1" or number > "4":
            print("Number out of range")
        else:
            if number == "1":
                input_1.port_scanner()
            if number == "2":
                input_2.syn_flood_attack()
            # if number == "3":
            #     program_type.christmas_tree_attack()
            # if number == "4":
            #     program_type.another_attack()


