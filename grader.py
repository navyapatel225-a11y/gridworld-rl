def grade(rewards):
    if not rewards:
        return 0.0

    score = sum(rewards) / (len(rewards) * 10)
    return max(0.0, min(score, 1.0))


if __name__ == "__main__":
    print(grade([1, 2, 3]))