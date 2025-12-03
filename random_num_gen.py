import random 


non_phishing = "non_phishing"

phishing = "phishing"

for i in range(1, 51):
    label = random.choice([phishing, non_phishing])
    if label == phishing:
        print(f"{i}. phishing email")
    else:
        print(f"{i}. non-phishing email")