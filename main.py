import pygame
from grid import Grid
from algorithms import astar

# Window setup
WIDTH = 600
ROWS = 30
pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer (A*)")

def main():
    grid = Grid(ROWS, WIDTH)

    start = None
    end = None
    run = True

    while run:
        grid.draw(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Left click -> place start, end, or barriers
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked(pos)
                cell = grid.grid[row][col]

                if not start and cell != end:
                    start = cell
                    start.make_start()
                elif not end and cell != start:
                    end = cell
                    end.make_end()
                elif cell != end and cell != start:
                    cell.make_barrier()

            # Right click -> reset a cell
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked(pos)
                cell = grid.grid[row][col]
                cell.reset()
                if cell == start:
                    start = None
                elif cell == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid.grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    astar(lambda: grid.draw(WIN), grid.grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = Grid(ROWS, WIDTH)

    pygame.quit()

if __name__ == "__main__":
    main()
