import os
import yaml
import dashscope
from http import HTTPStatus


# 读取 YAML 文件中的 API 密钥
def get_api_key():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
        return config.get('api_key', None)


# 设置阿里云API密钥
dashscope.api_key = get_api_key()


def call_with_prompt(prompt):
    response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_max,
        prompt=prompt
    )
    if response.status_code == HTTPStatus.OK:
        return response.output.text
    else:
        return None


def translate_markdown(input_file, output_file, target_language):
    try:
        # 读取Markdown文档
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()

        # 调用阿里云AI进行翻译
        translated_text = call_with_prompt(markdown_text + "\n将以上markdown文档翻译成" + target_language)

        # 处理翻译结果并导出
        if translated_text:
            output_filename = os.path.splitext(output_file)[0] + '-output.md'
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print(f"翻译并导出成功！输出文件：{output_filename}")
        else:
            print("翻译失败，请检查代码或API密钥。")
    except Exception as e:
        print(f"翻译失败：{str(e)}")


def batch_translate_docs(input_dir, output_dir, target_language):
    try:
        # 检查输出目录是否存在，不存在则创建
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 遍历输入目录下的所有Markdown文件
        for filename in os.listdir(input_dir):
            if filename.endswith('.md'):
                input_file = os.path.join(input_dir, filename)
                output_file = os.path.join(output_dir, filename)
                translate_markdown(input_file, output_file, target_language)
    except Exception as e:
        print(f"批量翻译失败：{str(e)}")


# 示例用法
input_dir = 'docs'  # 输入Markdown文件夹路径
output_dir = 'i18n/zh-cn/docusaurus-plugin-content-docs/current'  # 输出Markdown文件夹路径
target_language = '中文'  # 目标语言默认是中文
batch_translate_docs(input_dir, output_dir, target_language)
