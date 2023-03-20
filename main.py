# python3
# Nikita Smirnovs 221RDB433
import heapq


def parallel_processing(stream, job, time):
    output = []
    threads = [(0, i) for i in range(stream)]

    heapq.heapify(threads)

    for i in range(job):
        data1, thread1 = heapq.heappop(threads)
        output.append((thread1, data1))
        completion_time = data1 + time[i]
        heapq.heappush(threads, (completion_time, thread1))

    return output


def main():

    stream, job = map(int, input().split())
    time = list(map(int, input().split()))

    assert 1 <= stream <= 10 ** 5
    assert 1 <= job <= 10 ** 5
    assert len(time) == job
    assert all(0 <= t <= 10 ** 9 for t in time)

    result = parallel_processing(stream, job, time)

    for thread_index, start_time in result:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
