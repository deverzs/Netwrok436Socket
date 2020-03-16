import time


viasat = { 'name': "www.viasat.com", 'type':"A", 'value':'122.222.222', 'static':1, 'TTL':None, 'timer':None}
test = { 'name':"test", 'type': "A", 'static': 0,'value':"222.222.222", 'TTL':60, 'timer':time.time() }
RR = [viasat, test]
def printTable():
    i = 0
    print("------------------------------------------------------------------")
    print("%-15s %-10s %-15s %-15s %-15s" %("Name", "Type", "Value", "Static", "TTL"))
    print("------------------------------------------------------------------")
    for x in RR:
        if((RR[i]['timer'])):
            current = int(time.time()-RR[i]['timer'])
            RR[i]['TTL']=RR[i]['TTL']-current
            RR[i]['timer']=time.time()
            if(RR[i]['TTL']<1):
                RR.remove(x)
        i +=1

    i = 0
    for x in RR:
        print("%-15s %-10s %-15s %-15s" %(RR[i]['name'], RR[i]['type'], RR[i]['value'], RR[i]['static']), end=" ")
        if(RR[i]['TTL']):
            print(RR[i]['TTL'])
        i +=1
        print()
    print("------------------------------------------------------------------")




#from socket import *
#do we have to change these?
serverPort = 12000


#serverSocket = socket(AF_INET, SOCK_DGRAM)
#serverSocket.bind(('', serverPort))
print ('The server at Viasat is ready to receive')


while 1:

    #MESSAGE FROM LOCAL SERVER - A SEARCH
    #message, clientAddress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode()
    messageName = input("Name? ")
    messageType = input("Type? ")

    #check local RR

    printTable()

    #if not found locally, send  

    #serverSocket.sendto(modifiedMessage.encode(), clientAddress)


    
