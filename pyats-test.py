from genie import testbed
from unicon import Connection
from pprint import pprint

print("genie example")

testbed = testbed.load('testbed.yaml')

router = testbed.devices['bogfam1921']
switch = testbed.devices['bogfam3560']

# connect to the devices using the testbed.yaml file
print (f"Connecting to {router}...")
router.connect(log_stdout=False)
print (f"Connecting to {switch}...")
switch.connect(log_stdout=False)

# Note all parsers are available: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers

output = router.parse("show ip static route")
#pprint (output)

print (f"Displaying the 'show ip static route' table for {router}")
# In this example, we are going to parse out the next hops for the static routes
value = output['vrf']['default']['address_family']['ipv4']['routes']
for key in value:
    print (f"{key:20}    Next Hop: {value[key]['next_hop']['next_hop_list'][1]['next_hop']} ")


print (f"Displaying the 'show interfaces status' table for {switch}")
output = switch.parse("show interfaces status")
# Print out each interface if the port is not a trunk
for key in output['interfaces']:
    if (output['interfaces'][key]['vlan'] != "trunk"):
        print (f"{key:20} ----- {output['interfaces'][key]['vlan']}")


#Perform clean disconnections
router.disconnect()
switch.disconnect()
