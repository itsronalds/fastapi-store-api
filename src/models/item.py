import json


class Item:


    @staticmethod
    def get_items():
        with open('src/db/mock.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('items', [])

    
    @staticmethod
    def get_item(item_id: int):
        with open('src/db/mock.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('items', [])
            for item in items:
                if item['id'] == item_id:
                    return item
            return None
        