# Recursive Sorting Algorithm Visualizer

An interactive terminal-based Sorting Algorithm Visualizer built with Python that demonstrates how recursive sorting algorithms work through real-time ASCII animations.

Unlike traditional sorting visualizers that rely heavily on iterative loops, this project showcases purely recursive implementations of multiple classical sorting algorithms. It is designed as an educational tool for learning recursion, understanding algorithm behavior, and comparing algorithm performance directly from the command line.

---

## Features

- Purely recursive implementations of five classical sorting algorithms
- Real-time terminal visualization using ASCII bar graphs
- Smooth animations using ANSI escape codes without excessive screen flickering
- Live algorithm statistics during execution
  - Total steps
  - Comparisons
  - Swaps
- Color-coded visualization
  - Yellow for active comparisons or shifts
  - White for unsorted elements
  - Green for completed sorting
- Supports custom user-defined arrays
- Generates randomized unique arrays automatically
- Adjustable visualization speed
  - Slow
  - Normal
  - Fast
- Automatic performance benchmarking
- Comparative summary table after running all algorithms

---

## Supported Algorithms

### Bubble Sort (Recursive)

Recursively performs each bubble pass until the largest unsorted element reaches its correct position.

**Technique**
- Recursive pass generation
- Recursive traversal

---

### Insertion Sort (Recursive)

Recursively sorts smaller subarrays before inserting elements into their proper positions.

**Technique**
- Recursive insertion
- Recursive shifting

---

### Merge Sort (Recursive)

Uses the divide-and-conquer paradigm by recursively splitting arrays and recursively merging them back together.

**Technique**
- Recursive divide
- Recursive merge

---

### Quick Sort (Recursive)

Partitions the array around a pivot and recursively sorts the resulting partitions.

**Technique**
- Recursive partitioning
- Divide and conquer

---

### Heap Sort (Recursive)

Constructs a max heap recursively and repeatedly extracts the largest element.

**Technique**
- Recursive heapify
- Recursive extraction

---

## Visualization

The program displays the array as horizontal ASCII bars that update in real time.

### Color Legend

| Color | Meaning |
|--------|---------|
| White | Unsorted element |
| Yellow | Current comparison or shift |
| Green | Sorted element |

During execution, the program continuously displays:

- Current array state
- Number of steps
- Number of comparisons
- Number of swaps
- Current algorithm
- Execution progress

---

## Performance Summary

After all selected algorithms finish, the program generates a benchmark table comparing their performance.

Metrics include:

- Execution time
- Total comparisons
- Total swaps
- Total steps

The application also identifies the best-performing algorithm for each measured category.

---

## Technical Stack

The project is implemented entirely in Python using only the standard library.

| Module | Purpose |
|---------|---------|
| `os` | Terminal operations and screen handling |
| `sys` | Stream flushing and Windows ANSI support |
| `time` | High-precision timing and animation delays |
| `random` | Random array generation |

---

## Requirements

- Python 3.10 or newer
- A terminal that supports ANSI escape sequences

No third-party libraries are required.

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/your-username/recursive-sorting-visualizer.git
```

Navigate into the project directory:

```bash
cd recursive-sorting-visualizer
```

Run the program:

```bash
python main.py
```

---

## Example Workflow

1. Launch the application.
2. Choose a sorting algorithm or run all algorithms.
3. Enter a custom array or generate a random one.
4. Select the visualization speed.
5. Watch the sorting process in real time.
6. Review the benchmark summary after completion.

---

## Educational Purpose

This project is intended to help students and programming enthusiasts understand:

- Recursion fundamentals
- Sorting algorithm mechanics
- Divide-and-conquer strategies
- Recursive state management
- Algorithm complexity
- Performance comparison
- Terminal-based visualization techniques

---

## Project Highlights

- Pure recursive implementations
- Interactive command-line interface
- Live algorithm visualization
- Performance benchmarking
- Beginner-friendly educational design
- Uses only Python's standard library

---

## Future Improvements

Potential enhancements include:

- Additional recursive sorting algorithms
- Vertical bar visualization
- Statistical graph generation
- Export benchmark results to CSV
- Custom color themes
- Sound effects during sorting
- Support for larger datasets
- Interactive pause and resume controls

---

## License

This project is available for educational and personal use.

---

## Author

Developed as a Python educational project demonstrating recursive sorting algorithms, terminal visualization, and algorithm performance analysis.