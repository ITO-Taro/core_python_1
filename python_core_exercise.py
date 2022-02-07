"python core exercise class PY131"



class PythonCoreExercise:
    "contians char_counter, char_manipulation, & distance funcs"

    # def __init__(self, var_x, var_y):
    #     self.var_x = var_x
    #     self.var_y = var_y

    @classmethod
    def find_modes(cls, var_x):
        "finds duplicated values amd return them in dictionary format ('vallues': 'frequency')"
        data, modes = {}, {}
        lst_x = [i for i in var_x]
        lst_x.sort()
        cnt = 1
        for num in range(1, len(lst_x)):
            if lst_x[num] == lst_x[num-1]:
                cnt += 1
            else:
                data[lst_x[num-1]] = cnt
                cnt = 1
        for key, val in data.items():
            if val == max(data.values()) and val > 1:
                modes[key] = val
        return modes

    # def char_counter(self, x):
    #     "char_counter with ord"
    #     res = {'chars': 0, 'digits': 0, 'symbol': 0}
    #     nums = [ord(i) for i in x.lower()]
    #     for n in nums:
    #         if n in range(97, 123):
    #             res['chars'] += 1
    #         elif n in range(48, 58):
    #             res['digits'] += 1
    #         else:
    #             res['symbol'] += 1
    #     return res

    def char_counter(self, var_x):
        "counts the number of alphabets, nums, & symbols and returns the counts in that order"
        res = {'chars': 0, 'digits': 0, 'symbol': 0}
        for i in var_x:
            if i.isalpha():
                res['chars'] += 1
            elif i.isnumeric():
                res['digits'] += 1
            else:
                res['symbol'] += 1
        return res

    def char_manupilation(self, var_one, var_two):
        "takes two strings & transform the former to the latter and returns it"
        if var_one != var_two:
            caps = [var_two.index(i) for i in var_two if i.isupper()]
            common = [i for i in var_one if i in var_two]
            only_var_two = [i for i in var_two if not i in common]
            var_one = list(set(common+only_var_two))
            duplicates = self.find_modes(var_two)
            cnt = 1
            for key, val in duplicates.items():
                while val > cnt:
                    var_one.append(key)
                    cnt += 1
            for num in range(len(var_two)):
                var_one[num] = var_two[num]
            res = "".join([var_one[num].upper() if num in caps else var_one[num]
                          for num in range(len(var_one))])
        else:
            res = var_one
        return res

    def distance(self, str_x, str_y):
        "returns the minimum number of operations required to trnasform str_x to str_y"
        num_1, num_2 = len(str_x), len(str_y)
        matrix = [[i+j for j in range(num_2+1)] for i in range(num_1+1)]
        for i in range(1, num_1+1):
            for j in range(1, num_2+1):
                if str_x[i-1] == str_y[j-1]:
                    d = 0
                else:
                    d = 1
                matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1], matrix[i][j]+d)
        return matrix[-1][-1]

    def is_anagram(self, word_1, word_2):
        return sorted(word_1) == sorted(word_2)