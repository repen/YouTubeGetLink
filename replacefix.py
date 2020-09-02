import sys,re
PATH = sys.argv[1]
with open(PATH) as f:
    sr = f.read()
res=re.sub(r'(\[\")(cipher)(\"\])', r'\1signatureCipher\3', sr)
with open(PATH, "w") as f:
    f.write(res)