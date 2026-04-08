from baseline import baseline
from inference import predict

def grade():
    test_cases = ["Ansh", "OpenEnv", "Tester"]

    results = []

    for inp in test_cases:
        expected = baseline(inp)
        actual = predict(inp)

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
