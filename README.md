# Maze Solver

Solve ASCII mazes using **Breadth-First Search (BFS)** and watch the path unfold in real time—without flicker—directly in your terminal.

---

## Features

* **BFS shortest-path** solver from `S` (start) to `E` (exit)
* **Smooth in-place animation** using ANSI cursor movement (no screen flashing)
* Simple **maze file format** (`maze.txt`)
* Minimal dependencies (standard library only)

---

## Requirements

* Python **3.10+** (for `list[str]` type hints)
* A terminal that supports ANSI escape codes

  * Windows 10+ terminals usually work out of the box. If you see odd characters, enable ANSI or use Windows Terminal.

---

## Maze File Format (`maze.txt`)

* Walls are **`█`** (solid block). In your script, dots `.` are converted to `█` on load, so you can author with either.
* Open paths are **spaces** (` `).
* Start is **`S`**, exit is **`E`**.
* **Important:** The maze **must be fully enclosed by walls** to avoid out-of-bounds moves.

**Example:**

```
█████████
█S      █
█ ███ █ █
█     E █
█████████
```

---

## Run

```bash
python3 maze_solver.py
```

You should see:

* `Solving maze...`, then
* The maze updating in-place with the discovered path marked by `.`

---

## How It Works

1. **Load & Normalize**

   * Reads `maze.txt`, converts `.` to `█` (so authoring is easier), strips newlines.
2. **BFS Search** (`solve_maze`)

   * Finds `S`, explores neighbors in four directions (UDLR), and reconstructs the path to `E` using a `previous_node` map.
3. **Animation** (`animate_path`)

   * Draws the maze once with `render()`.
   * For each position on the solution path, marks it with `.` and **moves the cursor up by the maze height** using `\x1b[{rows}A`, then reprints the grid—creating a smooth animation with no screen clear.

---

## Configuration

* **Speed:** `animate_path(..., delay=0.5)` → decrease for faster animation.
* **Path marker:** `mark='.'` → set to `'·'`, `'o'`, `'*'`, etc.
* **Maze authoring:** Write with spaces and `.` for readability; the loader converts `.` to walls.

---

## Implementation Notes

* **Bounds:** `get_legal_moves` assumes the maze border is walled. Keep the outer frame as `█` to prevent index errors.
* **Visited set:** Prevents revisiting coordinates; BFS guarantees shortest path in an unweighted grid.
* **Path reconstruction:** Starts from `E` and walks back via `previous_node` to `S`, then reverses.

---

## Quick Checklist

* ✅ `maze.txt` present and rectangular (equal-length rows)
* ✅ Exactly one `S` and one `E`
* ✅ Outer border fully `█`

---

## License

This project is licensed under the MIT License. Feel free to modify and use it.

___

## Author
**Dhruv Pharasi**

[GitHub](https://github.com/dhruv-pharasi) • [LinkedIn](https://www.linkedin.com/in/dhruvpharasi/)