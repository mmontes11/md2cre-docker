import sys
import re

# spec: https://mariadb.com/kb/en/meta/editing-help/
def md_to_creole(md_text):
    # Headings: Convert Markdown # to Creole ==
    md_text = re.sub(r'^# (.*)', r'== \1 ==', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.*)', r'=== \1 ===', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^### (.*)', r'==== \1 ====', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^#### (.*)', r'===== \1 =====', md_text, flags=re.MULTILINE)

    # Bold: **text** -> **text**
    md_text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', md_text)

    # Italics: *text* -> //text//
    md_text = re.sub(r'\*(.*?)\*', r'//\1//', md_text)

    # Strike-through: ~~text~~ -> <<strike>>text<</strike>>
    md_text = re.sub(r'~~(.*?)~~', r'<<strike>>\1<</strike>>', md_text)

    # Subscript: ~text~ -> ,,text,,
    md_text = re.sub(r'~(.*?)~', r',,\1,,', md_text)

    # Superscript: ^text^ -> ^^text^^
    md_text = re.sub(r'\^(.*?)\^', r'^^\1^^', md_text)

    # Monospace: `text` -> ##text##
    md_text = re.sub(r'`(.*?)`', r'##\1##', md_text)

    # Code blocks: ```code``` -> {{{code}}}
    md_text = re.sub(r'```(.*?)```', r'{{{\n\1\n}}}', md_text, flags=re.DOTALL)

    # Links: [text](url) -> [[url|text]]
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'[[\2|\1]]', md_text)

    # Images: ![alt](url) -> {{url|alt}}
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'{{\2| \1}}', md_text)

    # Horizontal lines: --- or *** -> ----
    md_text = re.sub(r'^(---|\*\*\*)$', r'----', md_text, flags=re.MULTILINE)

    # Tables: Convert Markdown tables to Creole format
    md_text = re.sub(r'^\|(.*?)\|$', lambda m: '|'.join(['=' + x.strip() if i == 0 else x.strip() for i, x in enumerate(m.group(1).split('|'))]), md_text, flags=re.MULTILINE)

    # Lists: Convert Markdown lists to Creole
    md_text = re.sub(r'^\s*-\s(.*)', r'* \1', md_text, flags=re.MULTILINE)  # Unordered lists
    md_text = re.sub(r'^\s*\d+\.\s(.*)', r'# \1', md_text, flags=re.MULTILINE)  # Ordered lists

    # Blockquotes: Convert Markdown > to Creole >
    md_text = re.sub(r'^> (.*)', r'> \1', md_text, flags=re.MULTILINE)

    # Line breaks: Add \\ for forced line breaks
    md_text = md_text.replace('  \n', '\\\\\n')

    return md_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert.py <markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    with open(file_path, "r") as f:
        md_content = f.read()
    
    creole_content = md_to_creole(md_content)
    
    print(creole_content)
