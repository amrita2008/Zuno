import tempfile


def save_uploaded_file(uploaded_file):

    suffix = uploaded_file.name.split(".")[-1]

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{suffix}",
    )

    temp.write(uploaded_file.read())

    temp.close()

    return temp.name
