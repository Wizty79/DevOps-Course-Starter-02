class Item: 
    def __init__(self, id, title, status = 'To Do'): 
        self.id = id 
        self.title = title 
        self.status = status 
 
    @staticmethod
    def from_trello_card(card, list): 
        return Item(card['id'], card['name'], list['name'])

    @staticmethod
    def from_mongo_item(item): 
        return Item(item['_id'], item['name'], item['status'])



