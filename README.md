# PortHammer
A simple port scanning tool written in python3. This tool is made for beginners and it's really easy to use.

# Installation

````bash
git clone https://github.com/zerodayrat/PortHammer.git
````

````bash
cd PortHammer
````

````bash
python3 porthammer.py -p1 <starting port> -p2 <ending port> -t <target ip address>
````  

# Help Menu

usage: `porthammer.py [-h] -p1 PORT1 -p2 PORT2 -t TARGET`

````text
optional arguments:
  -h, --help                     show this help message and exit
  -p1 PORT1, --port1 PORT1       Enter starting Port
  -p2 PORT2, --port2 PORT2       Enter Ending Port
  -t TARGET, --target TARGET     Enter Target IP
````

# Example

To scan first 1000 ports of ip address 192.168.42.20 :
  
````bash
python3 porthammer.py -p1 1 -p2 1000 -t 192.168.42.20 
````

To scan from port 50 to 100 

````bash
python3 porthammer.py -p1 50 -p2 100 -t 192.168.42.20

````
