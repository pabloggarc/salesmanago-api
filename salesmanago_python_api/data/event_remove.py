import re
import datetime
from typing import Optional
from dataclasses import dataclass, field


@dataclass
class SalesManagoDeleteEventData:
    '''
        Class for interfacing with event instances of SalesManago platform.
        Structure is valid for following API actions: /api/v2/contact/deleteContactExtEvent
    '''

    owner: str
    _owner: str = field(init=False, repr=False, default=None)

    eventId: Optional[str] = None
    externalId: Optional[str] = None

    def __post_init__(self):
        if not self.owner:
            raise ValueError('owner[str] is required')

        if not self.eventId and not self.externalId:
            raise ValueError('eventId[str] or externalId[str] is required')

    @property
    def owner(self) -> str:
        return self._owner

    @owner.setter
    def owner(self, owner: str) -> None:
        if type(owner) is property:
            owner = self._owner

        if owner and not self._validate_email(owner):
            raise ValueError('%s is not valid OWNER e-mail' % owner)

        self._owner = owner
    
    def _validate_email(self, email: str) -> bool:
        mailre = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return bool(mailre.match(email))
    
    def requestDict(self) -> dict:
        """
        Prepare the dictionary payload for the API request based on the instance attributes.
        """
        rdata = {
            'owner': self.owner
        }

        if self.eventId:
            rdata['eventId'] = self.eventId

        if self.externalId:
            rdata['externalId'] = self.externalId

        return rdata
