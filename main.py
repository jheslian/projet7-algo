from timeit import default_timer as timer
from datetime import timedelta
from algo.optimized import optimized
from algo.brutforce import brutforce


def main():
    files = ['dataset/csv/brutforce.csv', 'dataset/csv/dataset1_Python+P7.csv', 'dataset/csv/dataset2_Python+P7.csv']
    for file_path in files:
        start = timer()
        optimized(file_path)
        end = timer()
        print(f"Optimize file:{file_path} finished in {timedelta(seconds=end - start)} seconds")

    start = timer()
    brutforce(files[0])
    end = timer()
    print(f"Brutforce file:{files[0]} finished in {timedelta(seconds=end - start)} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
