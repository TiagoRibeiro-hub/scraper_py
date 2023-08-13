class Utils:
    @staticmethod
    def split_list(list, n):
        for i in range(0, len(list), n):
            yield list[i:i + n]