import scapy.all as scapy
import optparse as opt

def scan (ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    both = broadcast / arp_request
    (answered , unanswered) = scapy.srp(both, timeout=1)
    answered.summary()

def getInput ():
    parse_object = opt.OptionParser()
    parse_object.add_option("-i","--ip",dest="ip_address",help ="Enter IP Adress")
    (input,arguments) = parse_object.parse_args()
    return input

user_ip = getInput()
scan(user_ip.ip_address)
