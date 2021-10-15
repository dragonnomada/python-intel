import bots

bots.create_folder("foo/bar/gee")

bots.create_file("foo/hello.txt", "Hola mundo mundial")

date = bots.date_when("+ 1 day - 5 hours")

print("Fecha", date)

date = bots.date_when("last wednesday")

print("Fecha", date)

files = bots.list_files("*.py")

print(files)

for filename in files:
    bots.copy_file(filename, f"foo/{filename}")