from trac.core import *
from trac.perm import IPermissionRequestor

class SCMAccessControlPlugin(Component):
    implements(IPermissionRequestor)

    def get_permission_actions(self):
        return ['SCM_VIEW', 'SCM_EDIT']