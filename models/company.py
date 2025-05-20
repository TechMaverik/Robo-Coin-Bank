from pydantic import BaseModel
from typing import Optional


class AddCompany(BaseModel):

    company: Optional[str] = None
    ceo: Optional[str] = None
    grade: Optional[str] = None
    division: Optional[str] = None
    s1: Optional[str] = None
    s2: Optional[str] = None
    s3: Optional[str] = None
    s4: Optional[str] = None
    s5: Optional[str] = None
    s6: Optional[str] = None
    balance: Optional[str] = None
    strike: Optional[str] = None
    remarks: Optional[str] = None
    id: Optional[str] = None
