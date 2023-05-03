from threading import Thread
from tqdm import tqdm


class MultiThread():
    def __init__(self, target, args_list: list[tuple]) -> None:
        self.threads: list[Thread] = []
        self.__target = target
        self.__args_list = args_list
        self.__create_threads()

    def __create_threads(self):
        for args in tqdm(self.__args_list):
            self.threads.append(Thread(target=self.__target, args=args))
        print('created threads')

    def start(self, thread_num=1):
        canContinue = True
        while canContinue:
            print('threads start')
            canContinue = self.__multi_thread_start(
                thread_num)  # 残りの処理がない場合Falseを返します
            print('threads finish')

    def __multi_thread_start(self, thread_num):
        unexecuted_threads = len(self.threads)  # 未実行のスレッド数

        if unexecuted_threads <= 0:  # 残りの処理がない場合
            return False

        if unexecuted_threads < thread_num:  # 残りの処理がスレッド数より少ない場合
            self.__thread_start(unexecuted_threads)
            self.__thread_join(unexecuted_threads)
            return False

        self.__thread_start(thread_num)
        self.__thread_join(thread_num)
        self.threads = self.threads[thread_num:]  # 終了したスレッドを除外
        return True

    def __thread_start(self, n):  # スレッドの0~(n-1)番目まで実行
        for i in range(n):
            self.threads[i].start()

    def __thread_join(self, n):  # スレッドの0~(n-1)番目が完了するまで待機
        for i in range(n):
            self.threads[i].join()
