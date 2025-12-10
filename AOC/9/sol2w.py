import sys
from collections import deque


def solve():
    pairs = []
    
    while True:
        try:
            line = input().strip()
            if not line: break
            coords = [int(i) for i in line.split(',')]
            pairs.append(coords)
        except EOFError:
            break

    
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]
    
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    width = max_x - min_x + 3
    height = max_y - min_y + 3
    
    normalized_pairs = [[p[0] - min_x + 1, p[1] - min_y + 1] for p in pairs]

    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    num_points = len(normalized_pairs)
    for i in range(num_points):
        p1 = normalized_pairs[i]
        p2 = normalized_pairs[(i + 1) % num_points]
        
        x1, y1 = p1
        x2, y2 = p2
        
        if y1 == y2:
            start, end = min(x1, x2), max(x1, x2)
            for x in range(start, end + 1):
                grid[y1][x] = 1
        elif x1 == x2:
            start, end = min(y1, y2), max(y1, y2)
            for y in range(start, end + 1):
                grid[y][x1] = 1

    queue = deque([(0, 0)])
    seen_outside = set([(0, 0)])
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] == 0 and (nx, ny) not in seen_outside:
                    seen_outside.add((nx, ny))
                    queue.append((nx, ny))

    valid_grid = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if (x, y) not in seen_outside:
                valid_grid[y][x] = 1
            else:
                valid_grid[y][x] = 0

    prefix = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    
    for y in range(height):
        for x in range(width):
            prefix[y+1][x+1] = (valid_grid[y][x] 
                                + prefix[y][x+1] 
                                + prefix[y+1][x] 
                                - prefix[y][x])

    def get_sum(x1, y1, x2, y2):
        x_start, x_end = min(x1, x2), max(x1, x2)
        y_start, y_end = min(y1, y2), max(y1, y2)
        
        return (prefix[y_end+1][x_end+1] 
                - prefix[y_start][x_end+1] 
                - prefix[y_end+1][x_start] 
                + prefix[y_start][x_start])

    max_area = 0
    best_pair = []
    
    for i in range(len(normalized_pairs)):
        for j in range(i + 1, len(normalized_pairs)):
            p1 = normalized_pairs[i]
            p2 = normalized_pairs[j]
            
            x1, y1 = p1
            x2, y2 = p2
            
            w = abs(x2 - x1) + 1
            h = abs(y2 - y1) + 1
            area = w * h
            
            if area <= max_area:
                continue
                
            grid_sum = get_sum(x1, y1, x2, y2)
            
            if grid_sum == area:
                max_area = area
                orig_p1 = [x1 + min_x - 1, y1 + min_y - 1]
                orig_p2 = [x2 + min_x - 1, y2 + min_y - 1]
                best_pair = [orig_p1, orig_p2]

    print(f"Max Area: {max_area}")
    print(f"Corners: {best_pair}")

if __name__ == "__main__":
    solve()
