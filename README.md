# Data-Packet-Flow-Debuging


### What is ip address and it's other components 


![ipaddress](https://user-images.githubusercontent.com/60421249/152775019-f79dc90d-d795-433c-847f-6212d2a80818.png)


### Data Packet Flow Example

Before starting the workflows lets learn more about some inco-terms

### What is Ingress 

Data ingress refers to traffic that comes from outside an organization’s network and is transferred into it. It is unsolicited traffic that gets sent from the internet to a private network. The traffic does not come in response to a request made from inside an organization’s network. 

### What is Egress

A common egress meaning is the process of data leaving a network and transferring to an external location. Data egress is a form of network activity but poses a threat to organizations if it exposes sensitive data to unauthorized or unintended recipients.

Egress happens whenever data leaves an organization’s network, be it via email messages, as uploads to the cloud or websites, as a file transferred onto removable media like Universal Serial Bus (USB) drives and external hard drives, or through File Transfer Protocol (FTP) or Hypertext Transfer Protocol (HTTP) transfers.

![800px-PacketFlowDiagram_v6_a svg](https://user-images.githubusercontent.com/60421249/152416474-89dc272e-44bd-403b-9e1d-43a42ea0b5d0.png)


### Routing Table:

A routing table is a set of rules, often viewed in table format, that is used to determine where data packets traveling over an Internet Protocol (IP) network will be directed. All IP-enabled devices, including routers and switches, use routing tables. See below a Routing Table:

![route-table](https://user-images.githubusercontent.com/60421249/152777370-cde0f85c-008d-4468-a979-53be0eca5e1b.png)

 
### Entries of an IP Routing Table:
A routing table contains the information necessary to forward a packet along the best path toward its destination. Each packet contains information about its origin and destination. Routing Table provides the device with instructions for sending the packet to the next hop on its route across the network.

Each entry in the routing table consists of the following entries:

Network ID:
The network ID or destination corresponding to the route.
Subnet Mask:
The mask that is used to match a destination IP address to the network ID.
Next Hop:
The IP address to which the packet is forwarded
Outgoing Interface:
Outgoing interface the packet should go out to reach the destination network.
Metric:
A common use of the metric is to indicate the minimum number of hops (routers crossed) to the network ID.

We will use docker for this lab

### What is tcp dump

Tcpdump is a data-network packet analyzer computer program that runs under a command line interface. It allows the user to display TCP/IP and other packets being transmitted or received over a network to which the computer is attached.

### What is docker ?

Docker is a containerization tools, where we can development different types of tools and software in a isolated environment.
Run this command:
```
docker pull nginx
```
Then:
```
docker run nginx
```
It will run the nginx container.Open a new tab and open the container using :
```
docker exec -it nginx sh
```
