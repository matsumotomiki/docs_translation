import os
import time
import argparse
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def translate_text(text, target_language="Japanese"):
    try:
        # translation using GPT
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Translate the following ClickHouse documentation text from English to {target_language}. Please maintain the original markdown formatting used in Docusaurus, including any headings, code blocks, lists, links, and inline formatting like bold or italic text. Ensure that no content, links, or references are omitted or altered during translation, preserving the same amount of information as the original text. This translation is intended for users familiar with database and IT terminology, so use technical and accurate language. Keep the translation precise and professional, reflecting the technical nature of the content. Do not translate code, URLs, or any part of the markdown structure, and make sure all links are correctly preserved in the translated text."},
                {"role": "user", "content": text}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"failed to translate: {e}")
        return None

def translate_file(input_file_path, output_file_path):
    print(f"start translation: {input_file_path}")
    start_time = time.time()
    try:
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            original_text = input_file.read()

        translated_text = translate_text(original_text)

        if translated_text:
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(translated_text)
            print(f"translation completed: {output_file_path} ")
        else:
            print(f"failed to translate")

    except FileNotFoundError:
        print(f"no file: {input_file_path}")
    except Exception as e:
        print(f"error occured: {e}")

    end_time = time.time()
    duration = end_time - start_time
    print(f"time taken for {input_file_path}: {duration:.2f} seconds")
def translate_folder(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".md"):
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, input_folder)
                output_file_path = os.path.join(output_folder, relative_path)
                translate_file(input_file_path, output_file_path)

def main():
    parser = argparse.ArgumentParser(description="Translate Markdown files in a folder.")
    parser.add_argument("input_folder", help="Path to the input folder containing markdown files")
    parser.add_argument("output_folder", help="Path to the output folder where translated files will be saved")
    args = parser.parse_args()
    translate_folder(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()