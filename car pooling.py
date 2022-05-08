class Solution:
    def carPooling(self, trips, capacity):
        pickup, drop = [], []
        trips_pick, trips_drop = trips[:], trips[:]
        trips_drop.sort(key=lambda x: x[2])
        for trip in trips_drop:
            drop.append(trip[2])

        trips_pick.sort(key=lambda x: x[1])
        for trip in trips_pick:
            pickup.append(trip[1])

        n = len(trips)
        i, j = 0, 0
        bus_people = 0
        print(trips_pick)
        print(trips_drop)
        while i < n or j < n:
            if bus_people > capacity:
                return False
            if i < n and pickup[i] < drop[j]:
                bus_people += trips_pick[i][0]
                i = i + 1
            else:
                bus_people -= trips_drop[j][0]
                j = j + 1
        #print(bus_people)

        if bus_people == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    arr = [[10,5,7],[10,3,4],[7,1,8],[6,3,4]]
    c = 24
    print(Solution().carPooling(arr, c))