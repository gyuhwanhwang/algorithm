class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        units = 0
        while truckSize and boxTypes:
            box, unit = boxTypes.pop()
            if box >= truckSize:
                units += unit * truckSize
                truckSize = 0
            else:
                units += unit * box
                truckSize -= box
        return units