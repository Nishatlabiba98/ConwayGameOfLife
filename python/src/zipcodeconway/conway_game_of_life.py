from zipcodeconway.simple_window import SimpleWindow


class ConwayGameOfLife:
    """Starter scaffold for Conway's Game of Life lab."""

    def __init__(self, dimension: int, start_matrix: list[list[int]] | None = None):
        self.dimension = dimension
        self.display_window = SimpleWindow(dimension)

        if start_matrix is None:
            self.current_generation = self.create_random_start(dimension)
        else:
            self.current_generation = start_matrix

        self.next_generation = [[0 for _ in range(dimension)] for _ in range(dimension)]

    def create_random_start(self, dimension: int) -> list[list[int]]:
        """
        Contains the logic for the starting scenario.
        Which cells are alive or dead in generation 0.
        Allocates and returns the starting matrix of size 'dimension'.
        """
        import random
        matrix = []
        for i in range(dimension):
            row = []
            for j in range(dimension):
                row.append(random.randint(0, 1))
            matrix.append(row)
        return matrix

    def simulate(self, max_generations: int) -> list[list[int]]:
        """
        Run the simulation for max_generations and return the final state.
        Displays each generation in the window.
        """
        for generation in range(max_generations - 1):
            self.display_window.display(self.current_generation, generation)

            for row in range(self.dimension):
                for col in range(self.dimension):
                    self.next_generation[row][col] = self.is_alive(row, col, self.current_generation)

            self.copy_and_zero_out(self.next_generation, self.current_generation)
            self.display_window.sleep(100)

        return self.current_generation

    def copy_and_zero_out(self, next_matrix: list[list[int]], current_matrix: list[list[int]]) -> None:
        """
        Copy all values from next_matrix to current_matrix,
        then set all values in next_matrix to 0.
        """
        for row in range(self.dimension):
            for col in range(self.dimension):
                current_matrix[row][col] = next_matrix[row][col]
                next_matrix[row][col] = 0

    def is_alive(self, row: int, col: int, world: list[list[int]]) -> int:
        """
        Calculate if the cell at row,col should be alive in the next generation.

        Game rules:
        - Any live cell with fewer than two live neighbours dies.
        - Any live cell with more than three live neighbours dies.
        - Any live cell with two or three live neighbours lives.
        - Any dead cell with exactly three live neighbours becomes alive.

        Use wraparound edges: top/bottom and left/right connect.
        """
        live_neighbors = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r = (row + dr) % self.dimension
                c = (col + dc) % self.dimension
                live_neighbors += world[r][c]

        if world[row][col] == 1:
            return 1 if live_neighbors in (2, 3) else 0
        else:
            return 1 if live_neighbors == 3 else 0


def main() -> None:
    sim = ConwayGameOfLife(50)
    sim.simulate(50)


if __name__ == "__main__":
    main()
