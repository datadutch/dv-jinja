# write_messages.py

from jinja2 import Environment, FileSystemLoader
import os

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("message.txt")

for student in students:
    filename = f"message_{student['name'].lower()}.txt"
    filename2 = os.path.join(output_folder, filename)
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename2, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")