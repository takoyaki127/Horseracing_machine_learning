import glob
import re


# 未作成のファイルのリストを作成
def uncreated_files():
    files = glob.glob("./csv/Race_ID/*")
    exclude_files = __create_exclude_files().append('2018-1_2018-12')
    new_files = []
    for file in files:
        if (__file_path_to_date(file) in exclude_files) == False:  # 作成済みか確認
            file = __replace_backslash_to_forwardslash(file)
            new_files.append(file)
            print(file)
    return new_files


# バックスラッシュをフォワードスラッシュに置き換え
def __replace_backslash_to_forwardslash(path: str):
    return path.replace("\\", "/")


# 作成済みのファイルのリストを作成
def __create_exclude_files():
    exclude_files = glob.glob("./csv/Result/[0-9]*")
    exclude_files = [
        # 日付のリスト
        __file_path_to_date(exclude_file)for exclude_file in exclude_files
    ]
    return exclude_files


# ファイルの日付を抽出
def __file_path_to_date(path):
    return re.search('[0-9]*-[0-9]*_[0-9]*-[0-9]*', path).group()


def df_files():
    return glob.glob("./csv/Result/[0-9]*")


if __name__ == "__main__":
    print(uncreated_files())
