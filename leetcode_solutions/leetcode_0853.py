class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_indices_by_position = sorted(
            range(len(position)), key=lambda idx: position[idx]
        )

        fleet_count, previous_time = 0, 0

        for i in car_indices_by_position[::-1]:
            time_to_target = (target - position[i]) / speed[i]

            if time_to_target > previous_time:
                fleet_count += 1
                previous_time = time_to_target

        return fleet_count

# Time Complexity: O(N log N) sorting the list of positions: This is done by using the .sort() method, which typically 
# has a time complexity of O(N log N), where N is the length of the positions list.
# Space Complexity: Space taken by sorting depends on the implementation, but most sorting algorithms such as Timsort
# (used in Python's sort method) require O(N) space in the worst case.