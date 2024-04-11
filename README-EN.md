**AI Markdown Translation Tool**

**查看中文版本**
   - [Click here to view the English version](README.md)

This tool utilizes Alibaba Cloud's AI services to implement translation functionality for Markdown documents. It can batch-translate Markdown files into English and save the results to new files.

## Usage Instructions

1. **Prepare Alibaba Cloud API Key**
   - Register an account on the Alibaba Cloud official website and apply for an API key.
   - Save the API key in the `config.yml` file as follows:
     ```yaml
     api_key: YOUR_API_KEY
     ```
   - Note: Although it is possible to store the key in plain text, this is not secure. It is recommended to use environment variables for sensitive information.

2. **Install Dependencies**
   - Using a Python environment, install the required libraries:
     ```
     pip install dashscope pyyaml
     ```

3. **Run the Tool**
   - Place the Markdown files you wish to translate in the `docs` directory.
   - Execute the following command to perform the translation:
     ```bash
     python translate_markdown.py
     ```

4. **View Translation Results**
   - The translated results will be saved in the `i18n/zh-cn/docusaurus-plugin-content-docs/current` directory.

## Example Usage

```python
import os
import yaml
import dashscope
from http import HTTPStatus

# Code omitted...
```

Translate the above Markdown document into English.