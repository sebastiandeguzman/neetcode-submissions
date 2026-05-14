class Solution:
    def encode(self, strs: List[str]) -> str:
        x = ""
        for t in strs:
            x = f"{x}&&&&{t}"
        return x
    def decode(self, s: str) -> List[str]:
        return s.split("&&&&")[1:]