class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distFrom =[]
        hrTilDist = []
        combined = []
        curr = []
        for m in range(len(position)):
            curr.append(position[m])
            curr.append(speed[m])
            combined.append(curr)
            curr = []
        combined.sort(key=lambda position: position[0], reverse = True)
        print(combined)
        for i in range(len(combined)):
            hrTilDist.append((target - combined[i][0])/combined[i][1])
        
        greatest = hrTilDist[0]
        fleetCount = 1
        print(hrTilDist)
        for j in range(len(hrTilDist)):
            if hrTilDist[j] > greatest:
                fleetCount +=1
                greatest = hrTilDist[j]
                print(greatest)

        
        return fleetCount

        
        