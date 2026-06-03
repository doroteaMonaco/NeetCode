class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        function = init

        for _ in range(iterations):
            derivation = 2 * function
            function = function - learning_rate * derivation

        return round(function, 5)


#Time complexity: O(iterations) because we perform a constant amount of work for each iteration.
#Space complexity: O(1) because we are using a constant amount of space to store