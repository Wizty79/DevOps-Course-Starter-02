class Item: 
    def __init__(self, id, title, status = 'To Do'): 
        self.id = id 
        self.title = title 
        self.status = status 
 
    @staticmethod
    def from_trello_card(card, list): 
        return Item(card['id'], card['name'], list['name'])

class ViewModel:
	def __init__(self, items):
		self._items = items
 
	@property
	def items(self):
		return self._items



