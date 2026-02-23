"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Any
from typing import TYPE_CHECKING

from jinja2.runtime import Undefined

if TYPE_CHECKING:
    from encommon.parse.jinja2 import FILTERS



class FilterModule:
    """
    Define filter functions available with Ansible routines.

    .. note::
       This class is duplicative on purpose due to Ansible.
       It is intentionally present in both filter and test,
       to allow for both pipe (`|`) and `is` operations.
    """


    def filters(
        # NOCVR
        self,
    ) -> 'FILTERS':
        """
        Return the filter functions for use in Ansible routines.

        :returns: Filter functions for use in Ansible routines.
        """

        return {'present': present}



def present(  # noqa: CFQ004
    value: Any,  # noqa: ANN401
) -> bool:
    """
    Return the boolean indicating whether value is present.

    .. note::
       This function is duplicated until moved to encommon.

    :param value: Value which will be determined if present.
    :returns: Boolean indicating whether value is present.
    """

    if (isinstance(value, Undefined)
            or value is None):
        return False

    if isinstance(value, bool):
        return value

    if hasattr(value, '__len__'):
        return len(value) >= 1

    return True
