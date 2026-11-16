from pydantic import BaseModel

class MinimalSource(BaseModel):
    file_path: str
    first_character_index: int
    last_character_index: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MinimalSource):
            return NotImplemented
        if self.file_path != other.file_path:
            return False
        min_end = min(self.last_character_index, other.last_character_index)
        max_start = max(self.first_character_index, other.first_character_index)
        self_span = self.last_character_index - self.first_character_index
        other_span = other.last_character_index - other.first_character_index

        intersection = max(0, min_end - max_start)
        union = self_span + other_span - intersection

        if union == 0:
            iou = 0
        else:
            iou = intersection / union
        
        return iou >= 0.05