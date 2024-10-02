from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_subject(question: str):
    candidate_labels = ["Mechanical Engineering", "Physics", "Mathematics", "Biology", "Literature"]
    result = classifier(question, candidate_labels)
    return result['labels'][0]  # The most relevant subject
