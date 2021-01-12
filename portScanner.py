import socket 
import argparse

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

parser = argparse.ArgumentParser(description='Port scanner')
parser.add_argument('-s', type= str, help= 'The server you want to scan the ports in it')

args = parser.parse_args()
my_scan = args.s

def port_scan(port):                     #The function that try to conncect
    try:
        sock.connect((my_scan, port))
        return True 
    except:
        return False
        
j = 0

for i in range (1, 65535):               #The range of the scan you wish 
        if port_scan(i):                 # if the port was open
            print ('Port', i, 'is open')
            j = j + 1	                  #increase index number of open ports
            
print('============================')

if j == 0:      
    print ('The scan is finished NO ports are open')
else:
    print('The scan is finished', j, 'ports are open')

