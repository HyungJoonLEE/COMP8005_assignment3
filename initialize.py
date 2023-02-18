import ipaddress
import re

import port_scanner as input_1
import syn_flood_attack as input_2


def initialize_program():
    user_input = get_user_input_for_target()
    while 1:
        if user_input['dst_ip'] and user_input['dst_port_start'] and user_input['dst_port_end'] is not None:
            print(f"\n\n==========[ TARGET ]==========\n"
                  f" Destination ip = {user_input['dst_ip']}\n"
                  f" Destination port = {user_input['dst_port_start']} - {user_input['dst_port_end']}\n"
                  f"==========[ OPTION ]==========")

            number = input("1. port scanner\n"
                           "2. SYN flood attack\n"
                           "3. Christmas Tree attack\n"
                           "4. Perform another attack\n"
                           "5. Reset the [ TARGET ]\n"
                           "==============================\n"
                           "Choose the option to run the program: ")

            if number < "1" or number > "5":
                print("Number out of range")
            else:
                if number == "1":
                    input_1.port_scanner(user_input)
                if number == "2":
                    thread_num = int(input("Number of Thread to use: "))
                    target_port = int(input("Target Port: "))
                    num_thread = []
                    for SF_attack in range(thread_num):
                        input_2.SynFloodAttack(user_input['dst_ip'], target_port, thread_num)
                        num_thread.append(SF_attack)
                        SF_attack.start()
                # if number == "3":
                #     program_type.christmas_tree_attack()
                # if number == "4":
                #     program_type.another_attack()
                if number == "5":
                    user_input = get_user_input_for_target()



def get_user_input_for_target():
    user_input = {'dst_ip': None, 'dst_port_start': None, 'dst_port_end': None}
    port_regex = re.compile("([0-9]+){1,5}-?(([0-9]+){1,5})?")
    ip_regex1 = re.compile("^\d")
    ip_regex2 = re.compile("^www\.")

    while 1:
        print("\n\n* [SETTING TARGET] *")
        ip_address_input = input("Type Destination IP Address or Domain Address : ")
        try:
            ip_regex1_valid = ip_regex1.search(ip_address_input.replace(" ", ""))
            ip_regex2_valid = ip_regex2.search(ip_address_input.replace(" ", ""))
            if ip_regex1_valid:
                ip_address = ipaddress.ip_address(ip_address_input)
                user_input['dst_ip'] = ip_address.compressed
                break
            elif ip_regex2_valid:
                ip_address = ipaddress.ip_address(ip_address_input)
                user_input['dst_ip'] = ip_address.compressed
                break
        except:
            print("This is wrong type or format of IP address")

    while 1:
        port_start = 0
        port_end = 65335
        port_range = input("Type the port range ( ex: 1-65535 ) : ")
        port_range_valid = port_regex.search(port_range.replace(" ", ""))
        if port_range_valid:
            if port_range_valid.group(2) is None:
                port_start = int(port_range_valid.group(1))
                port_end = int(port_range_valid.group(1))
            elif int(port_range_valid.group(1)) < int(port_range_valid.group(2)):
                port_start = int(port_range_valid.group(1))
                port_end = int(port_range_valid.group(2))
            else:
                continue
            user_input['dst_port_start'] = port_start
            user_input['dst_port_end'] = port_end
            return user_input
        else:
            continue


