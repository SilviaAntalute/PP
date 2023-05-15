import asyncio

async def calculate_sum(n):
    total_sum = sum(range(n+1))
    return total_sum

async def main():
    n_values = [100, 200, 300, 400]

    results = []

    # Crearea corutinelor pentru fiecare valoare a lui n
    coroutines = [calculate_sum(n) for n in n_values]

    # Așteptarea finalizării corutinelor și colectarea rezultatelor
    results = await asyncio.gather(*coroutines)

    for n, result in zip(n_values, results):
        print(f"Suma pentru n = {n} este: {result}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())