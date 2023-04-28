import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = [
            ball_color
            for ball_color, num_balls in balls.items()
            for _ in range(num_balls)
        ]

    def draw(self, n: int):
        if n >= len(self.contents):
            result = copy.deepcopy(self.contents)
            self.contents.clear()
            return result

        result: list[str] = []
        for _ in range(n):
            index = random.randrange(0, len(self.contents))
            result.append(self.contents.pop(index))
        return result


def experiment(
    hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int
):
    num_successes = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        result = hat_copy.draw(num_balls_drawn)
        result_dict = dict()
        for ball in result:
            result_dict[ball] = result_dict.get(ball, 0) + 1

        # Assume success
        success = True
        for key, value in expected_balls.items():
            if key not in result_dict:
                success = False
                break
            if result_dict[key] < value:
                success = False
                break

        if success:
            num_successes += 1

    return num_successes / num_experiments
