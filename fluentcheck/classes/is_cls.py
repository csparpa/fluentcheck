from typing import Any

from ..assertions_is.booleans import __IsBool
from ..assertions_is.collections import __IsCollections
from ..assertions_is.dicts import __IsDicts
from ..assertions_is.emptiness import __IsEmptiness
from ..assertions_is.geo import __IsGeo
from ..assertions_is.numbers import __IsNumbers
from ..assertions_is.sequences import __IsSequences
from ..assertions_is.strings import __IsStrings
from ..assertions_is.types import __IsTypes
from ..assertions_is.uuids import __IsUUIDs


class Is(__IsBool, __IsCollections, __IsDicts, __IsEmptiness, __IsGeo,
         __IsNumbers, __IsSequences, __IsStrings, __IsTypes, __IsUUIDs):
    pass
