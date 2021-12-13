#!/usr/bin/env python3
import subprocess;
import optparse;


def change_Mac(options):

    print("[+] Changing mac addres for " + options.interface + " to " + options.mac_address);

    subprocess.call(["ifconfig", options.interface, "down"]);
    subprocess.call(["ifconfig", options.interface, "hw", "ether", options.mac_address]);
    subprocess.call(["ifconfig", options.interface, "up"]);
    ifconfig_result = subprocess.check_output(["ifconfig"]);
    print("[+] Successfully changed the mac address of your interface named as " + options.interface);

parser = optparse.OptionParser();
parser.add_option("-i", "--interface", dest="interface", help="Interface to change the name");
parser.add_option("-m", "--mac", dest="mac_address", help="Add mac address for the interface");
(options, arguments) = parser.parse_args();
if not options.interface:
    parser.error("[+] Please enter an Interface name or use --help")
elif not options.mac_address:
    parser.error("[+] Please enter mac address or use --help")
else:
    change_Mac(options); #function_Setter

