#Reduce multiple blank lines to single (Pythonically)
#https://stackoverflow.com/questions/28901452/reduce-multiple-blank-lines-to-single-pythonically
def strip(fn):
    """Сокращаем лишние пустые строки до одной и возвращаем в переменную."""
    with open(fn + ".txt") as fo:
        lines = ['']
        for line in (l.rstrip() for l in fo):
            if line != '' or lines[-1] != '\n':
                lines.append(line + '\n')
        stripped = "".join(lines)
        return stripped

def save(f,d):
    """Сохраняем файл"""
    with open(f, "w") as fo:
        fo.write(d)
try:
    print("----Multiple blank lines stripper----\n")
    name = input("What .txt file to strip: ")
    data = strip(name)
    save(name + "_st.txt", data)
    print("Done!")
except KeyboardInterrupt:
    print("\nBye")