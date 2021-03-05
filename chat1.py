def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip()) # strip()功能: 去掉空格 
    return lines


def convert(lines):
    new = []
    person = None # 設為虛無的
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('allen說了', allen_word_count, ',傳了', allen_sticker_count, '個貼圖,', allen_image_count, '張圖片')
    print('Viki說了', viki_word_count, ',傳了', viki_sticker_count, '個貼圖,', viki_image_count, '張圖片')
    return lines


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n') # 寫入功能


# 隨著程式執行，將function執行後所回傳的值傳給lines，下一行執行後覆蓋掉前次結果。
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('Words_count.txt', lines)

main()