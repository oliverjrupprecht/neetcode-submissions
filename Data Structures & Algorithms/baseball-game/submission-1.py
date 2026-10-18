class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            i = len(record)

            match op:
                case "+":
                    record.append(int(record[i-1])+int(record[i-2]))
                case "D":
                    record.append(int(record[i-1]) * 2)
                case "C":
                    record.pop()
                case _:
                    record.append(int(op))

        return sum(record)


        