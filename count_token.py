import tiktoken
import os
import time
import argparse



def translate_file(input_file_path):
    gpt_encoding = tiktoken.encoding_for_model("gpt-4o")
    try:
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            tokens = gpt_encoding.encode(text)
            return len(tokens)
#            print(f"Number of tokens: {token_count}") 
    except Exception as e:
        print(f"Error processing file {input_file_path}: {e}")

def translate_folder(input_folder):
    total_md = 0
    total_tokens = 0
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".md"):
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, input_folder)
                token_count = translate_file(input_file_path)
                print(f"Number of tokens: {token_count}")  
                total_tokens += token_count
                total_md += 1
    print(f"total_md files {total_md}")
    print(f"total_tokens{total_tokens}")

def main():
    parser = argparse.ArgumentParser(description="Translate Markdown files in a folder.")
    parser.add_argument("input_folder", help="Path to the input folder containing markdown files")
    args = parser.parse_args()
    translate_folder(args.input_folder)

if __name__ == "__main__":
    main()