import json
import html2text

with open('website_analysis_results.json') as f:
    data = json.load(f)

with open('output.txt', 'w') as f:
    for obj in data:
        f.write(f"Domain: {obj['domain']}\n")
        f.write("Technology Stack:\n")
        for tech in obj['technology_stack']:
            text = html2text.html2text(tech)
            f.write(f"- {text.strip()}\n")
        f.write("\n")  # add a newline to separate each object's output