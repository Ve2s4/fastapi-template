from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.models.item import Item
from app.schemas.item import ItemBase

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_items(db: Session = Depends(get_db), skip: int = 0, take: int = 10):
    try:
        all_items = Item.get_all_items(db, skip=skip, take=take)
        return {"message": "Items fetched successfully", "data": all_items}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {str(e)}")


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_item(mail: ItemBase, db: Session = Depends(get_db)):
    try:
        new_item = Item.create_item(Item(**mail.model_dump()), db)
        return {"message": "Item posted successfully", "data": new_item}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {str(e)}")