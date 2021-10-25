from browser import document, console


def show_text(event):
    console.log(event.target.value)
    document["output"].textContent = event.target.value


document["text"].bind("input", show_text)