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
        "recall@1": 0,
        "recall@3": 0,
        "recall@5": 0,
        "recall@10": 0,
    }

    for question in student_search_results.search_results:
        ref = get_ref_question(question.question_id, dataset_path)
        if not ref:
            continue
        ref_source = ref.sources[0]
        if ref_source == question.retrieved_sources[0]:
            recalls["recall@1"] += 1
            recalls["recall@3"] += 1
            recalls["recall@5"] += 1
            recalls["recall@10"] += 1
        elif ref_source in question.retrieved_sources[:3]:
            recalls["recall@3"] += 1
            recalls["recall@5"] += 1
            recalls["recall@10"] += 1
        elif ref_source in question.retrieved_sources[:5]:
            recalls["recall@5"] += 1
            recalls["recall@10"] += 1
        elif ref_source in question.retrieved_sources[:10]:
            recalls["recall@10"] += 1
    print(recalls)
    for k in recalls.keys():
        recalls[k] = recalls[k]/len(student_search_results.search_results)
    
    print(recalls)
