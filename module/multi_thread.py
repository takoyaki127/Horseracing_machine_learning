from threading import Thread


class MultiThread():
    def __init__(self, func, file_list) -> None:
        self.threads: list[Thread] = []
        self.__create_threads(func, file_list)
        print('created threads')

    def __create_threads(self, func, file_list):
        for file in file_list:
            self.threads.append(Thread(target=func, args=(file,)))

    def start(self, thread_num=1):
        canContinue = True
        while canContinue:
            print('threads start')
            canContinue = self.__multi_thread_start(thread_num)
            print('threads finish')

    def __multi_thread_start(self, thread_num):
        unexecuted_threads = len(self.threads)  # 未実行のスレッド数

        if unexecuted_threads <= 0:
            return False

        if unexecuted_threads < thread_num:
            self.__thread_start(unexecuted_threads)
            self.__thread_join(unexecuted_threads)
            return False

        self.__thread_start(thread_num)
        self.__thread_join(thread_num)
        self.threads = self.threads[thread_num:]  # 終了したスレッドを除外
        return True

    def __thread_start(self, n):
        for i in range(n):
            self.threads[i].start()

    def __thread_join(self, n):
        for i in range(n):
            self.threads[i].join()
