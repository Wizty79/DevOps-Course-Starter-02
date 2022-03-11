from todo_app.data.view_model import ViewModel
from todo_app.data.item import Item

# Requirements for todo_items property
# - Status, if Todo keep, if not Todo throw away


def test_todo_items_property_only_shows_doing_items_and_not_anything_else():
    #Arrange -  Create an instance of ViewModel containing some example Item objects with various statuses
    items = [
        Item("1", "A Test Todo", "To Do"),
        Item("2", "An in progress Todo", "Doing"),
        Item("3", "A completed Todo", "Done")
    ]

    view_model = ViewModel(items)


    #Act -  Get the result of the view model's new doing_items property (though this will actually be an empty list for now).
    test_todo_items = view_model.todo_items

    assert len(test_todo_items) == 1

    todo_item = test_todo_items[0]

    assert todo_item.id == "1"
    assert todo_item.title == "A Test Todo"
    assert todo_item.status == "To Do"

