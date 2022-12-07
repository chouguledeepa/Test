import argparse
from taskone import do_task_one
from tasktwo import do_task_two
from taskthree import do_task_three


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="To choose which task to perform out of 3")
    parser.add_argument("task", type=str, choices=["task_one", "task_two", "task_three"])
    args = parser.parse_args()
    if args.task == "task_one":
        do_task_one()
    elif args.task == "task_two":
        do_task_two()
    elif args.task == "task_three":
        do_task_three()
    else:
        print("[ERROR] - Incorrect Choice. \n Please choose from, "
              "task_one, task_two, task_three")


