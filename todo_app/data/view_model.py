class ViewModel:
	def __init__(self, items):
		self._items = items
 
	@property
	def items(self):
		return self._items
		
	@property
	def todo_items(self): 
        
    	todo_list_items = []
                
    	for item in self.items: 
            if status == 'To Do':   
	            print (todo_list_items.append(item)) 
            
    	return todo_list_items
	
