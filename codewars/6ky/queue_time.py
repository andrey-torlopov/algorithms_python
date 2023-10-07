# There is a queue for the self-checkout tills at the supermarket. Your task is write a function
# to calculate the total time required for all the customers to check out!

# input

# customers: an array of positive integers representing the queue. Each integer represents
# a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output

# The function should return an integer, the total time required.
def queue_time(customers: list[int], n: int):
    if len(customers) == 0:
        return 0
    tills = [0] * n
    for customer in customers:
        tills[0] += customer
        tills.sort()

    return max(tills)


print(queue_time([1, 2, 3, 4, 5], 1))
