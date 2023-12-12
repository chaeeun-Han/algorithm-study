def solution(slice, n):
    result = 0
    while (slice * result < n):
        result += 1
    return result