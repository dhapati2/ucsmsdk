"""This module contains the general information for ComputeDataSanitize ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeDataSanitizeConsts:
    DS_ADMIN_ACTION_BOARD_DOMAIN = "board-domain"
    DS_ADMIN_ACTION_HOST_BOARD_DOMAIN = "host-board-domain"
    DS_ADMIN_ACTION_HOST_DOMAIN = "host-domain"
    DS_ADMIN_ACTION_NONE = "none"
    DS_DECOM_SERVER_FALSE = "false"
    DS_DECOM_SERVER_NO = "no"
    DS_DECOM_SERVER_TRUE = "true"
    DS_DECOM_SERVER_YES = "yes"
    DS_STATUS_COMPLETED = "completed"
    DS_STATUS_FAILED = "failed"
    DS_STATUS_IN_PROGRESS = "in-progress"
    DS_STATUS_NONE = "none"
    DS_STATUS_READY = "ready"


class ComputeDataSanitize(ManagedObject):
    """This is ComputeDataSanitize class."""

    consts = ComputeDataSanitizeConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeDataSanitize", "computeDataSanitize", "data-sanitize", VersionMeta.Version434a, "InputOutput", 0x7f, [], ["admin"], ['computeBlade', 'computeRackUnit', 'computeServerUnit'], ['computeSanitizeComponent'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ds_admin_action": MoPropertyMeta("ds_admin_action", "dsAdminAction", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["board-domain", "host-board-domain", "host-domain", "none"], []),
        "ds_decom_server": MoPropertyMeta("ds_decom_server", "dsDecomServer", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []),
        "ds_status": MoPropertyMeta("ds_status", "dsStatus", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "failed", "in-progress", "none", "ready"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "dsAdminAction": "ds_admin_action", 
        "dsDecomServer": "ds_decom_server", 
        "dsStatus": "ds_status", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.ds_admin_action = None
        self.ds_decom_server = None
        self.ds_status = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeDataSanitize", parent_mo_or_dn, **kwargs)
