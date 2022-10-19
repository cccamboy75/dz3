def delete_htmltags(html, result=open('C:/Users/1/PycharmProjects/pythonProject/venv/cleaned.txt', 'w', encoding='utf-8')):
    html = html.replace(html[html.find('<'):html.find('>') + 1], "")
    if '<' and '>' in html:
        delete_htmltags(html)
    else:
        result.write(html)
        result.close()
    return None


def delede_line(file, result=open('C:/Users/1/PycharmProjects/pythonProject/venv/cleaned.txt', 'w', encoding='utf-8')):
    for i in range(len(file)):
        file[i] = file[i].strip()
    f = []
    for x in range(len(file)):
        if file[x] != "":
            f.append(file[x])
    text = '\n'.join(f)
    result.write(text)
    result.close()
    return None


old_text = open('C:/Users/1/PycharmProjects/pythonProject/venv/draft.html', 'r', encoding='utf-8')
a = old_text.read()
delete_htmltags(a)
new_text = open('C:/Users/1/PycharmProjects/pythonProject/venv/cleaned.txt', 'r', encoding='utf-8')
b = new_text.readlines()
delede_line(b)