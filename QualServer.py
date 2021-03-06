import time
#from socket import *

qualcom = { 'name': "www.qualcomm.com", 'type':"A", 'value':'104.86.224.205', 'static':1, 'TTL':None, 'timer':None}
qtiack12 = { 'name': "qtiack12.qti.qualcomm.com", 'type':"A", 'value':'129.46.100.21', 'static':1, 'TTL':None, 'timer':None}
RR = [qualcom, qtiack12]
def checkTimer():
    i = 0
    for x in RR:
        if((RR[i]['timer'])):
            current = int(time.time()-RR[i]['timer'])
            RR[i]['TTL']=RR[i]['TTL']-current
            RR[i]['timer']=time.time()
            if(RR[i]['TTL']<1):
                RR.remove(x)
        i +=1

def printTable():
    i = 0
    print()
    print("---------------------------------------------------------------------------")
    print("%-5s %-20s %-10s %-15s %-15s %-15s" %("No.", "Name", "Type", "Value", "Static", "TTL"))
    print("---------------------------------------------------------------------------")
    checkTimer()
    for x in RR:
        print("%-5d %-20s %-10s %-15s %-15s" %(i+1, RR[i]['name'], RR[i]['type'], RR[i]['value'], RR[i]['static']), end=" ")
        if(RR[i]['TTL']):
            print(RR[i]['TTL'])
        i +=1
        print()
    print("---------------------------------------------------------------------------")


def checkTableForValue(nameUser, typeUser):
    printTable()
    i = 0
    for x in RR:
        if(RR[i]['name']==nameUser):
            if(RR[i]['type']==typeUser):
                print("\nFound %s for %s and its value is %s\n" %(RR[i]['name'], RR[i]['type'], RR[i]['value']))
                return i
    i += 1
    print("\nA \"%s\" record for hostname \"%s\" was not found in the Loacl DNS server's RR table." %(typeUser, nameUser))
    print("...Unable to answer at this time\n")
    return -1

#from socket import *
#do we have to change these?
serverPort = 12000


#serverSocket = socket(AF_INET, SOCK_DGRAM)
#serverSocket.bind(('', serverPort))
print ('The server at Qualcomm is ready to receive')


while 1:

    #message, clientAddress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode()
    print()
    messageName = input("Name? ")
    messageType = input("Type? ")
    print()
    #print("Local Viasat server: The client with IP address %s sent a(n) %s request for hostname %s" %(clientAddress, messageType, messageName))
    print("Qualcomm server: The client with IP address %s sent a request for:" %("FILL_IN"))
    print("      hostname=>%s" %(messageName)) 
    print("      type=>%s" %(messageType))
    print()

    #check local RR
    current = checkTableForValue(messageName, messageType)
    print("********************************************")
    if(current == -1): #not in the table
        print("Return message: not in RR table")
    else: #in the table so return
        print("Returning: %s" %(RR[current]['value'])) 
        #serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("********************************************")
        

    
