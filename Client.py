#from socket import *
import time

#make this an add template
#viasat = { 'name': "www.viasat.com", 'type':"A", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
RR = []
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
    print("\nA \"%s\" record for hostname \"%s\" was not found in the Client's RR table." %(typeUser, nameUser))
    return -1



#serverName = 'localhost'
#serverPort = 12000
#clientSocket = socket(AF_INET, SOCK_DGRAM)

print ('The client is ready to receive')
    
#Does client need to be in while loop -- until exit maybe?
while(1):
    #message = input('Input lowercase sentence:')
    print()
    #outgoing socket messages (5 of them):
    messageName = input("Enter search name? ")
    messageType = input("Enter search type? ")
    print()
    print("You requested search for =>hostname: %s =>type: %s " %( messageName, messageType))

    #check local RR 
    current = checkTableForValue(messageName, messageType)
    if(current == -1): #not in the table
        print("Checking local DNS server...")
        #clientSocket.sendto(message.encode(),(serverName, serverPort))
        #modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        #serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        returnMessageValue = "2.3.3.3" #add the returned value from DNS here
        #add to table
        addToRR = { 'name': messageName, 'type':messageType, 'value':returnMessageValue, 'static':0, 'TTL':60, 'timer':time.time()}
        RR.append(addToRR)
        checkTableForValue(messageName, messageType)
    else: #in the table so return
        print("Returning: %s" %(RR[current]['value'])) 
    print("********************************************************")
        

    #print (modifiedMessage.decode())


#clientSocket.close()