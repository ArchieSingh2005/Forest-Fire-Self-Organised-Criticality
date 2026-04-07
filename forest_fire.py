import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# PARAMETERS
# ----------------------------
N = 120
p = 0.05
steps = 500000            # per run
trigger_interval = 40
num_runs = 3              # multiple realizations

# ----------------------------
# NEIGHBORS
# ----------------------------
def get_neighbors(x, y):
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            yield nx, ny

# ----------------------------
# COLLECT AVALANCHES FROM MULTIPLE RUNS
# ----------------------------
all_avalanches = []

for run in range(num_runs):
    print(f"Running simulation {run+1}/{num_runs}...")

    grid = np.zeros((N, N), dtype=int)
    growth_counter = 0
    avalanches = []

    for step in range(steps):

        # Random growth
        x, y = np.random.randint(0, N), np.random.randint(0, N)
        if grid[x, y] == 0 and np.random.rand() < p:
            grid[x, y] = 1
            growth_counter += 1

        # Trigger fire
        if growth_counter >= trigger_interval:

            trees = np.where(grid == 1)

            if len(trees[0]) > 0:
                idx = np.random.randint(len(trees[0]))
                x0, y0 = trees[0][idx], trees[1][idx]

                stack = [(x0, y0)]
                grid[x0, y0] = 2
                size = 0

                while stack:
                    cx, cy = stack.pop()
                    size += 1

                    for nx, ny in get_neighbors(cx, cy):
                        if grid[nx, ny] == 1:
                            grid[nx, ny] = 2
                            stack.append((nx, ny))

                grid[grid == 2] = 0
                avalanches.append(size)

            growth_counter = 0

    all_avalanches.extend(avalanches)

# ----------------------------
# ANALYSIS
# ----------------------------
avalanches = np.array(all_avalanches)

print("Total avalanches collected:", len(avalanches))

if len(avalanches) < 50:
    print("⚠️ Too few avalanches. Increase steps or runs.")
    exit()

# ----------------------------
# LOG BINNING (SMOOTH VERSION)
# ----------------------------
bins = np.logspace(np.log10(1),
                   np.log10(max(avalanches)), 80)

hist, edges = np.histogram(avalanches, bins=bins)

bin_widths = edges[1:] - edges[:-1]
P = hist / (np.sum(hist) * bin_widths)

centers = np.sqrt(edges[:-1] * edges[1:])  # geometric mean

# Remove zeros
valid = P > 0
s = centers[valid]
P = P[valid]

# ----------------------------
# FIT (SCALING REGION)
# ----------------------------
mask = (s > 5) & (s < max(s)/2)
s_fit = s[mask]
P_fit = P[mask]

if len(s_fit) > 5:
    coeffs = np.polyfit(np.log(s_fit), np.log(P_fit), 1)
    tau = -coeffs[0]
    print(f"Critical exponent tau ≈ {tau:.2f}")
else:
    tau = None
    print("Not enough data for fitting")

# ----------------------------
# PLOT
# ----------------------------
plt.figure(figsize=(7,5))

plt.loglog(s, P, 'o', markersize=4, alpha=0.6, label="Data")

if tau is not None:
    plt.loglog(s_fit,
               np.exp(np.polyval(coeffs, np.log(s_fit))),
               '--', linewidth=2,
               label=f"Fit (tau≈{tau:.2f})")

plt.xlabel("Avalanche Size")
plt.ylabel("Probability Density")
plt.title("Avalanche Distribution (SOC Forest Fire Model)")

plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)

plt.tight_layout()
plt.show()
