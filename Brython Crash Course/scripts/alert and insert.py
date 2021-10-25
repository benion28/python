from browser import document, console, alert


def show(event):
    console.log("Benion Says Welcome")
    console.log(event)
    alert("Hello From BeniFresh")
    document["hello"] <= "Hello From Benion"


document["alert-button"].bind("click", show)