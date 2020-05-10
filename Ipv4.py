"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""

from ip_model.util.Ipv4Tree import Ipv4Tree
from ip_model.util.Validator import Validator
from ipaddress import ip_network

validate = Validator.validate
validate_cidr = Validator.validate_cidr


class Ipv4:
    def __init__(self):
        self.head = Ipv4Tree()

    @validate
    def add(self, ip) -> bool:
        bin_ip = self._to_binary(ip)
        return self.head.add(bin_ip)

    @validate_cidr
    def add_cidr(self, cidr) -> bool:
        return self._insert_cidr(cidr)

    @validate
    def remove(self, ip) -> bool:
        bin_ip = self._to_binary(ip)
        self.head.remove(bin_ip)

    @validate_cidr
    def remove_cidr(self, cidr) -> bool:
        self._remove_cidr(cidr)

    @validate
    def is_present(self, ip) -> bool:
        bin_ip = self._to_binary(ip)
        return self.head.is_present(bin_ip)

    def _to_binary(self, ip):
        binary_ip = ""
        for x in ip.split("."):
            binary_ip += f'{int(x):08b}'
        return binary_ip

    def _insert_cidr(self, cidr) -> bool:
        ins = True
        for ip in ip_network(cidr):
            ins = ins and self.add(str(ip))
        return ins

    def _remove_cidr(self, cidr) -> bool:
        for ip in ip_network(cidr):
            self.remove(str(ip))
