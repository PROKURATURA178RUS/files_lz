import docx
doc = docx.Document(r"lion.docx")
from collections import Counter
Counter(doc).most_common(3)