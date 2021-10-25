from browser import document, ajax, console

url = "https://api.chucknorris.io/jokes/random"


def on_complete(request):
    console.log(request.responseText)
    import json
    data = json.loads(request.responseText)
    console.log(data["value"])
    joke = data["value"]
    document["joke"].text = joke


def get_joke(event):
    request = ajax.ajax()
    request.open("GET", url, True)
    request.bind("complete", on_complete)
    document["joke"].text = "Loading....."
    request.send()


document["joke-button"].bind("click", get_joke)