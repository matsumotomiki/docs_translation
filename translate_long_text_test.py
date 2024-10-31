import os
import time
import argparse
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def translate_folder(input_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".md"):
                input_file_path = os.path.join(root, file)
                # Open the file to read its contents
                with open(input_file_path, "r", encoding="utf-8") as input_file:
                    text_len = len(input_file.read())
                if text_len > 50000:
                    print(f"{text_len} : {input_file_path}")

def main():
    parser = argparse.ArgumentParser(description="Translate Markdown files in a folder.")
    parser.add_argument("input_folder", help="Path to the input folder containing markdown files")
    args = parser.parse_args()
    translate_folder(args.input_folder)

if __name__ == "__main__":
    main()
