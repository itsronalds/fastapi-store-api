from fastapi import APIRouter

from src.models.item import Item

router = APIRouter()


@router.get('/items')
def read_items():
    items = Item.get_items()
    return {'items': items}


@router.get('/items/{item_id}')
def read_item(item_id: int):
    pass


@router.post('/items/create')
def create_item():
    pass


@router.put('/items/update/{item_id}')
def update_item(item_id: int):
    pass


@router.delete('/items/delete/{item_id}')
def delete_item(item_id: int):
    pass
