# Prompts user for file name
file = input("File Name: ").strip().split(".")

# checks the extension at the end of the file after the dot
match file[-1]:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf" | "PDF":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")