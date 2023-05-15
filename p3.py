import concurrent.futures




class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=num_threads)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.terminate()

    def map(self, func, iterable):
        chunk_size = len(iterable) // self.num_threads
        chunks = [iterable[i:i+chunk_size] for i in range(0, len(iterable), chunk_size)]
        futures = []
        for chunk in chunks:
            future = self.executor.submit(func, chunk)
            futures.append(future)
        results = []
        for future in futures:
            result = future.result()
            results.extend(result)
        return results

    def terminate(self):
        self.executor.shutdown()

    def join(self):
        self.executor.shutdown(wait=True)

