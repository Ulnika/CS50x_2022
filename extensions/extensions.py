extensions = input("File name: ").lower().strip().split(".")

if len(extensions) <= 1:
    print("application/octet-stream")
else:
    if extensions[-1] == "gif" or extensions[1] == "png":
        print("image/" + extensions[-1])
    elif extensions[-1] == "jpg" or extensions[1] == "jpeg":
        print("image/jpeg")
    elif extensions[-1] == "pdf":
        print("application/pdf")
    elif extensions[-1] == "txt":
        print("text/plain")
    elif extensions[-1] == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")



