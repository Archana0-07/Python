# ==================================================
# 1️⃣ Tuple Iteration Loop
# ==================================================
a=10,20,30,40,50
for v in a:
    print(v) # prints each value in the tuple

print("\n")  # separate outputs

# ==================================================
# 2️⃣ Range Loop 3 to 19
# ==================================================
for v in range(3,20):
    print(v)  # prints numbers from 3 to 19

print("\n")

# ==================================================
# 3️⃣ Range Loop with Step 3
# ==================================================
for v in range(3,20,3):
    print(v) # prints numbers from 3 to 19, step 3 (3,6,9,...)

print("\n")

# ==================================================
# 4️⃣ Nested For Loop
# ==================================================
for i in range(3):   # outer loop 0,1,2
    for j in range(5):  # inner loop 0,1,2,3,4
        print(i)   # prints value of i 5 times for each i



