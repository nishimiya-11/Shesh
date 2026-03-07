import time
from concurrent.futures import ThreadPoolExecutor

# ============================================================
# Parallel Order Processing System
# ============================================================
# 1. Which concurrency tool did you use?
#    I used concurrent.futures with ThreadPoolExecutor.
#
# 2. Why did you select this approach?
#    I selected ThreadPoolExecutor because it is simple to use and works well
#    for tasks like order processing where multiple operations can run at the same time.
#
# 3. Is your program using task parallelism or data parallelism? Explain briefly.
#    This program uses data parallelism because the same process_order function
#    is applied to multiple different orders concurrently.
#
# 4. Is this example primarily CPU-bound or I/O-bound?
#    This example is primarily I/O-bound because the delays simulate waiting
#    for external operations such as payment systems, packaging updates, or shipping preparation.
#
# 5. How does the simulated delay (time.sleep) represent real-world system behavior?
#    The time.sleep() calls represent waiting time in real systems, such as
#    validating order details, confirming payment, preparing packaging, and updating shipping status.
#
# 6. Explain how processing orders concurrently improves system performance.
#    Processing orders concurrently improves performance because multiple orders
#    can move through the system at the same time instead of waiting for one order
#    to finish completely before starting the next.
#
# 7. If the system needed to process thousands of orders, what improvement could be made?
#    If the system needed to handle thousands of orders, improvements could include
#    using a task queue, async processing, distributed workers, or scaling across multiple servers.
# ============================================================


def process_order(order_id):
    print(f"Processing Order {order_id}...")
    
    print(f"Order {order_id}: Verifying order")
    time.sleep(1)

    print(f"Order {order_id}: Processing payment")
    time.sleep(1)

    print(f"Order {order_id}: Packaging item")
    time.sleep(1)

    print(f"Order {order_id}: Ready for shipping")
    time.sleep(1)

    print(f"Order {order_id} completed.")


def main():
    orders = list(range(1, 11))

    print("Starting parallel order processing...\n")

    with ThreadPoolExecutor(max_workers=5) as executor:
        list(executor.map(process_order, orders))

    print("\nAll orders have been completed.")


if __name__ == "__main__":
    main()
