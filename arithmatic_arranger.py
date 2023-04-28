def arithmetic_arranger(problems, compute_and_display_results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    split_up_problems = []
    for p in problems:
        a, op, b = p.split(" ")
        if op not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not (a.isnumeric() and b.isnumeric()):
            return "Error: Numbers must only contain digits."

        split_up_problems.append((a, op, b))

    arranged_problems = ""

    # Build first line of result string
    first_line = []
    for a, op, b in split_up_problems:
        length = max(len(a), len(b))
        first_line.append(f"  {a:>{length}}")
    first_line_str = (" " * 4).join(first_line)
    arranged_problems += first_line_str + "\n"

    # Build second line
    second_line = []
    for a, op, b in split_up_problems:
        length = max(len(a), len(b))
        second_line.append(f"{op} {b:>{length}}")
    second_line_str = (" " * 4).join(second_line)
    arranged_problems += second_line_str + "\n"

    # Build third line
    third_line = []
    for a, op, b in split_up_problems:
        length = max(len(a), len(b))
        # Add 2 to length to account for operation and space between-
        # operation and operand
        third_line.append("-" * (length + 2))
    third_line_str = (" " * 4).join(third_line)
    arranged_problems += third_line_str + "\n"

    if compute_and_display_results:
        # Build fourth line
        fourth_line = []
        for a, op, b in split_up_problems:
            length = max(len(a), len(b))
            result = (int(a) + int(b)) if op == "+" else (int(a) - int(b))
            fourth_line.append(f"{result:>{length + 2}}")
        fourth_line_str = (" " * 4).join(fourth_line)
        arranged_problems += fourth_line_str + "\n"

    return arranged_problems


# print(
#     repr(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
# )

foo = """  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
"""

# print(
#     repr(
#         foo
#         == arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
#     )
# )


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
foo = '  3801      123\n-    2    +  49\n------    -----'
print(foo == arithmetic_arranger(["3801 - 2", "123 + 49"])[:-1])
