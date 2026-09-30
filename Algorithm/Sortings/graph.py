import matplotlib.pyplot as plt

#NOTE: when running the code, to check the merge sort times,
# zoom in for better results.

# --------------------------------------
# Data
# --------------------------------------

# Number of elements in each dataset:
sizes = [
    1000,
    10000,
    100000,
    250000,
    500000,
    1000000
]


insertion_times = [
    0.019990921020507812,      # 1000
    2.32167387008667,      # 10000
    240.6452178955078,      # 100000
    2086.038494825363,      # 250000
    8249.954443216324,      # 500000
    32999.8177728653      # 1000000       NOTE: The 1 million time efficiency is expected, not 
                                                #the actual time from experiment. The csegrid
                                                # server is still running the insertion sort algorithm
                                                #and this estimated time is only to show a completed graph
]

merge_times = [
    0.001992940902709961,      # 1000
    0.04258298873901367,      # 10000
    0.35073113441467285,      # 100000
    1.1041626930236816,      # 250000
    2.1213505268096924,      # 500000
    5.291058301925659       # 1000000
]


# -------
# graph
# -------

plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    insertion_times,
    marker='o',
    label='Insertion Sort'
)

plt.plot(
    sizes,
    merge_times,
    marker='o',
    label='Merge Sort'
)


# ------------------
# Labels and title
# ------------------

plt.xlabel('Number of Elements')
plt.ylabel('Execution Time (seconds)')

plt.title('Insertion Sort vs Merge Sort')

plt.legend()
plt.grid(True)


plt.savefig('sorting_comparison.png', dpi=300)

# Display graph
plt.show()