# bee_manager
This is a simple script for deploy, initialization, monitoring multiple bee nodes.

## Usage
### Create nodes:
Command:  
`python manager.py <amount>`  
For example, this creates configuration file of ten nodes:  
`python manager.py 10`  
Nodes will be named in this format: node_0, node_1, node_2, ......, node_9  
The api port of each node will be: 30000, 30001, 30002, ......, 30009  
### Initialize node:
Command:  
`python manager.py init`  
This will create two file: `address_eth.txt` and `address_bzz.txt` in the script directory, the number of BZZ and ETH requirements for each node initialization is recorded.  
You can go to this website: https://bulksender.app/ to batch transfer.  
### Start
When everything have done, you can start your nodes with this command:  
`python manager.py start`  
This will start all the nodes and show a monitor for you.  
It looks like this:  
![image](https://user-images.githubusercontent.com/61218809/121532839-4f260780-ca32-11eb-843b-22306c16ba2e.png)
### Configuration
You can specify the directory address of the node in config,yaml.  
For example:  
```
path : /home/analogknight/bee_nodes/
```  
If you want to specify multiple directories:
```
path :
  - /media/analogknight/Data1/bee_nodes/
  - /media/analogknight/Data2/bee_nodes/
  - /media/analogknight/Data3/bee_nodes/
  - /media/analogknight/Data4/bee_nodes/
```  
The first directory will be used to create nodes, which you may need to move manually.  
