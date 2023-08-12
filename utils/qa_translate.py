from bs4 import BeautifulSoup
import markdown
import re

def parse_mdx_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = file.read()

    questions = re.findall(r'###.*?\n', data, re.DOTALL)
    question_contents= re.findall(r'###.*?<Question', data, re.DOTALL)
    choices = re.findall(r'<Question.*?/>', data, re.DOTALL)
    
    result = []
    for question, choice,question_content in zip(questions, choices,question_contents):
        question_text = question[4:]
        question_content_text=question_content.replace(question,'')[:-9].strip()
        choice_data = []
        for item in re.findall(r'{(.*?)}', str(choice),re.DOTALL):
            item_data = item.split(',')
            text = ":".join(item_data[0].split(':')[1:]).strip().strip('"')
            explain = ":".join(item_data[1].split(':')[1:]).strip().strip('"')
            correct = True if len(item_data) > 2 and ':' in item_data[2] else False
            choice_data.append({'text': text, 'explain': explain, 'correct': correct})
        result.append({'question': question_text, 'choices': choice_data,'content':question_content_text})
    return result

def write_to_markdown_file(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        for i, question_data in enumerate(data, 1):
            # Write question and choices to the question section
            file.write(f'#### {question_data["question"]}\n')
            file.write(f'{question_data["content"]}\n')
            for j, choice in enumerate(question_data["choices"], 1):
                file.write(f'{j}. {choice["text"]}\n')
            file.write('\n')

        # Write a separator between question and answer sections
        file.write('### 解析\n\n')

        for i, question_data in enumerate(data, 1):
            # Write question and explanations to the answer section
            file.write(f'#### {question_data["question"]}\n')
            file.write(f'{question_data["content"]}\n')
            for j, choice in enumerate(question_data["choices"], 1):
                if choice["correct"] == True:
                    file.write(f'正确选项: {j}. {choice["text"]}\n\n')
            for j, choice in enumerate(question_data["choices"], 1):
                file.write(f'{j}. {choice["text"]}    \n')
                file.write(f'解析: {choice["explain"]}\n')
            file.write('\n')
input_file='Course\publish/fix\chapter8/7.mdx'
output_file='Course\publish/fix\chapter8/7_fix.mdx'
# markdown = open(input_file, 'r', encoding='utf-8').read()
data = parse_mdx_file(input_file)
write_to_markdown_file(output_file, data)
text=open(output_file, 'r', encoding='utf-8').read()
text.replace('🤗 ','').replace('🤗','')
text = re.sub(r'^#', "##", text)
#对于异常空行的处理
text=text.replace('\n\n\n','\n\n').replace('\n\n\n','\n\n')
# transformed = transform_mdx(input_file)

with open(output_file, 'w',encoding='utf-8') as f:
    f.write("### 章末测试 \n\n"+text)
