# Minesweeper AI: Logical Reasoning and Approach

## Overview
The Minesweeper AI is designed to intelligently deduce safe moves and detect mines based on logical inference. The AI progressively gathers knowledge about the game board, updating its understanding of which cells contain mines and which are safe.

## Logical Reasoning Process

### Step 1: **Updating Knowledge**
When the AI receives information about a safe cell, it:
1. Marks the cell as a move made.
2. Marks the cell as safe.
3. Collects information about neighboring cells and the number of adjacent mines.
4. Creates a new sentence representing this information and adds it to the knowledge base.

### Step 2: **Deduction of Mines and Safe Cells**
- If a sentence states that all its cells are mines (`count == len(cells)`), those cells are marked as mines.
- If a sentence states that none of its cells are mines (`count == 0`), those cells are marked as safe.
- This process is applied iteratively to refine knowledge.

### Step 3: **Inference from Existing Knowledge**
- If one sentence is a subset of another, a new sentence can be inferred:
  - Example: `{(1,1), (1,2), (1,3)} = 2` and `{(1,2), (1,3)} = 1` implies `{(1,1)} = 1`.
- New sentences derived this way are added to the knowledge base for further reasoning.

### Step 4: **Making Moves**
- **Safe Move:** The AI selects a known safe cell that has not been clicked yet.
- **Random Move:** If no safe moves exist, the AI picks a random unclicked cell that is not known to be a mine.

## Conclusion
The AI uses logical inference to solve Minesweeper efficiently, reducing uncertainty whenever possible. Through systematic deduction and incremental knowledge updates, it minimizes the risk of stepping on a mine and improves its performance over time.

