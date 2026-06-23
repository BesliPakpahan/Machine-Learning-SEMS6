import fitz
doc = fitz.open("Week 13 - Transfer Learning.pdf")
text = ""
for i, page in enumerate(doc):
    text += f"\n--- PAGE {i+1} ---\n" + page.get_text()
with open("transfer_learning_content.txt", "w") as f:
    f.write(text)
print("Done!")
