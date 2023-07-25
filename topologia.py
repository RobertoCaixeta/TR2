from mininet.net import Mininet
from mininet.node import RemoteController, OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def customTopo():

  #net = Mininet(controller=OVSController)
  net = Mininet(controller=RemoteController)

  print('** Adding controller')
  net.addController('c0')

  print('*** Adding hosts')
  hosts = []
  for i in range(1, 11):
    host_ip = f'10.0.0.{i}'
    host_mac = f'00:00:00:00:00:{i:02}'
    host = net.addHost(f'h{i}', ip=host_ip, mac=host_mac)
    hosts.append(host)

  print('*** Adding switches')
  switches = []
  for i in range(1, 5):
    switch = net.addSwitch(f's{i}')
    switches.append(switch)

  print('*** Creating links')

  for i in range(0, len(hosts)):
    net.addLink(hosts[i], switches[i // 4])

  for i in range(0, len(switches) - 1):
    net.addLink(switches[i], switches[-1])

  print('*** Starting network')
  net.start()

  print('*** Running CLI')
  CLI(net)

  print('*** Stopping network')
  net.stop()

if __name__ == '__main__':
  setLogLevel('info')
  customTopo()