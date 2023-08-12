import os

target_hex = "0020AF30"
new_filename = ""
for filename in os.listdir():
    if filename.endswith(".tpl"):
        print(filename)
    if filename.endswith(".bin") or filename.endswith(".rel"):
        try:
            with open(filename, "rb") as file:
                hex_values = file.read(4).hex().upper()
                if hex_values == target_hex:
                    new_filename = filename.rsplit(".", 1)[0] + ".tpl"
                else:
                    print(f"{filename} is not a TPL file.")
            if new_filename:
                os.rename(filename, new_filename)
                print(f"Renamed {filename} to {new_filename}")
        except OSError as e:
            print(f"Error renaming {filename}: {e}")
