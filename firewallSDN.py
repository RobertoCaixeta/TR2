from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventMixin
from pox.lib.addresses import EthAddr

log = core.getLogger()

# Constants for static data

FIREWALL_RULES = [
  ['00:00:00:00:00:01', '00:00:00:00:00:03'],
  ['00:00:00:00:00:03', '00:00:00:00:00:01']
]

class L2Firewall(EventMixin):
  def __init__(self):
    self.listenTo(core.openflow)

  def _handle_ConnectionUp(self, event):
    for rule in FIREWALL_RULES:
      block = of.ofp_match()
      block.dl_src = EthAddr(rule[0])
      block.dl_dst = EthAddr(rule[1])

      flow_mod = of.ofp_flow_mod()
      flow_mod.match = block

      event.connection.send(flow_mod)

def launch():
  core.registerNew(L2Firewall)