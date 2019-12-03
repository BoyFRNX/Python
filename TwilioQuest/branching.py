import sys

result_sum = int(sys.argv[1]) + int(sys.argv[2])

if result_sum <= 0:
    print("You have chosen the path of destitution.")
elif 1 <= result_sum <= 100:
    print("You have chosen the path of plenty.")
elif result_sum > 100:
    print("You have chosen the path of excess.")
