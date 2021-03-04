def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None # 設為虛無的，避免程式在沒有person參數時(txt檔第一行字不是Allen or Tom)，執行new.append(person......)時當掉，
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: # 如果person有值的話，就會執行
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n') # 寫入功能

# 隨著程式執行，將function執行後所回傳的值傳給lines，不停地覆蓋掉。
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main()