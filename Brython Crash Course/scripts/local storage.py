from browser import document, html, window, console

storage = window.localStorage

if storage.getItem("item"):
    document["item"] <= storage.getItem("item")


def add_item(event):
    item = document["item-input"].value
    console.log(item)
    storage.setItem("item", item)
    document["item"].textContent = item


def remove_item(event):
    storage.removeItem("item")
    document["item"].textContent = ""


document["add-button"].bind("click", add_item)
document["remove-button"].bind("click", remove_item)