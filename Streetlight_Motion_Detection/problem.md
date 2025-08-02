# Problem: Streetlight Motion Detection Duration

In a city, a streetlight turns on automatically and stays on for exactly **B** seconds each time it detects motion. If it detects motion again **before turning off**, the timer **resets**, and it stays on for another **B** seconds **from the new detection time**.

You are given a list **A** where each element **A\[i]** indicates the time (in seconds) when the streetlight detects motion, and an integer **B** (in seconds).

Your task is to calculate the **total time** the streetlight remains on.

### Input:

* An integer list **A** of length **n**, where **A\[i]** represents the timestamp (in increasing order) of the i-th motion detection.
* An integer **B** representing the duration the light stays on after a detection.

### Output:

* Return an integer representing the **total number of seconds** the streetlight stays on.

### Example:

**Input:**

```
A = [2, 5, 6, 10], B = 4
```

**Output:**

```
12
```

### Explanation:

* First motion at 2 → light on from 2 to 6
* Second motion at 5 → before it turned off, so it resets → on from 5 to 9
* Third motion at 6 → again before it turned off → resets → on from 6 to 10
* Fourth motion at 10 → exactly when it turns off, counts as new → on from 10 to 14

So the total duration is:

* \[2, 6) → 4 seconds
* \[6, 10) → 4 seconds
* \[10, 14) → 4 seconds
* Total = 12 seconds
