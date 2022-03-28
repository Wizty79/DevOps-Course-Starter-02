from todo_app.data.view_model import ViewModel
from todo_app.data.item import Item

# Requirements for todo_items property
# - Status, if Todo keep, if not Todo throw away

def test_todo_items_property_only_shows_todo_items_and_not_anything_else():
    #Arrange -  Create an instance of ViewModel containing some example Item objects with various statuses
    items = [
        Item("1", "A Test Todo", "To Do"),
        Item("2", "An in progress Todo", "Doing"),
        Item("3", "A completed Todo", "Done")
    ]

    view_model = ViewModel(items)


    #Act -  Get the result of the view model's new todo_items property (though this will actually be an empty list for now).
    test_todo_items = view_model.todo_items

    assert len(test_todo_items) == 1

    todo_item = test_todo_items[0]

    assert todo_item.id == "1"
    assert todo_item.title == "A Test Todo"
    assert todo_item.status == "To Do"


def test_done_items_property_only_shows_done_items_and_not_anything_else():
    #Arrange -  Create an instance of ViewModel containing some example Item objects with various statuses
    items = [
        Item("1", "A Test Todo", "To Do"),
        Item("2", "An in progress Todo", "Doing"),
        Item("3", "A completed Todo", "Done")
    ]

    view_model = ViewModel(items)

    #Act -  Get the result of the view model's new done_items property (though this will actually be an empty list for now).
    test_done_items = view_model.done_items

    assert len(test_done_items) == 1

    todo_item = test_done_items[0]

    assert todo_item.id == "1"
    assert todo_item.title == "A Test Todo"
    assert todo_item.status == "To Do"