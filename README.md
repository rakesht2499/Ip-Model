[![](https://img.shields.io/badge/pypi-v1.1.0-blue.svg)](https://pypi.org/project/ip-model/)
[![License](https://img.shields.io/badge/Licence-Apache--2.0-orange)](https://github.com/rakesht2499/Ip-Model/blob/master/LICENSE/)

# Ip-Model

A Data Structure for efficiently storing, removing and checking all Ipv4 addresses in O(1) time.

## Usage

```python
from ip_model.Ipv4 import Ipv4

blacklist = Ipv4()
```

### To add an IP:

```python
# arg: String
blacklist.add("192.0.0.18")
```

### To remove an IP:

```python
# arg: String
blacklist.remove("192.0.0.18")
```

### To check if an IP is present/not:

```python
# arg: String
# returns: bool
blacklist.is_present("192.0.0.18")
```

### To add CIDR - Ipv4:

```python
# arg: String
blacklist.add_cidr("192.92.53.0/24")
```
*Note: Overlapping CIDR's are accepted. 

### To remove CIDR - Ipv4:

```python
# arg: String
blacklist.remove_cidr("192.92.53.0/24")
```

*Note: Currently the range of IP's will be removed even if it was added as a part of an overlapping entry
The catch here is, the call for how to handle with overlapping CIDR's must be taken by the service using this DS. 
The DataStructure receives the request on what to do with the given data

### Exception Handling

- Throws `TypeError`: passing Invalid Datatype, incorrect number of arguments
- Throws `InvalidIpException`: When an invalid Ip is passed

```python
from ip_model.Exceptions import InvalidIpException

try:
    blacklist.add("192.455.554.343")
except InvalidIpException:
    print("Incorrect Ipv4 Address")

# For CIDR
try:
    blacklist.add("192.12.65.0/16")
except InvalidIpException:
    print("Incorrect CIDR")
```
