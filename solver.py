import copy
import signal
import sys
import time
import traceback
from typing import Any, Callable, Dict, List


# ANSI escape codes for styling terminal output
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class TimeoutException(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutException("Time Limit Exceeded")


def _format_val(val: Any) -> str:
    """Helper to format long values so they don't flood the terminal."""
    s = repr(val)
    if len(s) > 100:
        return s[:97] + "..."
    return s


def run_tests(
    func: Callable,
    test_cases: List[Dict[str, Any]],
    time_limit: float = 2.0,
    check_type: bool = True,
    disallow_original_input_return: bool = False,
):
    """
    Test harness for LeetCode/CP problems.
    """
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.BOLD}>>> Testing: {Colors.HEADER}{func.__name__}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.ENDC}\n")

    passed = 0
    total = len(test_cases)

    # Set up signal handler for time limit
    old_handler = signal.signal(signal.SIGALRM, _timeout_handler)

    for i, test in enumerate(test_cases):
        print(f"{Colors.BOLD}[ Test {i + 1} ]{Colors.ENDC}")

        inputs = test.get("inputs", [])
        if not isinstance(inputs, (list, tuple)):
            inputs = [inputs]

        expected = test.get("expected")
        kwargs = test.get("kwargs", {})

        input_copy = copy.deepcopy(inputs)

        try:
            signal.setitimer(signal.ITIMER_REAL, time_limit)
            start_time = time.perf_counter()
            result = func(*inputs, **kwargs)
            end_time = time.perf_counter()
            signal.setitimer(signal.ITIMER_REAL, 0)

        except TimeoutException:
            print(
                f"{Colors.FAIL}[FAIL] Time Limit Exceeded (>{time_limit}s){Colors.ENDC}"
            )
            print(f"   {Colors.BLUE}> Input:{Colors.ENDC} {_format_val(input_copy)}\n")
            continue
        except RecursionError:
            signal.setitimer(signal.ITIMER_REAL, 0)
            print(f"{Colors.FAIL}[FAIL] Recursion Limit Exceeded{Colors.ENDC}")
            print(f"   {Colors.BLUE}> Input:{Colors.ENDC} {_format_val(input_copy)}\n")
            continue
        except Exception as e:
            signal.setitimer(signal.ITIMER_REAL, 0)
            print(f"{Colors.FAIL}[FAIL] Runtime Error{Colors.ENDC}")
            print(f"   {Colors.BLUE}> Input:{Colors.ENDC} {_format_val(input_copy)}")
            print(f"{Colors.WARNING}", end="")
            traceback.print_exc()
            print(f"{Colors.ENDC}\n", end="")
            continue

        # Error Checks
        failed_checks = False

        if check_type and expected is not None:
            if type(result) != type(expected):
                print(f"{Colors.FAIL}[FAIL] Return type mismatch.{Colors.ENDC}")
                print(
                    f"   {Colors.BLUE}> Expected type:{Colors.ENDC} {type(expected).__name__}"
                )
                print(
                    f"   {Colors.BLUE}> Got type:     {Colors.ENDC} {type(result).__name__}\n"
                )
                failed_checks = True

        if not failed_checks and disallow_original_input_return:
            for arg in inputs:
                if isinstance(arg, (list, dict, set)) and id(result) == id(arg):
                    print(
                        f"{Colors.FAIL}[FAIL] Returned original input reference.{Colors.ENDC}"
                    )
                    print(
                        f"   {Colors.WARNING}The problem requires copying/creating a new data structure.{Colors.ENDC}\n"
                    )
                    failed_checks = True
                    break

        if not failed_checks:
            if result == expected:
                duration = (end_time - start_time) * 1000
                print(f"{Colors.GREEN}[PASS] in {duration:.2f}ms{Colors.ENDC}\n")
                passed += 1
            else:
                print(f"{Colors.FAIL}[FAIL] Incorrect Result{Colors.ENDC}")
                print(
                    f"   {Colors.BLUE}> Input:   {Colors.ENDC} {_format_val(input_copy)}"
                )
                print(
                    f"   {Colors.BLUE}> Expected:{Colors.ENDC} {_format_val(expected)}"
                )
                print(
                    f"   {Colors.FAIL}> Got:     {Colors.ENDC} {_format_val(result)}\n"
                )

    # Restore old signal handler
    signal.signal(signal.SIGALRM, old_handler)

    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.ENDC}")
    if passed == total:
        print(
            f"{Colors.BOLD}{Colors.GREEN}[*] All {total} tests passed successfully! [*]{Colors.ENDC}"
        )
    else:
        print(
            f"{Colors.BOLD}{Colors.WARNING}>>> Results: {passed}/{total} passed.{Colors.ENDC}"
        )
        print(f"{Colors.FAIL}[!] Some tests failed. Keep trying!{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.ENDC}\n")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}\n")
