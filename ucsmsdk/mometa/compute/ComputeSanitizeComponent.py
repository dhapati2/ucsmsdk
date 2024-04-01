"""This module contains the general information for ComputeSanitizeComponent ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeSanitizeComponentConsts:
    DS_STATUS_COMPLETED = "completed"
    DS_STATUS_FAILED = "failed"
    DS_STATUS_IN_PROGRESS = "in-progress"
    DS_STATUS_NONE = "none"
    DS_STATUS_READY = "ready"
    DS_TYPE_BOARD_DOMAIN = "board-domain"
    DS_TYPE_HOST_DOMAIN = "host-domain"
    DS_TYPE_PNU_OS = "pnuOS"
    DS_TYPE_VIC = "vic"


class ComputeSanitizeComponent(ManagedObject):
    """This is ComputeSanitizeComponent class."""

    consts = ComputeSanitizeComponentConsts()
    naming_props = set(['dsType'])

    mo_meta = MoMeta("ComputeSanitizeComponent", "computeSanitizeComponent", "ds-comp-[ds_type]", VersionMeta.Version434a, "InputOutput", 0x3f, [], ["admin"], ['computeDataSanitize'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "ds_completion": MoPropertyMeta("ds_completion", "dsCompletion", "uint", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "ds_end_time": MoPropertyMeta("ds_end_time", "dsEndTime", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "ds_failed_comps": MoPropertyMeta("ds_failed_comps", "dsFailedComps", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "ds_sanitized_comps": MoPropertyMeta("ds_sanitized_comps", "dsSanitizedComps", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "ds_start_time": MoPropertyMeta("ds_start_time", "dsStartTime", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "ds_status": MoPropertyMeta("ds_status", "dsStatus", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["completed", "failed", "in-progress", "none", "ready"], []),
        "ds_type": MoPropertyMeta("ds_type", "dsType", "string", VersionMeta.Version434a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["board-domain", "host-domain", "pnuOS", "vic"], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version434a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "dsCompletion": "ds_completion", 
        "dsEndTime": "ds_end_time", 
        "dsFailedComps": "ds_failed_comps", 
        "dsSanitizedComps": "ds_sanitized_comps", 
        "dsStartTime": "ds_start_time", 
        "dsStatus": "ds_status", 
        "dsType": "ds_type", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, ds_type, **kwargs):
        self._dirty_mask = 0
        self.ds_type = ds_type
        self.child_action = None
        self.ds_completion = None
        self.ds_end_time = None
        self.ds_failed_comps = None
        self.ds_sanitized_comps = None
        self.ds_start_time = None
        self.ds_status = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeSanitizeComponent", parent_mo_or_dn, **kwargs)
