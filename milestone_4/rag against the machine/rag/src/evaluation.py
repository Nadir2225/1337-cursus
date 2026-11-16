import json
from .models.RagDataset import RagDataset
from .models.StudentSearchResults import StudentSearchResults
from .models.MinimalSearchResults import MinimalSearchResults
from .models.Question import AnsweredQuestion, UnansweredQuestion


def get_ref_question(id: int, dataset_path: str) -> AnsweredQuestion | None:
    with open(dataset_path, "r") as file:
        dataset = json.load(file)
    
    dataset = RagDataset(**dataset)

    for q in dataset.rag_questions:
        if q.question_id == id and isinstance(q, AnsweredQuestion):
            return q
    return None
    

def evaluate(student_search_results_path: str, dataset_path: str):
    with open(student_search_results_path, "r") as file:
        student_search_results = json.load(file)
    
    student_search_results = StudentSearchResults(**student_search_results)

    recalls = {
        "Recall@1": 0,
        "Recall@3": 0,
        "Recall@5": 0,
        "Recall@10": 0,
    }

    q_count = 0
    for question in student_search_results.search_results:
        ref = get_ref_question(question.question_id, dataset_path)
        q_count += 1
        if not ref:
            continue
        ref_source = ref.sources[0]
        if ref_source == question.retrieved_sources[0]:
            recalls["Recall@1"] += 1
            recalls["Recall@3"] += 1
            recalls["Recall@5"] += 1
            recalls["Recall@10"] += 1
        elif ref_source in question.retrieved_sources[:3]:
            recalls["Recall@3"] += 1
            recalls["Recall@5"] += 1
            recalls["Recall@10"] += 1
        elif ref_source in question.retrieved_sources[:5]:
            recalls["Recall@5"] += 1
            recalls["Recall@10"] += 1
        elif ref_source in question.retrieved_sources[:10]:
            recalls["Recall@10"] += 1

    for k in recalls.keys():
        recalls[k] = round(
            recalls[k]/len(student_search_results.search_results), 3
        )
    print("=================================")
    print(f"Questions evaluated: {q_count}")
    for recall, value in recalls.items():
        print(f"{recall}: {value} ({(value * 100):.1f}%)")
