# AI Markdown 翻译工具

**View English Version**
   - [Click here to view the English version](README-EN.md)

这个工具利用阿里云的 AI 服务实现了 Markdown 文档的翻译功能。它可以批量将 Markdown 文件翻译成英文，并将结果保存到新的文件中。

## 使用说明

1. **准备阿里云 API 密钥**
   - 在阿里云官网注册账号，并申请 API 密钥。
   - 将 API 密钥保存到 `config.yml` 文件中，格式如下：
     ```yaml
     api_key: YOUR_API_KEY
     ```
   - 注意：虽然可以将密钥明文放置，但这并不安全，建议使用环境变量来保存敏感信息。

2. **安装依赖**
   - 使用 Python 环境，安装依赖库：
     ```
     pip install dashscope pyyaml
     ```

3. **运行工具**
   - 将需要翻译的 Markdown 文件放置在 `docs` 目录下。
   - 执行以下命令进行翻译：
     ```bash
     python translate_markdown.py
     ```

4. **查看翻译结果**
   - 翻译结果将保存在 `i18n/zh-cn/docusaurus-plugin-content-docs/current` 目录下。

## 示例用法

```python
import os
import yaml
import dashscope
from http import HTTPStatus

# 代码省略...

