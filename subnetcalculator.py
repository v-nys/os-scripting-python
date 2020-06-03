import sys
#Parameter definiëren
Fout_invoering_message = "IP-adres en/of subnetmasker is ongeldig."

#Stap 1 + Stap 2
##IPv4-hostadres opvragen
##subnetmasker opvragen
 
def ask_for_number_sequence(message):
    antwoord = input(message)
    return [int(elem) for elem in antwoord.split(".")]

  
#Stap 3 
##ip-adres geldigheid controleren

def is_valid_ip_address(numberlist):
    block =[(print(Fout_invoering_message), sys.exit(0)) for elem in numberlist if elem > 255 or elem < 0 or len(numberlist) != 4 ]
    return block


##subnetmasker geldigheid controleren

def is_valid_netmask(numberlist):
###Exit als numberlist niet exact 4 elementen bevat
    
    if len(numberlist) !=4 :
        print(Fout_invoering_message)
        sys.exit(0)
 
#checking_ones = True
    else:
###binaire voorstelling met 8 symbolen van elke byte bepalen en allemaal aan elkaar plakken
        binary_netmask = ""
            
        for elem in numberlist:
            if elem > 255 or elem < 0:
                print(Fout_invoering_message)
                sys.exit(0)
            block_binaire = f"{int(elem):08b}"
            binary_netmask = binary_netmask + block_binaire

###checking_ones controleren
        checking_ones = True

        for symbol in binary_netmask :
            if  checking_ones == True and symbol == "0":
                checking_ones = False
            elif symbol == "1" and checking_ones == False:
                print(Fout_invoering_message)
                sys.exit(0)        
    return binary_netmask
    


#Stap 4
#aantal 1-bits tellen

def one_bits_in_netmask(binary_netmask):
    binary_netmask_l=""
    counter = 0
    
    for elem in binary_netmask:
        block_binaire = str(f"{int(elem):08b}")
        binary_netmask_l = binary_netmask_l + block_binaire
    for elem in binary_netmask_l:
        if elem == "1":           
            counter +=1 

    return counter
    

#Stap 5 
#adres van het subnet berekenen

def apply_network_mask(host_address,netmask):
    binary_host = ""
    binary_netmask = ""
    i = 0
    sub_str = ""

    for block in host_address:
        block_binaire = f"{int(block):08b}"
        binary_host = binary_host + block_binaire

    
    for block in netmask:
        block_binaire = f"{int(block):08b}"
        binary_netmask = binary_netmask + block_binaire


    while i < 32:
        if binary_host[i] == "1" and binary_netmask[i] == "1":
            sub_str = sub_str + "1"
        else:
            sub_str = sub_str + "0"
        i +=1

    networkID = []
    networkID_str= int(sub_str[0:8],2), int(sub_str[8:16],2) , int(sub_str[16:24],2) , int(sub_str[24:32],2)
    networkID = [int (elem) for elem in networkID_str]    
    return networkID
    

#Stap 6 
#wildcardmasker berekenen

def netmask_to_wilcard_mask(subnet_masker):     
    wildcard_mask = []
    for elem in subnet_masker:
        wildcard_bit = ""
        for bit in f"{elem:08b}":
            if bit == "0":
                wildcard_bit += "1"
            else:
                wildcard_bit += "0"
        wildcard_mask.append(int(wildcard_bit,2))        
    return wildcard_mask


#Stap 7 
#broadcastadres berekenen

def get_broadcast_address(network_address,wildcard_mask):
    
    binary_network = ""
    binary_wildcard = ""
    i = 0
    sub_str = ""
    
    for block in network_address:
        block_binaire = f"{int(block):08b}"
        binary_network = binary_network + block_binaire
    
    for block in wildcard_mask:
        block_binaire = f"{int(block):08b}"
        binary_wildcard = binary_wildcard + block_binaire
     

    while i < 32:
        if binary_network[i] == "1" or binary_wildcard[i] == "1":
            sub_str = sub_str + "1"
        else:
            sub_str = sub_str + "0"
        i +=1

    broadcast = [] 
    broadcast_str= int(sub_str[0:8],2), int(sub_str[8:16],2) , int(sub_str[16:24],2) , int(sub_str[24:32],2)
    broadcast = [int (elem) for elem in broadcast_str]
    return broadcast


#Stap 8
#maximaal aantal hosts berekenen

def prefix_length_to_max_hosts(aantal_1_bits):
    aantal_host = 2** (32 - aantal_1_bits) - 2
    return aantal_host
    

if __name__ == '__main__':
    # ++++++++++++++++++++++
    # ++++++++++++++++++++++
    
    #1+2
    ##IPv4-hostadres opvragen
    ##subnetmasker opvragen
    host_address = ask_for_number_sequence("Wat is het IP-adres?\n")
    subnet_mask = ask_for_number_sequence("Wat is het subnetmasker?\n")
    
    #3
    ##ip-adres geldigheid controleren
    ##subnetmasker geldigheid controleren
    is_valid_ip_address(host_address)
    is_valid_netmask(subnet_mask)
    if len(subnet_mask) ==4:
        print("IP-adres en subnetmasker zijn geldig.")
        
    #4
    #aantal 1-bits tellen
    aantal_1_bits = one_bits_in_netmask(subnet_mask)
    print("De lengte van het subnetmasker is " + str(aantal_1_bits) + ".")
    
    #5
    #adres van het subnet berekenen
    netwerk_address = apply_network_mask(host_address,subnet_mask)
    print("Het adres van het subnet is " + ('.'.join([str(i) for i in (netwerk_address)])) +".")
    
    #6
    #wildcardmasker berekenen
    wildcard_mask = netmask_to_wilcard_mask(subnet_mask)
    print("Het wildcardmasker is " + ('.'.join([str(i) for i in (wildcard_mask)]))+".")
    
    #7
    #broadcastadres berekenen
    broadcast_address= get_broadcast_address(netwerk_address,wildcard_mask)
    print("Het broadcastadres is " + ('.'.join([str(i) for i in (broadcast_address)]))+".")
    
    #8
    #maximaal aantal hosts berekenen
    max_anntalhosts = prefix_length_to_max_hosts(aantal_1_bits)
    print("Het maximaal aantal hosts op dit subnet is " + (str(max_anntalhosts))+".")
    
