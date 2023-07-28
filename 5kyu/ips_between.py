# Implement a function that receives two IPv4 addresses, and returns the number of addresses
# between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings.
# The last address will always be greater than the first one.
# * With input "10.0.0.0", "10.0.0.50"  => return   50
# * With input "10.0.0.0", "10.0.1.0"   => return  256
# * With input "20.0.0.10", "20.0.1.0"  => return  246

def ips_between(start, end) -> int:
    from_list = list(map(lambda x: int(x), a.split(".")))[::-1]
    to_list = list(map(lambda x: int(x), b.split(".")))[::-1]
    a = 0
    b = 0
    for i in range(4):
        a += from_list[i] * (256 ** i)
        b += to_list[i] * (256 ** i)
    return b - a

# from ipaddress import ip_address

# def ips_between(start, end):
#     return int(ip_address(end)) - int(ip_address(start))
