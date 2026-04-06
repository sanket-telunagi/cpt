# Solution for 874. Walking Robot Simulation
# Platform: LeetCode
# Date: 2026-04-06
#

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir_map = {"east": (1, 0), "west": (-1, 0), "south": (0, -1), "north": (0, 1)}

        face_map = {
            "east": {"2": "north", "1": "south"},
            "west": {"2": "south", "1": "north"},
            "north": {"2": "west", "1": "east"},
            "south": {"2": "east", "1": "west"},
        }

        face_direction = "north"
        robot_curr_pos = [0, 0]
        max_distance = 0

        # uses hashing function, hence faster
        obstacles = set([tuple(obstacle) for obstacle in obstacles])

        for command in commands:
            if command == -1 or command == -2:
                face_direction = face_map[face_direction]["1" if command == -1 else "2"]
            else:
                for i in range(command):
                    x, y = dir_map[face_direction]
                    robot_next_pos = [robot_curr_pos[0] + x, robot_curr_pos[1] + y]

                    if tuple(robot_next_pos) in obstacles:
                        break
                    else:
                        robot_curr_pos = robot_next_pos
            max_distance = max(
                max_distance, (robot_curr_pos[0] ** 2 + robot_curr_pos[1] ** 2)
            )

        return max_distance
