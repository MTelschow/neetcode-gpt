class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        current = init

        for _ in range(iterations):
            derivitatve = 2 * current

            current -= derivitatve * learning_rate

        return round(current, 5)
    