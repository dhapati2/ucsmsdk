"""This module contains the general information for AdaptorEthPortPfcStats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorEthPortPfcStatsConsts:
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TRAFFIC_DIRECTION_RX = "rx"
    TRAFFIC_DIRECTION_TX = "tx"
    TRAFFIC_DIRECTION_UNKNOWN = "unknown"


class AdaptorEthPortPfcStats(ManagedObject):
    """This is AdaptorEthPortPfcStats class."""

    consts = AdaptorEthPortPfcStatsConsts()
    naming_props = set(['trafficDirection'])

    mo_meta = MoMeta("AdaptorEthPortPfcStats", "adaptorEthPortPfcStats", "eth-port-pfc-stats-[traffic_direction]", VersionMeta.Version434a, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorExtEthIf'], ['adaptorEthPortPfcStatsHist'], [None])

    prop_meta = {
        "active_pfc_bits": MoPropertyMeta("active_pfc_bits", "activePfcBits", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0": MoPropertyMeta("priority0", "priority0", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0_delta": MoPropertyMeta("priority0_delta", "priority0Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0_delta_avg": MoPropertyMeta("priority0_delta_avg", "priority0DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0_delta_max": MoPropertyMeta("priority0_delta_max", "priority0DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority0_delta_min": MoPropertyMeta("priority0_delta_min", "priority0DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1": MoPropertyMeta("priority1", "priority1", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_delta": MoPropertyMeta("priority1_delta", "priority1Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_delta_avg": MoPropertyMeta("priority1_delta_avg", "priority1DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_delta_max": MoPropertyMeta("priority1_delta_max", "priority1DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority1_delta_min": MoPropertyMeta("priority1_delta_min", "priority1DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2": MoPropertyMeta("priority2", "priority2", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_delta": MoPropertyMeta("priority2_delta", "priority2Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_delta_avg": MoPropertyMeta("priority2_delta_avg", "priority2DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_delta_max": MoPropertyMeta("priority2_delta_max", "priority2DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority2_delta_min": MoPropertyMeta("priority2_delta_min", "priority2DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3": MoPropertyMeta("priority3", "priority3", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_delta": MoPropertyMeta("priority3_delta", "priority3Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_delta_avg": MoPropertyMeta("priority3_delta_avg", "priority3DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_delta_max": MoPropertyMeta("priority3_delta_max", "priority3DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority3_delta_min": MoPropertyMeta("priority3_delta_min", "priority3DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4": MoPropertyMeta("priority4", "priority4", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_delta": MoPropertyMeta("priority4_delta", "priority4Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_delta_avg": MoPropertyMeta("priority4_delta_avg", "priority4DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_delta_max": MoPropertyMeta("priority4_delta_max", "priority4DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority4_delta_min": MoPropertyMeta("priority4_delta_min", "priority4DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5": MoPropertyMeta("priority5", "priority5", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_delta": MoPropertyMeta("priority5_delta", "priority5Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_delta_avg": MoPropertyMeta("priority5_delta_avg", "priority5DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_delta_max": MoPropertyMeta("priority5_delta_max", "priority5DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority5_delta_min": MoPropertyMeta("priority5_delta_min", "priority5DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6": MoPropertyMeta("priority6", "priority6", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_delta": MoPropertyMeta("priority6_delta", "priority6Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_delta_avg": MoPropertyMeta("priority6_delta_avg", "priority6DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_delta_max": MoPropertyMeta("priority6_delta_max", "priority6DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority6_delta_min": MoPropertyMeta("priority6_delta_min", "priority6DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7": MoPropertyMeta("priority7", "priority7", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_delta": MoPropertyMeta("priority7_delta", "priority7Delta", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_delta_avg": MoPropertyMeta("priority7_delta_avg", "priority7DeltaAvg", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_delta_max": MoPropertyMeta("priority7_delta_max", "priority7DeltaMax", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "priority7_delta_min": MoPropertyMeta("priority7_delta_min", "priority7DeltaMin", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "traffic_direction": MoPropertyMeta("traffic_direction", "trafficDirection", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, None, None, None, None, ["rx", "tx", "unknown"], []),
        "unit": MoPropertyMeta("unit", "unit", "ulong", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "activePfcBits": "active_pfc_bits", 
        "childAction": "child_action", 
        "dn": "dn", 
        "intervals": "intervals", 
        "priority0": "priority0", 
        "priority0Delta": "priority0_delta", 
        "priority0DeltaAvg": "priority0_delta_avg", 
        "priority0DeltaMax": "priority0_delta_max", 
        "priority0DeltaMin": "priority0_delta_min", 
        "priority1": "priority1", 
        "priority1Delta": "priority1_delta", 
        "priority1DeltaAvg": "priority1_delta_avg", 
        "priority1DeltaMax": "priority1_delta_max", 
        "priority1DeltaMin": "priority1_delta_min", 
        "priority2": "priority2", 
        "priority2Delta": "priority2_delta", 
        "priority2DeltaAvg": "priority2_delta_avg", 
        "priority2DeltaMax": "priority2_delta_max", 
        "priority2DeltaMin": "priority2_delta_min", 
        "priority3": "priority3", 
        "priority3Delta": "priority3_delta", 
        "priority3DeltaAvg": "priority3_delta_avg", 
        "priority3DeltaMax": "priority3_delta_max", 
        "priority3DeltaMin": "priority3_delta_min", 
        "priority4": "priority4", 
        "priority4Delta": "priority4_delta", 
        "priority4DeltaAvg": "priority4_delta_avg", 
        "priority4DeltaMax": "priority4_delta_max", 
        "priority4DeltaMin": "priority4_delta_min", 
        "priority5": "priority5", 
        "priority5Delta": "priority5_delta", 
        "priority5DeltaAvg": "priority5_delta_avg", 
        "priority5DeltaMax": "priority5_delta_max", 
        "priority5DeltaMin": "priority5_delta_min", 
        "priority6": "priority6", 
        "priority6Delta": "priority6_delta", 
        "priority6DeltaAvg": "priority6_delta_avg", 
        "priority6DeltaMax": "priority6_delta_max", 
        "priority6DeltaMin": "priority6_delta_min", 
        "priority7": "priority7", 
        "priority7Delta": "priority7_delta", 
        "priority7DeltaAvg": "priority7_delta_avg", 
        "priority7DeltaMax": "priority7_delta_max", 
        "priority7DeltaMin": "priority7_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "trafficDirection": "traffic_direction", 
        "unit": "unit", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, traffic_direction, **kwargs):
        self._dirty_mask = 0
        self.traffic_direction = traffic_direction
        self.active_pfc_bits = None
        self.child_action = None
        self.intervals = None
        self.priority0 = None
        self.priority0_delta = None
        self.priority0_delta_avg = None
        self.priority0_delta_max = None
        self.priority0_delta_min = None
        self.priority1 = None
        self.priority1_delta = None
        self.priority1_delta_avg = None
        self.priority1_delta_max = None
        self.priority1_delta_min = None
        self.priority2 = None
        self.priority2_delta = None
        self.priority2_delta_avg = None
        self.priority2_delta_max = None
        self.priority2_delta_min = None
        self.priority3 = None
        self.priority3_delta = None
        self.priority3_delta_avg = None
        self.priority3_delta_max = None
        self.priority3_delta_min = None
        self.priority4 = None
        self.priority4_delta = None
        self.priority4_delta_avg = None
        self.priority4_delta_max = None
        self.priority4_delta_min = None
        self.priority5 = None
        self.priority5_delta = None
        self.priority5_delta_avg = None
        self.priority5_delta_max = None
        self.priority5_delta_min = None
        self.priority6 = None
        self.priority6_delta = None
        self.priority6_delta_avg = None
        self.priority6_delta_max = None
        self.priority6_delta_min = None
        self.priority7 = None
        self.priority7_delta = None
        self.priority7_delta_avg = None
        self.priority7_delta_max = None
        self.priority7_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unit = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorEthPortPfcStats", parent_mo_or_dn, **kwargs)
