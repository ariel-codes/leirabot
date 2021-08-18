import random

from extractor import WhatsappExtractor

if __name__ == '__main__':
    e = WhatsappExtractor(platform='ios')
    e.extract(open("training_data/isabel.txt"))
    contacts = e.contacts()
    print(f"Contatos: {contacts}")
    sampled_contact = random.sample(contacts, 1)[0]
    print(f"Random samples ('{sampled_contact}', k=5): {random.sample(e.messages_from(sampled_contact), 5)}")
