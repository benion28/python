from browser import document, window


def file_read(event):
    def onload(event):
        document["file-text"].value = event.target.result


    file = document["file-output"].files[0]
    reader = window.FileReader.new()
    reader.readAsText(file)
    reader.bind("load", onload)

document["file-output"].bind("input", file_read)