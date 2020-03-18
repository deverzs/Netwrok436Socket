#from socket import *
import time


resource1 = { 'name': "www.csusm.edu", 'type':"A", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
resource2 = { 'name': "cc.csusm.edu", 'type':"A", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
resource3 = { 'name': "cc1.csusm.edu", 'type':"CNAME", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
resource4 = { 'name': "cc1.csusm.edu", 'type':"A", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
resource5 = { 'name': "my.csusm.edu", 'type':"A", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
resource6 = { 'name': "qualcomm.com", 'type':"NS", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
resource7 = { 'name': "viasat.com", 'type':"NS", 'value':'8.37.96.179', 'static':1, 'TTL':None, 'timer':None}
RR = [resource1, resource2, resource3, resource4, resource5, resource6, resource7]
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
    return -1


#serverPort = 12000
#serverSocket = socket(AF_INET, SOCK_DGRAM)
#serverSocket.bind(('', serverPort))
print ('The Local DNS server is ready to receive')
while 1:
    #message, clientAddress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode().upper()
    print()
    messageName = input("Enter search name? ")
    messageType = input("Enter search type? ")
    print()
    print("Local DNS server: The client with IP address %s sent a request for:" %("FILL_IN"))
    print("      hostname=>%s" %(messageName)) 
    print("      type=>%s" %(messageType))
        
    #check local RR 
    current = checkTableForValue(messageName, messageType)
    if(current == -1): #not in the table

        #strip domain
        splitList = messageName.split(".")
        if(splitList[0]=="www"):
            splitName = splitList[1] + "." + splitList[2]
            splitType = "NS"
        else:
            print("Unable to answer at this time.")
            continue;
        #if viasat, send to viasat
        if(splitList[1]=="viasat"):
            checkTableForValue(messageName, messageType)
            print("Checking Viasat DNS server...")
            #to viasat message with original search values
        #sending to qualcomm
        elif(splitList[1]=="qualcomm"):
            checkTableForValue(messageName, messageType)
            print("Checking Qualcomm DNS server...")
            #to qualcomm message with original search values
        else:
            print("Unable to answer at this time.")
            break;
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

    #serverSocket.sendto(modifiedMessage.encode(), clientAddress)
