class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "67676-----676767-"
        return "67676-----676767".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "67676-----676767-":
            return []
        return s.split("67676-----676767")