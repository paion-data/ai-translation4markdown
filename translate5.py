import dashscope
from http import HTTPStatus

# 设置阿里云API密钥
dashscope.api_key = 'sk-ba382c83374640c4bb8d36535acbfc6b'

def call_with_prompt(prompt):
    response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_max,
        prompt=prompt
    )
    if response.status_code == HTTPStatus.OK:
        return response.output.text
    else:
        return None

def translate_markdown_and_export(input_file, output_file):
    # 读取Markdown文档
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # 调用阿里云AI进行翻译
    translated_text = call_with_prompt(markdown_text + "\n将以上markdown文档翻译成中文")

    # 处理翻译结果并导出
    if translated_text:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_text)
        print("翻译并导出成功！")
    else:
        print("翻译失败，请检查代码或API密钥。")

# 示例用法
input_file = 'docs/example.md'  # 输入Markdown文件路径
output_file = 'i18n/zh-cn/docusaurus-plugin-content-docs/current/outputExample.md'  # 输出Markdown文件路径
translate_markdown_and_export(input_file, output_file)



