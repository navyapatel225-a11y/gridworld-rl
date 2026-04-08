from baseline import baseline
from task import run_task

def grade():
    test_inputs = ["Ansh", "OpenEnv", "Tester"]

    results = []

    for inp in test_inputs:
        expected = baseline(inp)
        actual = run_task(inp)

        results.append({
            "input": inp,
            "expected": expected,
            "actual": actual,
            "pass": expected == actual
        })

    score = sum(r["pass"] for r in results) / len(results)

    return {
        "score": score,
        "details": results
    }


if __name__ == "__main__":
    print(grade())
