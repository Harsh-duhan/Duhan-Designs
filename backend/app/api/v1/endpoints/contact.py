from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_contact
from app.schemas.contact import ContactCreate, Contact

router = APIRouter()

@router.post("/", response_model=Contact)
def create_contact(
    *,
    db: Session = Depends(deps.get_db),
    contact_in: ContactCreate,
) -> Any:
    """
    Create new contact inquiry.
    """
    contact = crud_contact.create_contact(db, contact=contact_in)
    return contact
